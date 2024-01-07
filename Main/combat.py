from UI_Button import *
from bars import *
from information import *
from debug import *
from fights import *
import random
pg.font.init()


combat_background = pg.image.load('pics/assets/background.png').convert_alpha()
scaled_bg = pg.transform.scale(
    combat_background, (combat_background.get_width(), combat_background.get_height()))
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


def check_sides():
    if white_bar.x <= 350:
        return True
    elif white_bar.x >= 950:
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
        self.contain = False
    
    def terminate(self):
        self.ends_combat()
        pg.quit()
        sys.exit()

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
        fights['wolf1']['fight_begun'] = False
    
    # Basic combat AI
    def hawk_combat(self, opponent):
        enemy = opponent
        if enemy.name == 'Hawk':
            attack = random.randint(0, 2)
            if attack == 0:
                fights['attack_type'] = 'throws a snowball!'
                print(fights['attack_type'])
            if attack == 1:
                fights['attack_type'] = 'throws a water balloon!'
                print(fights['attack_type'])
            if attack == 2:
                fights['attack_type'] = 'throws a snowball!'
                print(fights['attack_type'])
    def wolf_combat(self, opponent):
        enemy = opponent
        if enemy.name == 'Wolf':
            attack = random.randint(0, 6)
            if attack == 0 or attack == 5 or attack == 6:
                fights['attack_type'] = 'throws a snowball!'
                print(fights['attack_type'])
            if attack == 1:
                fights['attack_type'] = 'throws a water balloon!'
                print(fights['attack_type'])
            if attack == 2 or attack == 4:
                fights['attack_type'] = 'steals some snow!'
                print(fights['attack_type'])
            if attack == 3:
                fights['attack_type'] = 'charges an attack!'
                print(fights['attack_type'])
        


    # Main combat function

    def run(self, screen, enemies, total_chars, health_bars):
        if not fights['RUN']:
            self.terminate(self)
        player.hp = player.max_hp
        player.snow = player.max_snow
        self.no_snow = False
        if not fights['creeper1']['fight_begun'] and not fights['creeper2']['fight_begun']:
            self.win = False
            self.running = False
            self.cooldown = 0

        self.attack_btn = UIButton(center_position=(
            650, 608), font_size=45, text_color=WHITE, text="Snowball")
        self.ability1_btn = UIButton(center_position=(
            650, 658), font_size=45, text_color=WHITE, text="Ice Ball COST: 10")
        self.collect_btn = UIButton(center_position=(
            650, 558), font_size=45, text_color=WHITE, text="Collect Snow")
        if fights['creeper1']['fight_begun'] or fights['creeper2']['fight_begun'] or fights['wolf1']['fight_begun']:
            self.start_combat()
            while self.running and not self.end_combat:
                create_default_screen(screen, enemies)

                self.mouse_up = False
                self.mouse_pos = pg.mouse.get_pos()

                keys = pg.key.get_pressed()

                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        self.terminate()
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_m:
                            pg.mixer.music.set_volume(0)
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
                        if player.blind:
                            textbox_talk('Blinded!', 50, color = 'Red', bg_color=None, x=140, y=260)
                        # Check if action was selection
                        if not self.attack and not self.ability_1:
                            if player.name == 'player_throw':
                                print(player.name)
                                player.name = 'player'
                                player.image = pg.image.load(f'pics/{player.name}/default.png')
                            textbox_talk('Your Turn!', 50, bg_color=None, x=550, y=0)

                            if self.attack_btn.clicked(self.mouse_pos, self.mouse_up):
                                self.attack = True

                            if self.ability1_btn.clicked(self.mouse_pos, self.mouse_up) and player.snow >= 10:
                                self.ability_1 = True
                            elif self.ability1_btn.clicked(self.mouse_pos, self.mouse_up):
                                self.no_snow = True
                            elif self.no_snow:
                                textbox_talk('Not Enough Snow!', 50, bg_color=None, x=550, y=50)


                            if self.collect_btn.clicked(self.mouse_pos, self.mouse_up):
                                player.collect_snow()
                                self.active_char += 1

                        if self.attack or self.ability_1:
                            textbox_talk('Select Target', 50, bg_color=None, x=550, y=0)
                            for enemy in enemies:
                                if enemy.rect.collidepoint(self.mouse_pos) and self.mouse_up and enemy.alive:
                                    self.target = enemy

                        if self.attack == True and self.target != None:
                            for bar in attack_bars:
                                bar.draw(screen)
                            if player.blind and not self.contain:
                                self.white_bar_speed = 14
                            if not player.blind and not self.contain:
                                self.white_bar_speed = 6
                            white_bar.x += self.white_bar_speed
                            pg.draw.rect(screen, WHITE, white_bar)
                            self.side = check_sides()
                            if player.blind:
                                if white_bar.x > 950 or white_bar.x < 350:
                                    print('speed reversed and blind')
                                    self.contain = True
                                    self.white_bar_speed *= -1
                                    if white_bar.x > 1100 or white_bar.x < 200:
                                        white_bar.x = 400
                            else:
                                if self.side or white_bar.x > 950 or white_bar.x < 350:
                                    self.contain = True
                                    print(f'speed reversed and not blind {self.white_bar_speed}')
                                    self.white_bar_speed *= -1
                                    if white_bar.x > 1100 or white_bar.x < 200:
                                        white_bar.x = 400
                                
                            if keys[pg.K_SPACE]:
                                self.contain = False
                                if player.blind:
                                    player.blind = False
                                if attack_y1.check_collision(white_bar) or attack_y2.check_collision(white_bar):
                                    self.yellow = True
                                if attack_r1.check_collision(white_bar) or attack_r2.check_collision(white_bar):
                                    self.red = True
                                if attack_g.check_collision(white_bar):
                                    self.green = True
                                if not self.green and not self.yellow and not self.red:
                                    player.attack(self.target, 1)
                                    self.reset_attack()
                                    self.target = None
                                    white_bar.x = 350
                                    self.attack = False
                                    self.active_char += 1

                            if self.red == True and not self.yellow:
                                player.attack(self.target, 0)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.yellow == True and not self.green:
                                player.attack(self.target, 1)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.green == True and not self.yellow:
                                player.attack(self.target, 1.5)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.red and self.yellow:
                                player.attack(self.target, 0.5)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.yellow and self.green:
                                player.attack(self.target, 1.25)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1



                        if self.ability_1 == True and self.target != None:
                            for bar in hard_bars:
                                bar.draw(screen)
                            if player.blind and not self.contain:
                                self.white_bar_speed = 14
                            if not player.blind and not self.contain:
                                self.white_bar_speed = 9
                            white_bar.x += self.white_bar_speed
                            pg.draw.rect(screen, WHITE, white_bar)
                            self.side = check_sides()
                            if player.blind:
                                if white_bar.x > 950 or white_bar.x < 350:
                                    self.white_bar_speed = 14
                                    print('speed reversed and blind')
                                    self.contain = True
                                    self.white_bar_speed *= -1
                                    if white_bar.x > 1100 or white_bar.x < 200:
                                        white_bar.x = 400
                            else:
                                if self.side or white_bar.x > 950 or white_bar.x < 350:
                                    self.contain = True
                                    print(f'speed reversed and not blind {self.white_bar_speed}')
                                    self.white_bar_speed *= -1
                                    if white_bar.x > 1100 or white_bar.x < 200:
                                        white_bar.x = 400
                                
                            if keys[pg.K_SPACE]:
                                self.contain = False
                                if player.blind:
                                    player.blind = False
                                if attack_y1.check_collision(white_bar) or attack_y2.check_collision(white_bar):
                                    self.yellow = True
                                if attack_r1.check_collision(white_bar) or attack_r2.check_collision(white_bar):
                                    self.red = True
                                if attack_g.check_collision(white_bar):
                                    self.green = True

                            if self.red == True and not self.yellow:
                                player.harder_hitting_ability(self.target, 0.25)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.yellow == True and not self.green:
                                player.harder_hitting_ability(self.target, 1.25)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.green == True and not self.yellow:
                                player.harder_hitting_ability(self.target, 1.85)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.red and self.yellow:
                                player.harder_hitting_ability(self.target, 1.25)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1
                            if self.yellow and self.green:
                                player.harder_hitting_ability(self.target, 1.75)
                                self.reset_attack()
                                self.target = None
                                white_bar.x = 350
                                self.attack = False
                                self.active_char += 1

                # Enemy Turn
                dead_list = []
                for i, enemy in enumerate(enemies):
                    if self.active_char == 2 + i:
                        if enemy.alive:
                            if not fights['RNG']:
                                self.hawk_combat(enemy)
                                self.wolf_combat(enemy)
                                fights['RNG'] = True
                                print(f" {enemy.name} {fights['attack_type']}")
                            textbox_talk('Enemy Turn!', 50, bg_color=None, x=550, y=0)
                            enemy_x, enemy_y = enemy.rect.center
                            opp = enemy.name
                            att = fights['attack_type']
                            textbox_talk(opp + ' ' + att, 30, color='Black', x=enemy_x - 100, y=enemy_y - 100, bg_color='White')
                            self.cooldown += 1
                            if self.cooldown >= self.wait:
                                enemy.attack(player)
                                fights['RNG'] = False
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
                        self.terminate()
                    


                if self.win:
                    screen.fill(YELLOW)
                    create_text("YOU HAVE WON", BLACK, 100, 400, 300, screen)
                    self.cooldown += 1
                    if self.cooldown >= self.win_wait:
                        if fights['creeper1']['fight_begun']:
                            fights['creeper1']['fight_won'] = True
                        if fights['creeper2']['fight_begun']:
                            fights['creeper2']['fight_won'] = True
                        if fights['wolf1']['fight_begun']:
                            fights['wolf1']['fight_won'] = True
                        self.combat = False
                        self.win = False
                        self.ends_combat()
                        
                    

                pg.display.flip()


# if __name__ == "__main__":
#     combat()
