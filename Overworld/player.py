import pygame as pg
from information import *

class Player(pg.sprite.Sprite):

    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pg.image.load('Player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        # Adjust once placeholders are not in use
        self.hitbox = self.rect.inflate(-37, 0)
        
        # Must normalize later
        self.direction = pg.math.Vector2()

        self.speed = 5
        self.obstacle_sprites = obstacle_sprites
    
    # Controls
    def input(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_UP] or keys[pg.K_w]:
            self.direction.y = -1
        elif keys[pg.K_DOWN] or keys[pg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction.x = 1
        elif keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        # Checking if vector has length, then setting it to 1 to keep speed equal in all directions
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center


    # This system will only work with static obstacles.
    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Moving to the right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # Moving to the left
                        self.hitbox.left = sprite.hitbox.right
                    
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # Moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # Moving up
                        self.hitbox.top = sprite.hitbox.bottom


    def update(self):
        # update and draw the game
        self.input()
        self.move(self.speed)
