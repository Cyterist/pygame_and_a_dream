import pygame as pg, sys, os

# Window Information
pg.display.set_caption('Snowball Chronicles')
WINDOWWIDTH = 1280
WINDOWHEIGHT = 720
screen = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
FPS = 60
TILESIZE = 64


# Convert() to speed rendering time.
background = pg.Surface(screen.get_size())
background = background.convert()
background.fill((35, 187, 51)) # Green



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

# Player Information
PLAYERMOVERATE = 90 # Approx. 14 x 8 grid movement


WORLD_MAP = []