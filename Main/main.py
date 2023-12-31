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
        self.actions = {'start' : False, 'end': False, 'combat': False}

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    terminate()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.actions['start'] = True
                    if event.key == pg.K_h and self.actions['start']:
                        self.actions['combat'] = True

            screen.blit(background, (0, 0))
            textbox_talk('Snowball Chronicles', text_size = 120, bg_color= 'Blue', x = 190, y = 60)
            textbox_talk('Press the enter button to start.', text_size = 100, x = 120, y = 300)
            
            
            if self.actions['start']:
                self.level.run()
            if self.level.creeper1:
                self.combat.run(fights['creeper1']['screen'], fights['creeper1']['enemies'], fights['creeper1']['total_chars'], fights['creeper1']['health_bars'])
                if self.combat.combat == False:
                    self.level.creeper1 = False
                if self.combat.loss == True and self.combat.combat == False:
                    self.actions['start'] == False

            pg.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
