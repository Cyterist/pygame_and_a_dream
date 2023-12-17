from UI_Button import *
from Character import *
from enum import Enum

active_char = 1
characters = []
enemies = []
cooldown = 0
wait = 100
attack = False
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

def create_text(text, text_color, font_size, x, y, screen, bgcolor=None):
    font = pg.font.SysFont("Arial", font_size)
    image = font.render(text, True, text_color, bgcolor)
    screen.blit(image, (x, y))

# Creating screens

def create_default_screen(screen):
    pg.draw.rect(screen, BROWN, BATTLE_BAR)
    create_text(f'{village.name} HP: {village.hp}', WHITE, 30, 200, SCREEN_HEIGHT - BOTTOM_PANEL + 10, screen)
    create_text(f'{creeper.name} HP: {creeper.hp}', WHITE, 30, 1000, SCREEN_HEIGHT - BOTTOM_PANEL + 10, screen)
    create_text(f'{creeper2.name} HP: {creeper2.hp}', WHITE, 30, 1000, SCREEN_HEIGHT - BOTTOM_PANEL + 65, screen)




# Characters

village = Character(200, 450, 'villager', 30, 5)
creeper = Character(850, 340, 'creeper', 30, 10)
creeper2 = Character(1050, 340, 'creeper', 30, 10)


village_hp = HealthBar(200, SCREEN_HEIGHT - BOTTOM_PANEL + 50, village.hp, village.max_hp)
creeper_hp = HealthBar(1000, SCREEN_HEIGHT - BOTTOM_PANEL + 50, creeper.hp, creeper.max_hp)
creeper2_hp = HealthBar(1000, SCREEN_HEIGHT - BOTTOM_PANEL + 100, creeper2.hp, creeper2.max_hp)

characters.append(village)
characters.append(creeper)
characters.append(creeper2)
enemies.append(creeper)
enemies.append(creeper2)
# Main game function
def main():
    pg.init()

    
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    attack_btn = UIButton(center_position=(650,608), font_size=30, surface_color=BROWN, text_color=WHITE, text="Attack")
    
    while True:
        
        global active_char
        global cooldown
        global wait
        global characters
        global attack
        global enemies

        total_chars = len(characters)

        clock.tick(FPS)
        screen.fill(BLUE)

        mouse_up = False
        mouse_pos = pg.mouse.get_pos()
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        
        #Update Buttons
        attack_btn.update(mouse_pos)

        #players turn
        if village.alive:
            if active_char == 1:
                create_text("Your Turn", WHITE, 50, 550, 0, screen)
                if attack_btn.clicked(mouse_pos, mouse_up):
                    attack = True
                if attack == True:
                    create_text("Select Target", WHITE, 50, 550, 0, screen, BLUE)
                    # if creeper.rect.collidepoint(mouse_pos) and mouse_up:
                    #     village.attack(creeper)
                    #     active_char += 1
                    #     attack = False
                    for enemy in enemies:
                        if enemy.rect.collidepoint(mouse_pos) and mouse_up:
                            village.attack(enemy)
                            active_char += 1
                            attack = False
        
        #Enemy Turn  
        for enemy in enemies:
            if active_char > 1 and active_char <= total_chars:
                if enemy.alive:
                    create_text("Enemy Turn", WHITE, 50, 550, 0, screen)
                    cooldown +=1
                    if cooldown >= wait:
                        enemy.attack(village)
                        active_char += 1
                        cooldown = 0

        if active_char > total_chars:
            active_char = 1


    
        
        # Drawing
        create_default_screen(screen)
        attack_btn.draw(screen)
        village.draw(screen)
        creeper.draw(screen)
        creeper2.draw(screen)
        village_hp.draw(village.hp, screen)
        creeper_hp.draw(creeper.hp, screen)
        creeper2_hp.draw(creeper2.hp, screen)
        pg.display.flip()
        

if __name__ == "__main__":
    main()





