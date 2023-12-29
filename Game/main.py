import pygame as pg
from pygame.locals import *
from information import *
from debug import *
from level import Level
from combat import *


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        # self.combat = Combat()
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
            textbox_talk('Press the enter button to start', x = 340, y = 300)
            
            if self.actions['start']:
                self.level.run()
            if self.actions['combat']:
                self.combat.run(screen, [creeper, creeper2], 3, [creeper_hp, creeper2_hp])
                if self.combat.combat == False:
                    self.actions['combat'] = False
                if self.combat.loss == True and self.combat.combat == False:
                    self.actions['start'] == False

            pg.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
