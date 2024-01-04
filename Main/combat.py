from UI_Button import *
from Character import *
from bars import *
from information import *
from debug import debug
from fights import *


combat_background = pg.image.load('pics/assets/background.png').convert_alpha()
scaled_bg = pg.transform.scale(
    combat_background, (combat_background.get_width() * 4, combat_background.get_height() * 4))
panel = pg.image.load('pics/assets/panel.png')
scaled_panel = pg.transform.scale(
    panel, (panel.get_width() * 3.25, panel.get_height() * 2.3))


def create_default_screen(screen, enemies):

    screen.blit(scaled_bg, (0, 0))
    screen.blit(scaled_panel, (-90, WINDOWHEIGHT-BOTTOM_PANEL-85))

    create_text(f'{player.name} HP: {player.hp}', WHITE, 30,
                200, WINDOWHEIGHT - BOTTOM_PANEL + 15, screen)
    create_text(f'{player.name} SNOW: {player.snow}', WHITE, 30,
                200, WINDOWHEIGHT - BOTTOM_PANEL + 75, screen)

    for i, enemy in enumerate(enemies):
        create_text(f'{enemy.name} HP: {enemy.hp}', WHITE, 30, 1000,
                    (WINDOWHEIGHT - BOTTOM_PANEL + 15) + i * 60, screen)


def create_text(text, text_color, font_size, x, y, screen, bgcolor=None):
    font = pg.font.Font("EquipmentPro.ttf", font_size)
    image = font.render(text, True, text_color, bgcolor)
    screen.blit(image, (x, y))


def check_sides(rect):
    if rect.left <= 350:
        return True
    elif rect.right >= 950:
        return True
    else:
        return False


class Combat():

    def __init__(self):
        self.active_char = 1
        # 100 is one second
        self.win_wait = 150
        self.wait = 100
        self.attack = False
        self.ability_1 = False
        self.target = None
        self.white_bar_speed = 0
        self.yellow = False
        self.red = False
        self.green = False
        self.combat = True
        self.loss = False
        self.running = False
        self.win = False
        self.cooldown = 0
        self.end_combat = False
    
    def reset_attack(self):
        self.red = False
        self.green = False
        self.yellow = False

    def start_combat(self):
        # Initialize combat state
        self.running = True
        self.win = False
        self.cooldown = 0
        self.end_combat = False

    def ends_combat(self):
        # Clean up combat state
        self.running = False
        self.end_combat = True
        fights['creeper1']['fight_begun'] = False
        fights['creeper2']['fight_begun'] = False


    # Main combat function

    def run(self, screen, enemies, total_chars, health_bars):
        if not fights['creeper1']['fight_begun'] and not fights['creeper2']['fight_begun']:
            self.win = False
            self.running = False
            self.cooldown = 0

        self.attack_btn = UIButton(center_position=(
            650, 608), font_size=30, text_color=WHITE, text="Attack")
        self.ability1_btn = UIButton(center_position=(
            650, 658), font_size=30, text_color=WHITE, text="Ability 1")
        self.collect_btn = UIButton(center_position=(
            650, 558), font_size=30, text_color=WHITE, text="Collect Snow")
        if fights['creeper1']['fight_begun'] or fights['creeper2']['fight_begun']:
            self.start_combat()
            while self.running and not self.end_combat:
                create_default_screen(screen, enemies)

                self.mouse_up = False
                self.mouse_pos = pg.mouse.get_pos()

                keys = pg.key.get_pressed()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        pg.quit()
                    if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                        self.mouse_up = True

                # Update Buttons
                self.attack_btn.update(self.mouse_pos)
                # ability1_btn.update(mouse_pos)
                self.collect_btn.update(self.mouse_pos)

                if player.snow >= 10:
                    self.ability1_btn.update(self.mouse_pos)

                # players turn
                if player.alive:
                    if self.active_char == 1:

                        # Check if action was selection
                        if not self.attack and not self.ability_1:

                            # create_text("Your Turn", WHITE, 50, 550, 0, screen)
                            textbox_talk('Your Turn!', 50, bg_color=None, x=550, y=0)

                            if self.attack_btn.clicked(self.mouse_pos, self.mouse_up):
                                self.attack = True

                            if self.ability1_btn.clicked(self.mouse_pos, self.mouse_up) and player.snow >= 10:
                                self.ability_1 = True

                            if self.collect_btn.clicked(self.mouse_pos, self.mouse_up):
                                player.collect_snow()
                                self.active_char += 1

                        if self.attack or self.ability_1:
                            textbox_talk('Select Target', 50, bg_color=None, x=550, y=0)
                            # create_text("Select Target", WHITE, 50, 550, 0, screen)
                            for enemy in enemies:
                                if enemy.rect.collidepoint(self.mouse_pos) and self.mouse_up and enemy.alive:
                                    self.target = enemy

                        if self.attack == True and self.target != None:
                            for bar in attack_bars:
                                bar.draw(screen)

                            if self.white_bar_speed == 0:
                                self.white_bar_speed = 1

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

                            if self.red == True and not self.yellow:
                                player.attack(self.target, 0)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.yellow == True and not self.green:
                                player.attack(self.target, 3)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.green == True and not self.yellow:
                                player.attack(self.target, 10)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.red and self.yellow:
                                player.attack(self.target, 3)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.yellow and self.green:
                                player.attack(self.target, 10)
                                self.reset_attack()
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

                # Enemy Turn
                dead_list = []
                for i, enemy in enumerate(enemies):
                    if self.active_char == 2 + i:
                        if enemy.alive:
                            textbox_talk('Enemy Turn!', 50, bg_color=None, x=550, y=0)
                            # TODO Find absolute reference for enemy health bar location, then input whatever action the enemy takes
                            healthbar_loc = healthbar_list[i]
                            textbox_talk('Creeper Attacks!', 30, color='Black', x=healthbar_loc.x - 200, y=healthbar_loc.y - 20)
                            self.cooldown += 1
                            if self.cooldown >= self.wait:
                                enemy.attack(player)
                                self.active_char += 1
                                self.cooldown = 0
                        else:
                            dead_list.append(enemy)
                            self.active_char += 1
                            self.cooldown = 0

                if len(dead_list) == len(enemies):
                    self.win = True
                        

                if self.active_char > total_chars:
                    self.active_char = 1

                # Drawing

                player.draw(screen)

                for enemy in enemies:
                    enemy.draw(screen)

                for bar, enemy in zip(health_bars, enemies):
                    bar.draw(enemy.hp, screen)

                self.collect_btn.draw(screen)
                self.attack_btn.draw(screen)
                self.ability1_btn.draw(screen)

                player_hp.draw(player.hp, screen)
                player_snow.draw(player.snow, screen)

                
                if not player.alive:
                    screen.fill(BLACK)
                    create_text("GAME OVER", RED, 100, 400, 300, screen)
                    self.cooldown += 1
                    if self.cooldown >= self.win_wait:
                        self.loss = True
                        self.combat = False
                        self.ends_combat()
                    


                if self.win:
                    screen.fill(YELLOW)
                    create_text("YOU HAVE WON", BLACK, 100, 400, 300, screen)
                    self.cooldown += 1
                    if self.cooldown >= self.win_wait:
                        if fights['creeper1']['fight_begun']:
                            fights['creeper1']['fight_won'] = True
                        if fights['creeper2']['fight_begun']:
                            fights['creeper2']['fight_won'] = True
                        self.combat = False
                        self.win = False
                        self.ends_combat()
                        
                    

                pg.display.flip()


# if __name__ == "__main__":
#     combat()
