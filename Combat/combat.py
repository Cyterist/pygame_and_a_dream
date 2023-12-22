from UI_Button import *
from Character import *
from bars import *

active_char = 1
characters = []
enemies = []
cooldown = 0
wait = 100
attack = False
target = None
white_bar_speed = 0
yellow = False
red = False
green = False

# Define colors
BLUE = (0,0,255)
BROWN = (105, 77, 49)
WHITE = (255, 255, 255)


# Define screen information
BOTTOM_PANEL = 200
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BATTLE_BAR = pg.Rect((0,SCREEN_HEIGHT - BOTTOM_PANEL), (SCREEN_WIDTH,BOTTOM_PANEL))
FPS = 60

clock = pg.time.Clock()

#text function v2, cause I can't figure out why the one from UI_button won't work in certain cases

def create_text(text, text_color, font_size, x, y, screen, bgcolor=None):
    font = pg.font.SysFont("Arial", font_size)
    image = font.render(text, True, text_color, bgcolor)
    screen.blit(image, (x, y))

# Creating screens

def create_default_screen(screen):
    pg.draw.rect(screen, BROWN, BATTLE_BAR)
    create_text(f'{player.name} HP: {player.hp}', WHITE, 30, 200, SCREEN_HEIGHT - BOTTOM_PANEL + 15, screen)
    create_text(f'{player.name} SNOW: {player.snow}', WHITE, 30, 200, SCREEN_HEIGHT - BOTTOM_PANEL + 75, screen)
    for i, enemy in enumerate(enemies):
        create_text(f'{enemy.name} HP: {enemy.hp}', WHITE, 30, 1000, (SCREEN_HEIGHT - BOTTOM_PANEL + 15) + i * 60, screen)

def check_sides(rect):
    if rect.left <= 350:
        return True
    elif rect.right >= 950:
        return True
    else:
        return False



# Characters

player = Character(200, 400, 'player', 30, 30, 5)
creeper = Character(850, 390, 'creeper', 30, 30, 10)
creeper2 = Character(1050, 390, 'creeper', 30, 30, 10)


player_hp = HealthBar(200, SCREEN_HEIGHT - BOTTOM_PANEL + 55, player.hp, player.max_hp)
creeper_hp = HealthBar(1000, SCREEN_HEIGHT - BOTTOM_PANEL + 55, creeper.hp, creeper.max_hp)
creeper2_hp = HealthBar(1000, SCREEN_HEIGHT - BOTTOM_PANEL + 115, creeper2.hp, creeper2.max_hp)
player_snow = SnowMeter(200, SCREEN_HEIGHT - BOTTOM_PANEL + 115, player.snow, player.max_snow)

characters.append(player)
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
        global target
        global white_bar_speed
        global yellow
        global red
        global green

        total_chars = len(characters)

        clock.tick(FPS)
        screen.fill(BLUE)

        mouse_up = False
        mouse_pos = pg.mouse.get_pos()

        keys = pg.key.get_pressed()

        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        
        #Update Buttons
        attack_btn.update(mouse_pos)

        #players turn
        if player.alive:
            if active_char == 1:
                create_text("Your Turn", WHITE, 50, 550, 0, screen)
                if attack_btn.clicked(mouse_pos, mouse_up):
                    attack = True
                if attack == True:
                    create_text("Select Target", WHITE, 50, 550, 0, screen, BLUE)
                    for enemy in enemies:
                        if enemy.rect.collidepoint(mouse_pos) and mouse_up:
                            target = enemy
                            print(target) 
                if attack == True and target != None:
                    for bar in attack_bars:
                        bar.draw(screen)
                    
                    if white_bar_speed == 0:
                        white_bar_speed = 3
                    
                    white_bar.x += white_bar_speed
                    pg.draw.rect(screen, WHITE, white_bar)
                    side = check_sides(white_bar)
                    if side:
                        white_bar_speed *= -1
                    if keys[pg.K_SPACE]:
                        if attack_y1.check_collision(white_bar) or attack_y2.check_collision(white_bar):
                            yellow = True
                        if attack_r1.check_collision(white_bar) or attack_r2.check_collision(white_bar):
                            red = True
                        if attack_g.check_collision(white_bar):
                            green = True
                    
                    if red == True:
                        player.attack(target, 0)
                        red = False
                        target = None
                        white_bar.x = 350
                        attack = False
                        active_char += 1
                    if yellow == True:
                        player.attack(target, 3)
                        yellow = False
                        target = None
                        white_bar.x = 350
                        attack = False
                        active_char += 1
                    if green == True:
                        player.attack(target, 10)
                        green = False
                        target = None
                        white_bar.x = 350
                        attack = False
                        active_char += 1
        
        #Enemy Turn  
        for enemy in enemies:
            if active_char > 1 and active_char <= total_chars:
                if enemy.alive:
                    create_text("Enemy Turn", WHITE, 50, 550, 0, screen)
                    cooldown +=1
                    if cooldown >= wait:
                        enemy.attack(player, 0)
                        active_char += 1
                        cooldown = 0

        if active_char > total_chars:
            active_char = 1


    
        
        # Drawing
        
        player.draw(screen)
        
        for enemy in enemies:
            enemy.draw(screen)
        
        create_default_screen(screen)
        attack_btn.draw(screen)
        
        player_hp.draw(player.hp, screen)
        player_snow.draw(player.snow, screen)
        creeper_hp.draw(creeper.hp, screen)
        creeper2_hp.draw(creeper2.hp, screen)
        
        pg.display.flip()
        

if __name__ == "__main__":
    main()





