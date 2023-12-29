from combat import *
from Character import *
from info import *

clock = pg.time.Clock()

# creeper = Enemy(850, 390, 'creeper', 30, 30, 1)

fight1 = [creeper]
fight1_health = [creeper_hp]

def main():

    pg.init()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        
        clock.tick(FPS)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    combat(screen, fight1, 2, fight1_health)
                    print("pressed")

if __name__ == '__main__':
    main()