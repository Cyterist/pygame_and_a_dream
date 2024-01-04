import pygame as pg
import sys
import os

# Window Information
pg.display.set_caption('Snowball Chronicles')
WINDOWWIDTH = 1280
WINDOWHEIGHT = 720
screen = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
FPS = 60
tile_size = 64
BOTTOM_PANEL = 200


BLUE = (0, 0, 255)
BROWN = (105, 77, 49)
WHITE = (255, 255, 255)
RED = (255, 0 ,0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


# Convert() to speed rendering time.
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((255, 255, 255))  # White


# End program
def terminate():
    pg.quit()
    sys.exit()

# Load image and return image object
def load_png(name):
    '''All icons are currently placeholders gained for free from craftpix.net'''
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    fullname = os.path.join("data", name)
    try:
        image = pg.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except FileNotFoundError:
        print(f"Cannot load image: {fullname}")
        raise SystemExit
    return image, image.get_rect()

