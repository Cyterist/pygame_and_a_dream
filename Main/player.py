import pygame as pg
from information import *
from support import import_folder
from snowball import *
from debug import *
from combat import *
from fights import *
from dialog import *
pg.font.init()

class Player(pg.sprite.Sprite):

    def __init__(self, pos, groups, obstacle_sprites, snowman_group, level):
        super().__init__(groups)
        self.snowman_group = snowman_group

        self.image = pg.image.load('../Main/data/32-bit_placeholders/tile000.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        # Adjust once placeholders are not in use
        self.hitbox = self.rect.inflate(-29, -11)
        
        # Graphics
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0

        # Change later for sprite animation
        self.animation_speed = 0.15

        # Must normalize later
        self.direction = pg.math.Vector2()
        self.cooldown = 0
        self.end_cooldown = 0
        self.combat = Combat()
        self.combat_cooldown = 0
        self.wait = 10
        self.end_wait = 100
        self.combat_wait = 250
        self.speed = 5
        self.cooldown = 0
        self.wait = 100
        self.throwing = False
        self.snowball_cooldown = 721
        self.snowball_time = None
        self.obstacle_sprites = obstacle_sprites
        self.vel = pg.math.Vector2(0, 0)
        self.throwing = False
        self.talk = False
        self.talking = False
        self.talking_cooldown = 0
        self.talking_wait = 100
        self.end_talk = False
        self.creeper1 = False
        self.creeper2 = False


    # main character sprites and animation
    def import_player_assets(self):
        character_path = '../Main/data/player/'
        # TODO Get animation states, and import into self.animations
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           'right_throw': [], 'left_throw': [], 'up_throw': [], 'down_throw': []
                           }
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)


    def input(self):
        self.cooldown += 2
        if not self.talking:
            self.talk = False
        keys = pg.key.get_pressed()

        # Reset the direction vector
        self.direction = pg.math.Vector2(0, 0)

        # Check each key separately to set the corresponding direction
        if keys[pg.K_w]:
            self.direction.y = -1
            self.status = 'up'
            if self.snowball.direction == pg.math.Vector2(0, -1):
                self.status = 'up'
        elif keys[pg.K_s]:
            self.direction.y = 1
            self.status = 'down'

        if keys[pg.K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pg.K_a]:
            self.direction.x = -1
            self.status = 'left'
       
        if keys[pg.K_SPACE]:
            if self.cooldown > self.wait:                 
                if self.end_talk:
                    end_conversation(self)
            
                elif not self.talking:
                    if not self.talk:
                        self.talk = True
                        if fights['creeper2']['fight_won'] or fights['creeper1']['fight_won']:
                            self.combat_cooldown = 0
                self.cooldown = 0
            
                if self.talking and self.end_talk:
                    self.talking = False
            self.cooldown += 1

        

        # Normalize the direction vector only if it is not the zero vector
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        # Check for arrow key presses to throw snowball
        if not self.throwing:
            if keys[pg.K_UP]:
                self.status = 'up'
                self.snowball.direction = pg.math.Vector2(0, -1)
                self.launch_snowball()
            elif keys[pg.K_DOWN]:
                self.status = 'down'
                self.snowball.direction = pg.math.Vector2(0, 1)
                self.launch_snowball()
            elif keys[pg.K_LEFT]:
                self.status = 'left'
                self.snowball.direction = pg.math.Vector2(-1, 0)
                self.launch_snowball()
            elif keys[pg.K_RIGHT]:
                self.status = 'right'
                self.snowball.direction = pg.math.Vector2(1, 0)
                self.launch_snowball()
        
    def move(self, speed):
        if not self.throwing:
            self.vel.x = 0
            self.vel.y = 0

            # Get the normalized direction vector only if the player is moving
            if self.direction.x != 0 or self.direction.y != 0:
                self.direction = self.direction.normalize()

            self.hitbox.x += self.direction.x * speed
            self.collision('horizontal')
            self.hitbox.y += self.direction.y * speed
            self.collision('vertical')
            self.rect.center = self.hitbox.center


    def get_status(self):

        # idle status
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'throw' in self.status:
                self.status = self.status + '_idle'
            
        if self.throwing:
            self.direction.x = 0
            self.direction.y = 0
            if not 'throw' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_throw')
                else:
                    self.status = self.status + '_throw'
        else:
            if 'throw' in self.status:
              self.status = self.status.replace('_throw', '')

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.launch_snowball()

    
    # This system will only work with static obstacles.
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                # if sprite.sprite_type == 'enemy' and self.rect.colliderect(sprite.rect):
                #     pass
                if sprite.sprite_type == 'jack' and self.rect.colliderect(sprite.rect) and self.talk:
                    dialog['d']['jackRun'] = True
                    jack_dialog(self)

                elif sprite.sprite_type == 'npc2' and self.rect.colliderect(sprite.rect) and self.talk:
                    dialog['d']['npc2Run'] = True
                    npc2_dialog(self)
                elif sprite.sprite_type == 'npc3' and self.rect.colliderect(sprite.rect) and self.talk:
                    dialog['d']['npc3Run'] = True
                    npc3_dialog(self)

                            
            

                # Direction detection for collision
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Moving to the right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # Moving to the left
                        self.hitbox.left = sprite.hitbox.right
                    
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.sprite_type == 'enemy' and self.rect.colliderect(sprite.rect):
                    pass
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # Moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # Moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def cooldowns(self):
        current_time = pg.time.get_ticks()

        if self.throwing:
            if current_time - self.snowball_time > self.snowball_cooldown:
                self.throwing = False

    def animate(self):
        if not self.throwing:
            animation = self.animations[self.status]

            
            # Frame index looped over
            self.frame_index += self.animation_speed
            if self.frame_index >= len(animation):
                self.frame_index = 0

            
            # Set image
            self.image = animation[int(self.frame_index)]
            self.rect = self.image.get_rect(center = self.hitbox.center)
        elif self.throwing:
            if self.status == 'up_throw' and self.snowball.direction == pg.math.Vector2(0, -1):
                animation = self.animations['up_throw']

            
                # Frame index looped over
                self.frame_index += self.animation_speed
                if self.frame_index >= len(animation):
                    self.frame_index = 0

                
                # Set image
                self.image = animation[int(self.frame_index)]
                self.rect = self.image.get_rect(center = self.hitbox.center)
            elif self.status == 'left_throw' and self.snowball.direction == pg.math.Vector2(-1, 0):
                animation = self.animations[self.status]

            
                # Frame index looped over
                self.frame_index += self.animation_speed
                if self.frame_index >= len(animation):
                    self.frame_index = 0

                
                # Set image
                self.image = animation[int(self.frame_index)]
                self.rect = self.image.get_rect(center = self.hitbox.center)
            elif self.status == 'right_throw' and self.snowball.direction == pg.math.Vector2(1, 0):
                animation = self.animations[self.status]

            
                # Frame index looped over
                self.frame_index += self.animation_speed
                if self.frame_index >= len(animation):
                    self.frame_index = 0

                
                # Set image
                self.image = animation[int(self.frame_index)]
                self.rect = self.image.get_rect(center = self.hitbox.center)
            elif self.status == 'down_throw' and self.snowball.direction == pg.math.Vector2(0, 1):
                animation = self.animations[self.status]

            
                # Frame index looped over
                self.frame_index += self.animation_speed
                if self.frame_index >= len(animation):
                    self.frame_index = 0

                
                # Set image
                self.image = animation[int(self.frame_index)]
                self.rect = self.image.get_rect(center = self.hitbox.center)


    def launch_snowball(self):
        if not self.throwing and (self.snowball_time is None or pg.time.get_ticks() - self.snowball_time > self.snowball_cooldown):
            self.throwing = True
            self.snowball_time = pg.time.get_ticks()

            prev_direction = self.direction
            prev_speed = self.speed

            # Update the snowball's position without setting it as thrown
            self.snowball.update_position(self.snowman_group)

            self.direction = pg.math.Vector2(0, 0)
            self.speed = 0
            self.status += '_throw'
            self.snowball.rect.center = self.rect.center
            self.snowball.thrown = True

            self.direction = prev_direction
            self.speed = prev_speed

            

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()

        # Move the player based on the input
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        # Update snowball position if thrown, pass snowman group to check for collisions
        if self.snowball.thrown:
            self.snowball.update_position(self.snowman_group)
            self.snowball_thrown = False

