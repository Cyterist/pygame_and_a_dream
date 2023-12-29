import pygame as pg, sys, os
from pygame.locals import *
from information import *
from debug import debug


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    terminate()
                if event.type == KEYDOWN:
                    if event.key == [K_s] or [K_DOWN]:
                        moveDown = True    
            
            # Do logical updates here.
            # ...
        
            # Render the graphics here.
            # ...
            
            screen.blit(background, (0, 0))
            screen.blit((load_png('Frame_01.png')[0]), (0, 0))
            pg.display.flip()
            self.clock.tick(FPS)
if __name__ == '__main__':
    game = Game()
    game.run()