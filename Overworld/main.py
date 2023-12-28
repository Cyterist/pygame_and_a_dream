import pygame as pg
from pygame.locals import *
from information import *
from debug import debug
from level import Level


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()

        self.level = Level()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    terminate()
            
            self.level.run()

            pg.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
