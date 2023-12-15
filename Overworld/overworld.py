import pygame as pg, sys, os
from pygame.locals import *
from overworld_data import *

pg.init()
screen = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
clock = pg.time.Clock()

PLAYERMOVERATE = 90 # Approx. 14 x 8 grid movement

running = True

while running:
    # Process player inputs.
    for event in pg.event.get():
        if event.type == QUIT:
            terminate()
        
        
    # Do logical updates here.
    # ...
                
    screen.fill(BACKGROUNDCOLOR)
    
    # Render the graphics here.
    # ...

    pg.display.flip()
    clock.tick(FPS)