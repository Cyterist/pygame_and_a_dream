import pygame as pg
from pygame.locals import *
from information import *
from debug import *
from level import Level
from combat import *
from fights import *



class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.clock = pg.time.Clock()
        self.level = Level()
        self.combat = Combat()
        self.actions = {'start' : False, 'end': False, 'combat': False, 'controls': False, 'END': False}

        # Music
        self.menu_music = "../Main/data/music/Orphanages_theme.wav"
        self.overworld_music = "../Main/data/music/Belle_town.wav"
        self.combat_music = "../Main/data/music/Raid_boss_battle.wav"
        self.volume = 0
        self.mute = False
        self.running = False

        pg.mixer.music.load(self.menu_music)
        pg.mixer.music.set_volume(0.2)
        pg.mixer.music.play(-1)
    
    def terminate(self):
        fights['RUN'] = False
        self.combat.ends_combat()
        pg.quit()
        sys.exit()

    def play_menu_music(self):
        if not self.mute:
            self.volume = 0.25
            pg.mixer.music.set_volume(self.volume)
            pg.mixer.music.stop()
            pg.mixer.music.load(self.menu_music)
            pg.mixer.music.play(-1)  # -1 means loop indefinitely
            print(pg.mixer.music.get_busy())

    def play_game_music(self):
        if not self.mute:
            pg.mixer.music.stop()
            self.volume = 0.2
            pg.mixer.music.set_volume(self.volume)
            pg.mixer.music.load(self.overworld_music)
            pg.mixer.music.play(-1)  # -1 means loop indefinitely

    def play_fight_music(self):
        if not self.mute:
            self.volume = 0.075
            pg.mixer.music.set_volume(self.volume)
            pg.mixer.music.load(self.combat_music)
            pg.mixer.music.play(-1)

    def stop_music(self):
        if not self.mute:
            pg.mixer.music.stop()


    def run(self):
        self.running = True
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.terminate()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.terminate()
                    if event.key == pg.K_RETURN:
                        self.stop_music()
                        self.play_game_music()      
                        self.actions['start'] = True
                    if event.key == pg.K_c:
                        if self.actions['controls']:
                            self.actions['controls'] = False
                        elif self.actions['controls'] == False:
                            self.actions['controls'] = True
                    if event.key == pg.K_m:
                        if self.mute:
                            self.mute = False
                            pg.mixer.music.set_volume(0.2)
                        else:
                            self.mute = True
                            pg.mixer.music.set_volume(0)
                    if event.key == pg.K_h:
                        fights['wolf1']['fight_begun'] = True  

            screen.blit(background, (0, 0))
            
            textbox_talk('Snowball Chronicles', color = 'Black', bg_color = 'White', text_size = 140, x = 170, y = 60)
            textbox_talk('Press C for controls', color = 'Black', bg_color = 'White', text_size = 100, x = 275, y = 330)
            textbox_talk('Press the enter button to start', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 530)
            
            if fights['END']:
                self.actions['END'] = True

            if self.actions['start'] and not self.actions['controls']:
                
                self.level.run()
            
            # if not fights['creeper1']['fight_begun'] and not fights['creeper2']['fight_begun'] and not fights['wolf1']['fight_begun']:
            #     self.play_game_music()
            if fights['RUN']:
                if fights['creeper1']['fight_begun'] and not self.combat.running:
                    self.play_fight_music()
                    self.combat.run(screen, fights['creeper1']['enemies'], fights['creeper1']['total_chars'], fights['creeper1']['health_bars'])
                    self.stop_music()
                    self.play_game_music()
                if fights['creeper2']['fight_begun'] and not self.combat.running:
                    self.play_fight_music()
                    self.combat.run(screen, fights['creeper2']['enemies'], fights['creeper2']['total_chars'], fights['creeper2']['health_bars'])
                    self.stop_music()
                    self.play_game_music()
                if fights['wolf1']['fight_begun'] and not self.combat.running:
                    self.play_fight_music()
                    self.combat.run(screen, fights['wolf1']['enemies'], fights['wolf1']['total_chars'], fights['wolf1']['health_bars'])
                    self.stop_music()
                    self.play_game_music()
            if self.actions['controls']:
                            screen.blit(background, (0, 0))
                            textbox_talk('Controls:', color = 'Black', bg_color = 'White', text_size = 140, x = 60, y = 10)
                            textbox_talk('WASD: Movement', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 140)
                            textbox_talk('Arrow Keys: Throw Snowball', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 240)
                            textbox_talk('SPACE: Interact/Talk/Attack', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 340)
                            textbox_talk('LMB: Select Enemy', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 440)
                            textbox_talk('M: Mute', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 540)
                            textbox_talk('Press C to return', color = 'Black', bg_color = 'White', text_size = 100, x = 360, y = 610)
            if self.actions['END']:
                screen.blit(background, (0, 0))
                textbox_talk('Thank you for playing!', color = 'Black', bg_color = 'White', text_size = 140, x = 60, y = 10)
                textbox_talk('Made by team Pygame and a Dream for', color = 'Black', bg_color = 'White', text_size = 85, x = 20, y = 520)
                textbox_talk('the 2023 Winter GDEX Game Jam', color = 'Black', bg_color = 'White', text_size = 85, x = 20, y = 610)
            pg.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
