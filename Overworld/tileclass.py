import pygame as pg
from information import *

# This is the class for collidable field objects.
class Tile(pg.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)
		self.image = pg.image.load('wall.png').convert_alpha()
		self.rect = self.image.get_rect(topleft = pos)
		
		# Possible adjustment needed once placeholders not in use
		self.hitbox = self.rect.inflate(0, -10)