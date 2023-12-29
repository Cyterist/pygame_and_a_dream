from combat import *
from Character import *
from info import *

# creeper = Enemy(850, 390, 'creeper', 30, 30, 1)

fight1 = [creeper]
fight1_health = [creeper_hp]

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()

        self.combat = Combat()


    def run(self):
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    
            self.combat.run(self.screen, fight1, 2, fight1_health)

            pg.display.flip()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()