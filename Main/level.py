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
        self.visible_sprites = YSortedCameraGroup(game_width=640, game_height=480)
        self.obstacle_sprites = pg.sprite.Group()
        self.enemy_group = [] 

        # sprite setup
        self.snowman_group = pg.sprite.Group()
        self.create_map()
        self.creeper1 = False

        # Offset for camera
        self.offset = pg.math.Vector2() 

        # creating the floor
        self.floor_surf = pg.image.load('../Main/data/Level_32/32test_map.png').convert_alpha()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    # Map references in maps
    def create_map(self):
        # Key is style, value is layout
        # if self.level == 'level0':
        #     layouts = {
        #         'boundary': import_csv_layout('../Main/maps/Level_0/test_map_floorblocks.csv'),
        #         'snowman': import_csv_layout('../Main/maps/Level_0/test_map_snowman.csv'),
        #         'object': import_csv_layout('../Main/maps/Level_0/test_map_objects.csv'),
        #         'enemy': import_csv_layout('../Main/maps/Level_0/test_map_enemy.csv'), 
        #         'npc': import_csv_layout('../Main/maps/Level_0/test_map_npc.csv'),
        #         'npc2': import_csv_layout('../Main/maps/Level_0/test_map_npc2.csv')
        #     }
        #     graphics = {
        #         'snowman': pg.image.load('../Main/data/Level_0/snowman.png').convert_alpha(),
        #         'objects': import_cut_graphics('../Main/data/Level_0/fence_tiles64.png'),
        #         'enemy': import_cut_graphics('../Main/data/Level_0/enemy.png'),
        #         'npc': import_cut_graphics('../Main/data/Level_0/player.png'),
        #         'npc2': pg.image.load('../Main/data/Level_0/alienship64.png').convert()
        #     }
        #     for style, layout in layouts.items():
        #         for row_index, row in enumerate(layout):
        #             for col_index, col in enumerate(row):
        #                 if col != '-1':
        #                     x = col_index * tile_size
        #                     y = row_index * tile_size
        #                     if style == 'boundary':
        #                         Tile((x, y), [self.obstacle_sprites], 'invisible')
        #                     if style == 'object':
        #                         # create object tile
        #                         surf = graphics['objects'][int(col)]
        #                         Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'objects', surf)
        #                     if style == 'snowman':
        #                         # Add snowman sprites to both snowman_group and obstacle_sprites
        #                         snowman_tile = graphics['snowman']
        #                         Tile((x, y), [self.visible_sprites, self.snowman_group, self.obstacle_sprites], 'snowman', snowman_tile)
        #                     if style == 'enemy':
        #                         enemy_tile = graphics['enemy'][int(col)]
        #                         enemy = Enemy((x, y), [self.visible_sprites, self.obstacle_sprites], enemy_tile)
        #                         self.enemy_group.append(enemy)
        #                     if style == 'npc':
        #                         npc_tile = graphics['npc'][int(col)]
        #                         Tile((x, y), [self.visible_sprites, self.snowman_group, self.obstacle_sprites], 'npc', npc_tile)
        #                     if style == 'npc2':
        #                         npc2_tile = graphics['npc2']
        #                         Tile((x, y), [self.visible_sprites, self.snowman_group, self.obstacle_sprites], 'npc2', npc2_tile)

                                    
                                
            

        #     # Initialize snowball and player sprites
        #     self.snowball = Snowball((-1000, -1000), [self.visible_sprites], self.obstacle_sprites)
        #     self.player = Player((400, 600), [self.visible_sprites], self.obstacle_sprites, self.snowman_group, self)
        #     self.player.snowball = self.snowball
        layouts = {
            'boundary': import_csv_layout('../Main/maps/Level_32/_floorblocks.csv'),
            'snowman': import_csv_layout('../Main/maps/Level_32/_desobjects.csv'),
            'object': import_csv_layout('../Main/maps/Level_32/_objects.csv'),
            'large_object': import_csv_layout('../Main/maps/Level_32/_large_objects.csv'),
            'npc1': import_csv_layout('../Main/maps/Level_32/_npc1.csv'), 
            'npc2': import_csv_layout('../Main/maps/Level_32/_npc2.csv'),
            'npc3': import_csv_layout('../Main/maps/Level_32/_npc3.csv'),
            'player': import_csv_layout('../Main/maps/Level_32/_player.csv')
        }
        graphics = {
            'snowman': pg.image.load('../Main/data/Level_32/snowman32.png').convert_alpha(),
            'objects': import_cut_graphics('../Main/data/Level_32/TX_props.png'),
            'large_objects': import_cut_graphics('../Main/data/Level_32/TX_props.png'),
            'npc': import_cut_graphics('../Main/data/Level_32/npc.png')
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
                        if style == 'large_object':
                            large_surf = graphics['large_objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'large_objects', large_surf)
                        if style == 'snowman':
                            # Add snowman sprites to both snowman_group and obstacle_sprites
                            snowman_tile = graphics['snowman']
                            Tile((x, y), [self.visible_sprites, self.snowman_group, self.obstacle_sprites], 'snowman', snowman_tile)
                            # FIXME Unused class with AI to swarm towards player, could be transformed into pickups or?
                        # if style == 'enemy':
                        #     enemy_tile = graphics['enemy'][int(col)]
                        #     enemy = Enemy((x, y), [self.visible_sprites, self.obstacle_sprites], enemy_tile)
                        #     self.enemy_group.append(enemy)
                        if style == 'npc1':
                            npc_tile = graphics['npc'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.snowman_group, self.obstacle_sprites], 'npc', npc_tile)
                        # if style == 'player':
                            

        # Initialize snowball and player sprites
        self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, self.snowman_group, self)
        self.snowball = Snowball((-1000, -1000), [self.visible_sprites], self.obstacle_sprites)
        
        self.player.snowball = self.snowball

    def run(self, screen):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.player.move(self.player.speed)  # Call move method to handle player movement and collisions
        # Clear the screen with the background color
        screen.blit(background, (0, 0))

        # Draw the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        screen.blit(self.floor_surf, floor_offset_pos)

        # Sort sprites based on y-coordinate
        sprites = sorted(self.visible_sprites.sprites(), key=lambda sprite: sprite.rect.centery)

        # Draw sprites below and at player's level
        for sprite in sprites:
            if sprite.rect.centery < self.player.rect.centery:
                offset_pos = sprite.rect.topleft - self.offset
                screen.blit(sprite.image, offset_pos)

        # Draw the snowball
        snowball_offset_pos = self.player.snowball.rect.topleft - self.offset
        screen.blit(self.player.snowball.image, snowball_offset_pos)

        # Update snowball position if thrown
        if self.player.snowball.thrown:
            self.player.snowball.update_position(self.obstacle_sprites)

        if self.player.creeper1:
            self.creeper1 = True

        # Draw sprites above player's level
        for sprite in sprites:
            if sprite.rect.centery >= self.player.rect.centery:
                offset_pos = sprite.rect.topleft - self.offset
                screen.blit(sprite.image, offset_pos)

        # Update enemy positions
        for enemy in self.enemy_group:
            enemy.target = pg.math.Vector2(self.player.rect.center)
            enemy.update()
            offset_pos = enemy.rect.topleft - self.offset
            screen.blit(enemy.image, offset_pos)

        # Move the player based on the input
        self.player.move(self.player.speed)
        self.offset.x = self.player.rect.centerx - screen.get_width() // 2
        self.offset.y = self.player.rect.centery - screen.get_height() // 2

        pg.display.flip()


class YSortedCameraGroup(pg.sprite.Group):
    def __init__(self, game_width, game_height):
        super().__init__()
        self.game_width = game_width
        self.game_height = game_height
        self.display_surface = pg.Surface((self.game_width, self.game_height))
        self.display_surface = self.display_surface.convert()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pg.math.Vector2()

        # Create the floor surface outside of the update method
        self.floor_surf = pg.image.load('../Main/data/Level_32/32test_map.png').convert()
        self.floor_surf_scaled = pg.transform.scale_by(self.floor_surf, 2)
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

        # Scale the entire surface to fit the screen
        scaled_display_surface = pg.transform.scale_by(self.display_surface, 2)
        screen.blit(scaled_display_surface, (0, 0))