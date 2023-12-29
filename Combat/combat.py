from UI_Button import *
from Character import *
from bars import *
from info import *

active_char = 1
cooldown = 0
wait = 100
attack = False
ability_1 = False
target = None
white_bar_speed = 0
yellow = False
red = False
green = False



background = pg.image.load('pics/assets/background.png')
scaled_bg = pg.transform.scale(background, (background.get_width() * 4, background.get_height() * 4))
panel = pg.image.load('pics/assets/panel.png')
scaled_panel = pg.transform.scale(panel, (panel.get_width() * 3.25, panel.get_height() * 2.3))

#text function v2, cause I can't figure out why the one from UI_button won't work in certain cases

def create_text(text, text_color, font_size, x, y, screen, bgcolor=None):
    font = pg.font.SysFont("Arial", font_size)
    image = font.render(text, True, text_color, bgcolor)
    screen.blit(image, (x, y))


# Creating screen
def create_default_screen(screen, enemies):
    
    screen.blit(scaled_bg,(0,0))
    screen.blit(scaled_panel, (-90, SCREEN_HEIGHT-BOTTOM_PANEL-85))
    
    
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



# Main game function
def combat(screen, enemies, total_chars, health_bars):
    # pg.init()

    
    # screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    attack_btn = UIButton(center_position=(650,608), font_size=30, text_color=WHITE, text="Attack")
    ability1_btn = UIButton(center_position=(650,658), font_size=30, text_color=WHITE, text="Ability 1")
    collect_btn = UIButton(center_position=(650,558), font_size=30, text_color=WHITE, text="Collect Snow")

    
    while True:
        
        # global variables
        global active_char
        global cooldown
        global wait
        global attack
        global target
        global white_bar_speed
        global yellow
        global red
        global green
        global ability_1
        
        create_default_screen(screen, enemies)

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
        # ability1_btn.update(mouse_pos)
        collect_btn.update(mouse_pos)

        if player.snow >= 10:
            ability1_btn.update(mouse_pos)

        #players turn
        if player.alive:
            if active_char == 1:
                
                #Check if action was selection
                if not attack and not ability_1: 
                    
                    create_text("Your Turn", WHITE, 50, 550, 0, screen)
                    
                    if attack_btn.clicked(mouse_pos, mouse_up):
                        attack = True
                        print("attack")
                
                    if ability1_btn.clicked(mouse_pos, mouse_up) and player.snow >= 10:
                        ability_1 = True
                        print("ability")
                    
                    if collect_btn.clicked(mouse_pos, mouse_up):
                        player.collect_snow()
                        active_char += 1

                if attack or ability_1:
                    create_text("Select Target", WHITE, 50, 550, 0, screen)
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
                
                if ability_1 == True and target != None:
                    for bar in hard_bars:
                        bar.draw(screen)
                    
                    if white_bar_speed == 0:
                        white_bar_speed = 4
                    
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
                        player.harder_hitting_ability(target, 0)
                        red = False
                        target = None
                        white_bar.x = 350
                        ability_1 = False
                        active_char += 1
                    elif yellow == True:
                        player.harder_hitting_ability(target, 3)
                        yellow = False
                        target = None
                        white_bar.x = 350
                        ability_1 = False
                        active_char += 1
                    elif green == True:
                        player.harder_hitting_ability(target, 10)
                        green = False
                        target = None
                        white_bar.x = 350
                        ability_1 = False
                        active_char += 1

        #Enemy Turn  
        for i, enemy in enumerate(enemies):
            if active_char == 2 + i:
                if enemy.alive == True:
                    create_text("Enemy Turn", WHITE, 50, 550, 0, screen)
                    cooldown +=1
                    if cooldown >= wait:
                        enemy.attack(player)
                        active_char += 1
                        cooldown = 0
                else:
                    active_char += 1

        if active_char > total_chars:
            active_char = 1
        


    
        
        # Drawing
        
        
        player.draw(screen)
        
        for enemy in enemies:
            enemy.draw(screen)
            for bar in health_bars:
                bar.draw(enemy.hp, screen)
        
        collect_btn.draw(screen)
        attack_btn.draw(screen)
        ability1_btn.draw(screen)
        
        player_hp.draw(player.hp, screen)
        player_snow.draw(player.snow, screen)


        if not player.alive:
            screen.fill(BLACK)
            create_text("GAME OVER", RED, 100, 400, 300, screen)
        
        pg.display.flip()
        

# if __name__ == "__main__":
#     combat()





