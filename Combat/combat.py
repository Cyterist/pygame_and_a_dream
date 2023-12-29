from UI_Button import *
from Character import *
from bars import *
from info import *


background = pg.image.load('pics/assets/background.png')
scaled_bg = pg.transform.scale(background, (background.get_width() * 4, background.get_height() * 4))
panel = pg.image.load('pics/assets/panel.png')
scaled_panel = pg.transform.scale(panel, (panel.get_width() * 3.25, panel.get_height() * 2.3))

def create_default_screen(screen, enemies):
        
        screen.blit(scaled_bg,(0,0))
        screen.blit(scaled_panel, (-90, SCREEN_HEIGHT-BOTTOM_PANEL-85))
        
        
        create_text(f'{player.name} HP: {player.hp}', WHITE, 30, 200, SCREEN_HEIGHT - BOTTOM_PANEL + 15, screen)
        create_text(f'{player.name} SNOW: {player.snow}', WHITE, 30, 200, SCREEN_HEIGHT - BOTTOM_PANEL + 75, screen)
        
        for i, enemy in enumerate(enemies):
            create_text(f'{enemy.name} HP: {enemy.hp}', WHITE, 30, 1000, (SCREEN_HEIGHT - BOTTOM_PANEL + 15) + i * 60, screen)

def create_text(text, text_color, font_size, x, y, screen, bgcolor=None):
        font = pg.font.SysFont("Arial", font_size)
        image = font.render(text, True, text_color, bgcolor)
        screen.blit(image, (x, y))

def check_sides(rect):
    if rect.left <= 350:
        return True
    elif rect.right >= 950:
        return True
    else:
        return False


class Combat:
    
    def __init__(self):
        self.active_char = 1
        self.cooldown = 0
        self.wait = 100
        self.attack = False
        self.ability_1 = False
        self.target = None
        self.white_bar_speed = 0
        self.yellow = False
        self.red = False
        self.green = False


    #text function v2, cause I can't figure out why the one from UI_button won't work in certain cases



    # Creating screen


    # Main game function

    def run(self, screen, enemies, total_chars, health_bars):
        # pg.init()

        
        # screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.attack_btn = UIButton(center_position=(650,608), font_size=30, text_color=WHITE, text="Attack")
        self.ability1_btn = UIButton(center_position=(650,658), font_size=30, text_color=WHITE, text="Ability 1")
        self.collect_btn = UIButton(center_position=(650,558), font_size=30, text_color=WHITE, text="Collect Snow")

        
        while True:
            
            #   variables
            # self.active_char
            # self.cooldown
            # self.wait
            # self.attack
            # self.target
            # self.white_bar_speed
            # yellow
            # red
            # green
            # ability_1
            
            create_default_screen(screen, enemies)

            self.mouse_up = False
            self.mouse_pos = pg.mouse.get_pos()

            keys = pg.key.get_pressed()

            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    self.mouse_up = True
            
            #Update Buttons
            self.attack_btn.update(self.mouse_pos)
            # ability1_btn.update(mouse_pos)
            self.collect_btn.update(self.mouse_pos)

            if player.snow >= 10:
                self.ability1_btn.update(self.mouse_pos)

            #players turn
            if player.alive:
                if self.active_char == 1:
                    
                    #Check if action was selection
                    if not self.attack and not self.ability_1: 
                        
                        create_text("Your Turn", WHITE, 50, 550, 0, screen)
                        
                        if self.attack_btn.clicked(self.mouse_pos, self.mouse_up):
                            self.attack = True
                            print("attack")
                    
                        if self.ability1_btn.clicked(self.mouse_pos, self.mouse_up) and player.snow >= 10:
                            self.ability_1 = True
                            print("ability")
                        
                        if self.collect_btn.clicked(self.mouse_pos, self.mouse_up):
                            player.collect_snow()
                            self.active_char += 1

                    if self.attack or self.ability_1:
                        create_text("Select self.Target", WHITE, 50, 550, 0, screen)
                        for enemy in enemies:
                            if enemy.rect.collidepoint(self.mouse_pos) and self.mouse_up:
                                self.target = enemy
                                print(self.target) 
                    
                    if self.attack == True and self.target != None:
                        for bar in attack_bars:
                            bar.draw(screen)
                        
                        if self.white_bar_speed == 0:
                            self.white_bar_speed = 3
                        
                        white_bar.x += self.white_bar_speed
                        pg.draw.rect(screen, WHITE, white_bar)
                        self.side = check_sides(white_bar)
                        if self.side:
                            self.white_bar_speed *= -1
                        if keys[pg.K_SPACE]:
                            if attack_y1.check_collision(white_bar) or attack_y2.check_collision(white_bar):
                                self.yellow = True
                            if attack_r1.check_collision(white_bar) or attack_r2.check_collision(white_bar):
                                self.red = True
                            if attack_g.check_collision(white_bar):
                                self.green = True
                        
                        if self.red == True:
                            player.attack(self.target, 0)
                            self.red = False
                            self.target = None
                            white_bar.x = 350
                            self.attack = False
                            self.active_char += 1
                        if self.yellow == True:
                            player.attack(self.target, 3)
                            self.yellow = False
                            self.target = None
                            white_bar.x = 350
                            self.attack = False
                            self.active_char += 1
                        if self.green == True:
                            player.attack(self.target, 10)
                            self.green = False
                            self.target = None
                            white_bar.x = 350
                            self.attack = False
                            self.active_char += 1
                    
                    if self.ability_1 == True and self.target != None:
                        for bar in hard_bars:
                            bar.draw(screen)
                        
                        if self.white_bar_speed == 0:
                            self.white_bar_speed = 4
                        
                        white_bar.x += self.white_bar_speed
                        pg.draw.rect(screen, WHITE, white_bar)
                        self.side = check_sides(white_bar)
                        if self.side:
                            self.white_bar_speed *= -1
                        if keys[pg.K_SPACE]:
                            if attack_y1.check_collision(white_bar) or attack_y2.check_collision(white_bar):
                                self.yellow = True
                            if attack_r1.check_collision(white_bar) or attack_r2.check_collision(white_bar):
                                self.red = True
                            if attack_g.check_collision(white_bar):
                                self.green = True
                        
                        if self.red == True:
                            player.harder_hitting_ability(self.target, 0)
                            self.red = False
                            self.target = None
                            white_bar.x = 350
                            self.ability_1 = False
                            self.active_char += 1
                        elif self.yellow == True:
                            player.harder_hitting_ability(self.target, 3)
                            self.yellow = False
                            self.target = None
                            white_bar.x = 350
                            self.ability_1 = False
                            self.active_char += 1
                        elif self.green == True:
                            player.harder_hitting_ability(self.target, 10)
                            self.green = False
                            self.target = None
                            white_bar.x = 350
                            self.ability_1 = False
                            self.active_char += 1

            #Enemy Turn  
            for i, enemy in enumerate(enemies):
                if self.active_char == 2 + i:
                    if enemy.alive == True:
                        create_text("Enemy Turn", WHITE, 50, 550, 0, screen)
                        self.cooldown +=1
                        if self.cooldown >= self.wait:
                            enemy.attack(player)
                            self.active_char += 1
                            self.cooldown = 0
                    else:
                        self.active_char += 1

            if self.active_char > total_chars:
                self.active_char = 1
            


        
            
            # Drawing
            
            
            player.draw(screen)
            
            for enemy in enemies:
                enemy.draw(screen)
                for bar in health_bars:
                    bar.draw(enemy.hp, screen)
            
            self.collect_btn.draw(screen)
            self.attack_btn.draw(screen)
            self.ability1_btn.draw(screen)
            
            player_hp.draw(player.hp, screen)
            player_snow.draw(player.snow, screen)


            if not player.alive:
                screen.fill(BLACK)
                create_text("GAME OVER", RED, 100, 400, 300, screen)
            
            pg.display.flip()
            

# if __name__ == "__main__":
#     combat()





