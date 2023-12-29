import pygame as pg
from information import *

class Snowball(pg.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pg.image.load('../Main/data/Snowball/snowball.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.obstacle_sprites = obstacle_sprites

        self.direction = pg.math.Vector2()
        self.speed = 7.1
        self.thrown = False
        self.distance_traveled = 0
        self.max_distance = 640  # Adjust as needed
        self.initial_pos = pos

    def launch_snowball(self):
        if not self.throwing and (self.snowball_time is None or pg.time.get_ticks() - self.snowball_time > self.snowball_cooldown):
            prev_direction = self.direction
            prev_speed = self.speed

            # Set the initial position of the snowball
            self.rect.center = self.rect.center

            # Update the snowball's position without setting it as thrown
            self.update_position(self.snowman_group)

            # Stop the player briefly while throwing
            self.direction = pg.math.Vector2(0, 0)
            self.speed = 0
            self.status += '_throw'
            self.thrown = True
            self.snowball_time = pg.time.get_ticks()  # Set the time when the snowball was thrown

            pg.time.delay(200)
            self.direction = prev_direction
            self.speed = prev_speed


    def update_position(self, obstacle_sprites):
        if self.thrown:
            self.rect.x += self.direction.x * self.speed
            self.rect.y += self.direction.y * self.speed
            self.distance_traveled += self.speed

            # Check for collisions with snowman sprites
            collisions = pg.sprite.spritecollide(self, obstacle_sprites, False)
            for sprite in collisions:
                self.handle_collision(sprite)
                self.reset_snowball()
                break

            if self.distance_traveled >= self.max_distance:
                self.reset_snowball()
        else:
            self.rect.center = self.initial_pos

    def reset_snowball(self):
        self.thrown = False
        self.distance_traveled = 0
        self.rect.center = self.initial_pos

    def handle_collision(self, collidable_obj):
        for sprite in self.obstacle_sprites:
            if sprite.sprite_type == 'snowman' and self.rect.colliderect(sprite.rect):
                print(sprite.sprite_type)
                collidable_obj.kill()  # Destroy the 'snowman' object
                self.thrown = False
                self.rect.center = self.initial_pos
                self.distance_traveled = 0
                self.obstacle_sprites.remove(sprite)
                break
            elif sprite.sprite_type == 'objects' and self.rect.colliderect(sprite.rect):
                print(sprite.sprite_type)
                self.thrown = False
                self.distance_traveled = 0
                self.rect.center = self.initial_pos
                break
            elif sprite.sprite_type == 'enemy' and self.rect.colliderect(sprite.rect):
                print(sprite.sprite_type)
                print('Enemy hit with snowball, begin combat')