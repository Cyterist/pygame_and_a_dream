import pygame as pg
from information import *
from support import import_folder
from snowball import *
from debug import debug, textbox_talk

class Player(pg.sprite.Sprite):

    def __init__(self, pos, groups, obstacle_sprites, snowman_group, level):
        super().__init__(groups)
        self.snowman_group = snowman_group

        self.image = pg.image.load('../Overworld/data/32-bit_placeholders/Player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        # Adjust once placeholders are not in use
        self.hitbox = self.rect.inflate(-37, 0)
        
        # Graphics
        self.import_player_assets()
        self.status = 'down'
        self.frame_index = 0
        # Change later for sprite animation
        self.animation_speed = 0.15

        # Must normalize later
        self.direction = pg.math.Vector2()

        self.speed = 5
        self.throwing = False
        self.snowball_cooldown = 721
        self.snowball_time = None
        self.obstacle_sprites = obstacle_sprites
        self.vel = pg.math.Vector2(0, 0)
        self.throwing = False
        self.talk = False


    # main character sprites and animation
    def import_player_assets(self):
        character_path = '../Overworld/data/player/'
        # TODO Get animation states, and import into self.animations
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                           'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
                           'right_throw': [], 'left_throw': [], 'up_throw': [], 'down_throw': []
                           }
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)


    def input(self):
        keys = pg.key.get_pressed()

        # Reset the direction vector
        self.direction = pg.math.Vector2(0, 0)

        # Check each key separately to set the corresponding direction
        if keys[pg.K_w]:
            self.direction.y = -1
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
            self.talk = True
        elif keys[pg.K_ESCAPE]:
            self.talk = False

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
                if sprite.sprite_type == 'enemy' and self.rect.colliderect(sprite.rect):
                    pass
                if sprite.sprite_type == 'npc' and self.rect.colliderect(sprite.rect) and self.talk:
                    textbox_talk('This is a textbox')

                    
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Moving to the right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # Moving to the left
                        self.hitbox.left = sprite.hitbox.right
                    
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.sprite_type == 'enemy' and self.rect.colliderect(sprite.rect):
                    print('touched an enemy, begin combat')
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
            
            # Set the initial position of the snowball
            

            # Update the snowball's position without setting it as thrown
            self.snowball.update_position(self.snowman_group)

            self.direction = pg.math.Vector2(0, 0)
            self.speed = 0
            # self.status += '_throw'
            self.snowball.rect.center = self.rect.center
            self.snowball.thrown = True

            self.direction = prev_direction
            self.speed = prev_speed

            

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()

        # Move the player based on the input
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

        # Update snowball position if thrown, pass snowman group to check for collisions
        if self.snowball.thrown:
            self.snowball.update_position(self.snowman_group)  # Pass snowman group
            self.snowball_thrown = False
