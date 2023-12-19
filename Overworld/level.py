import pygame as pg
from information import *
from tileclass import Tile
from player import Player
from debug import debug


class Level():
    def __init__(self):

        # get the display surface
        self.display_surface = pg.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortedCameraGroup()
        self.obstacle_sprites = pg.sprite.Group()

        # sprite setup
        self.create_map()

    # Map reference on information.py - TODO import Tiled editor for bigger/easier stages
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = Player(
                        (x, y), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class YSortedCameraGroup(pg.sprite.Group):
    def __init__(self):

        # Setup
        super().__init__()
        self.display_surface = pg.display.get_surface()

        # Middle of screen offset
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2()

    def custom_draw(self, player):

        # Offset for camera
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Y-sorted collision layering, high y value overlaps
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
