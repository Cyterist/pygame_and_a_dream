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
        self.clock = pg.time.Clock()
        self.level = Level()
        self.combat = Combat()
        self.actions = {'start' : False, 'end': False, 'combat': False, 'controls': False}

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    terminate()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.actions['start'] = True
                    if event.key == pg.K_c:
                        if self.actions['controls']:
                            self.actions['controls'] = False
                        elif self.actions['controls'] == False:
                            self.actions['controls'] = True

            screen.blit(background, (0, 0))
            textbox_talk('Snowball Chronicles', color = 'Black', bg_color = 'White', text_size = 140, x = 170, y = 60)
            textbox_talk('Press C for controls.', color = 'Black', bg_color = 'White', text_size = 100, x = 275, y = 330)
            textbox_talk('Press the enter button to start.', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 530)
            
            if self.actions['controls'] and not self.actions['start']:
                screen.blit(background, (0, 0))
                textbox_talk('Controls:', color = 'Black', bg_color = 'White', text_size = 140, x = 60, y = 10)
                textbox_talk('WASD: Movement', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 160)
                textbox_talk('Arrow Keys: Throw Snowball', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 260)
                textbox_talk('SPACE: Interact/Talk/Attack', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 360)
                textbox_talk('LMB: Select Enemy', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 460)
                textbox_talk('Press C to return to Start Menu', color = 'Black', bg_color = 'White', text_size = 100, x = 60, y = 610)

            if self.actions['start']:
                self.level.run()
            
            if fights['creeper1']['fight_begun']:
                self.combat.run(fights['creeper1']['screen'], fights['creeper1']['enemies'], fights['creeper1']['total_chars'], fights['creeper1']['health_bars'])
            if fights['creeper2']['fight_begun'] and not self.combat.running:
                self.combat.run(fights['creeper2']['screen'], fights['creeper2']['enemies'], fights['creeper2']['total_chars'], fights['creeper2']['health_bars'])

            pg.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
