from UI_Button import *
from Character import *
from enum import Enum

active_char = 1
total_char = 2
cooldown = 0
wait = 100

# Define colors
BLUE = (0,0,255)
BROWN = (105, 77, 49)
WHITE = (255, 255, 255)


# Define screen information
BOTTOM_PANEL = 150
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BATTLE_BAR = pg.Rect((0,SCREEN_HEIGHT - BOTTOM_PANEL), (SCREEN_WIDTH,BOTTOM_PANEL))
FPS = 60

clock = pg.time.Clock()

#Gamestates
class GameState(Enum):
    DEFAULT = 0
    ATTACK = 1
    FIGHT = 2

#text function v2, cause I can't figure out why the one from UI_button won't work in certain cases

def create_text(text, text_color, font_size, x, y, screen):
    font = pg.font.SysFont("Arial", font_size)
    image = font.render(text, True, text_color)
    screen.blit(image, (x, y))

# Creating screens

def create_default_screen(screen):
    screen.fill(BLUE)
    village = Character(200, 450, 'villager', 30, 10)
    creeper = Character(850, 340, 'creeper', 30, 10)

    village_hp = HealthBar(200, SCREEN_HEIGHT - BOTTOM_PANEL + 50, village.hp, village.max_hp)
    creeper_hp = HealthBar(1000, SCREEN_HEIGHT - BOTTOM_PANEL + 50, creeper.hp, creeper.max_hp)
    pg.draw.rect(screen, BROWN, BATTLE_BAR)
    create_text(f'{village.name} HP: {village.hp}', WHITE, 30, 200, SCREEN_HEIGHT - BOTTOM_PANEL + 10, screen)
    create_text(f'{creeper.name} HP: {creeper.hp}', WHITE, 30, 1000, SCREEN_HEIGHT - BOTTOM_PANEL + 10, screen)
    attack_btn = UIButton(center_position=(650,608), font_size=30, surface_color=BROWN, text_color=WHITE, text="Attack", action=GameState.ATTACK)
    
    while True:
        mouse_up = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        
        attack_btn.draw(screen)
        village.draw(screen)
        creeper.draw(screen)
        village_hp.draw(village.hp, screen)
        creeper_hp.draw(creeper.hp, screen)
        
        pg.display.flip()




# Characters

# village = Character(200, 450, 'villager', 30, 10)
# creeper = Character(850, 340, 'creeper', 30, 10)

# village_hp = HealthBar(200, SCREEN_HEIGHT - BOTTOM_PANEL + 50, village.hp, village.max_hp)
# creeper_hp = HealthBar(1000, SCREEN_HEIGHT - BOTTOM_PANEL + 50, creeper.hp, creeper.max_hp)

# Main game function
def main():
    pg.init()

    
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_state = GameState.DEFAULT
    
    while True:
        
        # global active_char
        # global cooldown
        # global wait
        # global total_char

        clock.tick(FPS)
        
        # if village.alive:
        #     if active_char == 1:
        #         cooldown += 1
        #         if cooldown >= wait:
        #             village.attack(creeper)
        #             active_char += 1
        #             cooldown = 0
        # if active_char == 2:
        #     if creeper.alive:
        #         cooldown += 1
        #         if cooldown >= wait:
        #             creeper.attack(village)
        #             active_char += 1
        #             cooldown = 0
        #     else:
        #         active_char += 1
        # if active_char > total_char:
        #     active_char = 1

        
        # Drawing
        
        if game_state == GameState.DEFAULT:
            game_state = create_default_screen(screen)
        
        if game_state == GameState.ATTACK:
            pass
        

if __name__ == "__main__":
    main()





