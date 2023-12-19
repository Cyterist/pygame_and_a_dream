import pygame as pg
import sys
import os
from pygame.locals import *
from information import *
from debug import debug
from level import Level

path = r'..\Overworld\data'
os.chdir(path)


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

            # Do logical updates here.
            # ...

            # Render the graphics here.
            # ...

            screen.blit(background, (0, 0))
            self.level.run()

            pg.display.flip()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
