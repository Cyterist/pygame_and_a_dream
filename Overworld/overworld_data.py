import pygame as pg, sys, os

# Window Size is 720p
WINDOWWIDTH = 1280
WINDOWHEIGHT = 720
BACKGROUNDCOLOR = (45, 187, 51) # Green
FPS = 60

# End program
def terminate():
    running = False
    pg.quit()
    sys.exit()

