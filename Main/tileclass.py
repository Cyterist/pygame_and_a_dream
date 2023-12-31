import pygame as pg
from information import *


# This is the class for collidable field objects.
class Tile(pg.sprite.Sprite):
	def __init__(self, pos, groups, sprite_type, surface = pg.Surface((tile_size, tile_size))):
		super().__init__(groups)
		self.sprite_type = sprite_type
		self.image = surface
		# If larger pictures than 64 x 64 are used, this will be used to offset loading.
		if sprite_type == 'object':
			self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - tile_size))
		elif sprite_type == 'enemy':
			self.rect = self.image.get_rect(topleft = (pos[0], pos[1] - tile_size))
		else:
			self.rect = self.image.get_rect(topleft = pos)
		self.hitbox = self.rect.inflate(-20, -40)

class Enemy(Tile):
    def __init__(self, pos, groups, graphics):
        super().__init__(pos, groups, 'enemy', graphics)
        self.speed = 2  # Adjust the speed as needed
        self.target = pg.math.Vector2(pos)  # Set the initial target position to the enemy's starting position

    def update(self):
        # Basic AI: Move towards the target position (player's position)
        direction = self.target - pg.math.Vector2(self.rect.center)
        distance = direction.length()

        # Check if the enemy is close enough to the target position
        if distance <= 300 and distance > 0:
            direction.normalize_ip()
            move_amount = min(distance, self.speed)
            self.rect.x += direction.x * move_amount
            self.rect.y += direction.y * move_amount