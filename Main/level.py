import pygame as pg
from information import *
from tileclass import Tile, Enemy
from player import Player
from snowball import Snowball
from debug import *
from support import *
from combat import Combat


class Level():
    def __init__(self):
        self.display_surface = pg.display.get_surface()
        # Sprite Groups
        self.visible_sprites = YSortedCameraGroup()
        self.obstacle_sprites = pg.sprite.Group()
        self.enemy_group = []
        self.map = 'main'
        self.combat = Combat()

        # sprite setup
        self.snowman_group = pg.sprite.Group()
        self.create_map()
        self.creeper1 = False
        self.creeper2 = False

        # Offset for camera
        self.offset = pg.math.Vector2() 

        # creating the floor
        self.floor_surf = pg.image.load('../Main/data/Level_1/map.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    # Map references in maps
    def create_map(self):
        # Key is style, value is layout
        if self.map == 'test':
            layouts = {
                'boundary': import_csv_layout('../Main/maps/Level_0/test_map_floorblocks.csv'),
                'snowman': import_csv_layout('../Main/maps/Level_0/test_map_snowman.csv'),
                'object': import_csv_layout('../Main/maps/Level_0/test_map_objects.csv'),
                'enemy': import_csv_layout('../Main/maps/Level_0/test_map_enemy.csv'),
                'npc': import_csv_layout('../Main/maps/Level_0/test_map_npc.csv'),
                'npc2': import_csv_layout('../Main/maps/Level_0/test_map_npc2.csv')
            }
            graphics = {
                'snowman': pg.image.load('../Main/data/Level_0/snowman.png').convert_alpha(),
                'objects': import_cut_graphics('../Main/data/Level_0/fence_tiles64.png'),
                'enemy': import_cut_graphics('../Main/data/Level_0/enemy.png'),
                'npc': import_cut_graphics('../Main/data/Level_0/player.png'),
                'npc2': pg.image.load('../Main/data/Level_0/alienship64.png').convert()
            }
        elif self.map == 'main':
            # Locations of tiles
            layouts = {
                'boundary': import_csv_layout('../Main/maps/Level_1/_level_1_floorblocks.csv'),
                'decorations': import_csv_layout('../Main/maps/Level_1/_level_1_decorations.csv'),
                'snowman': import_csv_layout('../Main/maps/Level_1/_level_1_desobjects.csv'),
                'object': import_csv_layout('../Main/maps/Level_1/_level_1_objects.csv'),
                # 'enemy': import_csv_layout('../Main/maps/Level_1/_level_1_enemy.csv'),
                'npc': import_csv_layout('../Main/maps/Level_1/_level_1_npc.csv'),
                'npc2': import_csv_layout('../Main/maps/Level_1/_level_1_npc2.csv')
            }
            # Tile graphics
            graphics = {
                'snowman': import_folder('../Main/data/Level_1/snowmen/'),
                'decorations': import_folder('../Main/data/Level_1/decorations/'),
                'objects': pg.image.load('../Main/data/Level_1/objects/bench64.png'),
                # 'enemy': import_cut_graphics('../Main/data/Level_0/enemy.png'),
                'npc': pg.image.load('../Main/data/Level_1/sign-post64.png').convert_alpha(),
                'npc2': pg.image.load('../Main/data/Level_1/Player.png').convert()
            }
        
        # Draw map and render Tiles
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * tile_size
                        y = row_index * tile_size
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'decorations':
                            # Would have to redesign import_folder() to make this work, so the -3 is a placeholder to set it to count the graphics from 0
                            decorations = graphics['decorations'][int(col) - 3]
                            if int(col) - 3 == 1:
                                Tile((x, y - 192), [self.visible_sprites], 'large_decorations', decorations)
                            if int(col) - 3 == 0:
                                Tile((x, y - 64), [self.visible_sprites], 'small_decorations', decorations)
                        if style == 'object':
                            # create object tile
                            surf = graphics['objects']
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'objects', surf)
                        if style == 'snowman':
                            # Add snowman sprites to both snowman_group and obstacle_sprites
                            snowman_tile = graphics['snowman'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.snowman_group, self.obstacle_sprites], 'snowman', snowman_tile)
                        # if style == 'enemy':
                        #     enemy_tile = graphics['enemy'][int(col)]
                        #     enemy = Enemy((x, y), [self.visible_sprites, self.obstacle_sprites], enemy_tile)
                        #     self.enemy_group.append(enemy)
                        if style == 'npc':
                            npc_tile = graphics['npc']
                            Tile((x, y), [self.visible_sprites, self.snowman_group, self.obstacle_sprites], 'npc', npc_tile)
                        if style == 'npc2':
                            npc2_tile = graphics['npc2']
                            Tile((x, y), [self.visible_sprites, self.snowman_group, self.obstacle_sprites], 'npc2', npc2_tile)
        

        # Initialize snowball and player sprites
        self.player = Player((5504, 4096), [self.visible_sprites], self.obstacle_sprites, self.snowman_group, self)
        self.snowball = Snowball((-1000, -1000), [self.visible_sprites], self.obstacle_sprites)

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
        
        self.creeper1 = self.player.creeper1 if not self.combat.running else False
        self.creeper2 = self.player.creeper2 if not self.combat.running else False

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


class YSortedCameraGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pg.display.get_surface()

        # Middle of screen offset
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pg.math.Vector2()

        # Create the floor surface outside of the update method
        self.floor_surf = pg.image.load('../Main/data/Level_1/map.png').convert()
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
                    