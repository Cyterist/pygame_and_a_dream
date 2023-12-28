import pygame as pg
from information import *
from tileclass import Tile, Enemy
from player import Player
from snowball import Snowball
from debug import debug
from support import *


class Level():
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        # Sprite Groups
        self.visible_sprites = YSortedCameraGroup()
        self.obstacle_sprites = pg.sprite.Group()
        self.enemy_group = [] 

        # sprite setup
        self.snowman_group = pg.sprite.Group()
        self.create_map()

        # Offset for camera
        self.offset = pg.math.Vector2() 

        # creating the floor
        self.floor_surf = pg.image.load('../Overworld/data/Level_0/test_map.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    # Map references in maps
    def create_map(self):
        # Key is style, value is layout
        layouts = {
            'boundary': import_csv_layout('../Overworld/maps/Level_0/test_map_floorblocks.csv'),
            'snowman': import_csv_layout('../Overworld/maps/Level_0/test_map_snowman.csv'),
            'object': import_csv_layout('../Overworld/maps/Level_0/test_map_objects.csv'),
            'enemy': import_csv_layout('../Overworld/maps/Level_0/test_map_enemy.csv'),
            'npc': import_csv_layout('../Overworld/maps/Level_0/test_map_npc.csv')
        }
        graphics = {
            'snowman': pg.image.load('../Overworld/data/Level_0/snowman.png').convert_alpha(),
            'objects': import_cut_graphics('../Overworld/data/Level_0/fence_tiles64.png'),
            'enemy': import_cut_graphics('../Overworld/data/Level_0/enemy.png'),
            'npc': import_cut_graphics('../Overworld/data/Level_0/player.png')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * tile_size
                        y = row_index * tile_size
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'object':
                            # create object tile
                            surf = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'objects', surf)
                        if style == 'snowman':
                            # Add snowman sprites to both snowman_group and obstacle_sprites
                            snowman_tile = graphics['snowman']
                            Tile((x, y), [self.visible_sprites, self.snowman_group, self.obstacle_sprites], 'snowman', snowman_tile)
                        if style == 'enemy':
                            enemy_tile = graphics['enemy'][int(col)]
                            enemy = Enemy((x, y), [self.visible_sprites, self.obstacle_sprites], enemy_tile)
                            self.enemy_group.append(enemy)
                        if style == 'npc':
                            npc_tile = graphics['npc'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.snowman_group, self.obstacle_sprites], 'npc', npc_tile)
                            
        

        # Initialize snowball and player sprites
        self.snowball = Snowball((-1000, -1000), [self.visible_sprites], self.obstacle_sprites)
        self.player = Player((400, 600), [self.visible_sprites], self.obstacle_sprites, self.snowman_group, self)
        self.player.snowball = self.snowball

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        screen.blit(self.display_surface, (self.player.rect.x, self.player.rect.y))
        self.visible_sprites.update()
        self.player.move(self.player.speed)  # Call move method to handle player movement and collisions

        # Draw the background color and Floor
        screen.blit(background, (0, 0))
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        # Sort sprites based on y-coordinate
        sprites = sorted(self.visible_sprites.sprites(), key=lambda sprite: sprite.rect.centery)

        # Draw sprites below and at player's level
        for sprite in sprites:
            if sprite.rect.centery < self.player.rect.centery:
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)

        # Draw the snowball
        snowball_offset_pos = self.player.snowball.rect.topleft - self.offset
        self.display_surface.blit(self.player.snowball.image, snowball_offset_pos)

        # Update snowball position if thrown
        if self.player.snowball.thrown:
            self.player.snowball.update_position(self.obstacle_sprites)

        # Draw sprites above player's level
        for sprite in sprites:
            if sprite.rect.centery >= self.player.rect.centery:
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)
        
        # Update enemy positons
        for enemy in self.enemy_group:
            enemy.target = pg.math.Vector2(self.player.rect.center)
            enemy.update()
            offset_pos = enemy.rect.topleft - self.offset
            self.display_surface.blit(enemy.image, offset_pos)


        # Move the player based on the input
        self.player.move(self.player.speed)
        self.offset.x = self.player.rect.centerx - self.display_surface.get_size()[0] // 2 
        self.offset.y = self.player.rect.centery - self.display_surface.get_size()[1] // 2
        debug(self.player.status)


class YSortedCameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

        # Middle of screen offset
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2()

        # Create the floor surface outside of the update method
        self.floor_surf = pg.image.load('../Overworld/data/Level_0/test_map.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # Draw floor only once, outside the loop
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        sprites = sorted(self.sprites(), key=lambda sprite: sprite.rect.centery)

        for sprite in sprites:
            if sprite.rect.centery < player.rect.centery:
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)

        # Assuming player has a snowball attribute
        snowball_offset_pos = player.snowball.rect.topleft - self.offset
        self.display_surface.blit(player.snowball.image, snowball_offset_pos)

        for sprite in sprites:
            if sprite.rect.centery >= player.rect.centery:
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)
                    