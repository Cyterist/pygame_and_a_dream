import pygame as pg
import random
from information import *
pg.font.init()
pg.init()

# Character.py has been merged for ease of use, enemy AI is in combat.py
class Character():
    
    def __init__(self, x, y, name, max_hp, max_snow, dmg):
        self.name = name
        self.max_hp = max_hp
        self.max_snow = max_snow
        self.dmg = dmg
        self.hp = max_hp
        self.snow = max_snow
        self.alive = True
        self.combat_throw = False
        self.image = pg.image.load(f'pics/{self.name}/default.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.blind = False

    def collect_snow(self):
        self.snow = self.max_snow
    
    def draw(self, screen):
        if screen != None:
            screen.blit(self.image, self.rect)
    
class Player(Character):
    super.__init__

    def attack(self, target, modifier):
        self.combat_throw = 'True'
        self.image = pg.image.load(f'pics/player_throw/default.png')
        self.draw(screen)
        if target is not None:
            target.hp -= int(self.dmg * modifier)
            if target.hp <= 0:
                target.hp = 0
                target.alive = False
        elif target is None:
            print('Warning: Attempted to attack a NoneType object.')
    

    
    def harder_hitting_ability(self, target, modifier):
        if target is not None:
            self.combat_throw = 'True'
            self.image = pg.image.load(f'pics/player_throw/default.png')
            self.draw(screen)
            target.hp -= int(self.dmg * modifier)
            self.snow -= 10
            if target.hp < 1:
                target.hp = 0
                target.alive = False
        

class Enemy(Character):
        
    super.__init__
        
    def attack(self, target):
        if fights['attack_type'] == 'throws a snowball!':
            target.hp -= self.dmg
            if target.hp < 1:
                target.hp = 0
                target.alive = False
        elif fights['attack_type'] == 'throws a water balloon!' and not target.blind:
            target.hp -= int((self.dmg / 2) - 1)
            target.blind = True
            if target.hp < 1:
                target.hp = 0
                target.alive = False
        elif fights['attack_type'] == 'steals some snow!' and target.snow >= 10:
            snow_amt = random.randint(2, 3)
            snow_steal = int(target.snow / snow_amt)
            target.snow -= snow_steal
            target.hp -= snow_amt
            if target.hp < 1:
                target.hp = 0
                target.alive = False
        elif fights['attack_type'] == 'charges an attack!':
            self.dmg += 5
        elif fights['attack_type'] == 'throws an ice ball!':
            target.hp -= self.dmg + 4
            if target.hp < 1:
                target.hp = 0
                target.alive = False
        else:
            fights['attack_type'] = 'throws a snowball!'
            target.hp -= self.dmg
            if target.hp < 1:
                target.hp = 0
                target.alive = False
    
            



# Class for character health bars

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
    
    def draw(self, hp, screen):
        self.hp = hp
        bar_fill = self.hp / self.max_hp
        pg.draw.rect(screen, RED, (self.x, self.y, 150, 20))
        pg.draw.rect(screen, GREEN, (self.x, self.y, 150 * bar_fill, 20))

class SnowMeter():
    def __init__(self, x, y, snow, max_snow):
        self.x = x
        self.y = y
        self.snow = snow
        self.max_snow = max_snow
    
    def draw(self, snow, screen):
        self.snow = snow
        meter_fill = self.snow / self.max_snow
        if self.snow <= 0:
            self.snow = 0
        pg.draw.rect(screen, BLACK, (self.x, self.y, 150, 20))
        pg.draw.rect(screen, WHITE, (self.x, self.y, 150 * meter_fill, 20))
# Fight details





# CHARACTERS
        
player = Player(200, 350, 'player', 30, 20, 10)
creeper = Enemy(950, 350, 'Harold', 40, 30, 9)
creeper2 = Enemy(850, 350, 'Hawk', 30, 30, 5)
creeper3 = Enemy(1050, 350, 'Hawk', 30, 30, 6)
wolf = Enemy(850, 290, 'Wolf', 55, 30, 9)

player_hp = HealthBar(200, WINDOWHEIGHT - BOTTOM_PANEL + 55, player.hp, player.max_hp)
creeper_hp = HealthBar(1000, WINDOWHEIGHT - BOTTOM_PANEL + 55, creeper.hp, creeper.max_hp)
creeper2_hp = HealthBar(1000, WINDOWHEIGHT - BOTTOM_PANEL + 55, creeper2.hp, creeper2.max_hp)
creeper3_hp = HealthBar(1000, WINDOWHEIGHT - BOTTOM_PANEL + 115, creeper3.hp, creeper3.max_hp)
wolf_hp = HealthBar(1000, WINDOWHEIGHT - BOTTOM_PANEL + 55, wolf.hp, wolf.max_hp)

player_snow = SnowMeter(200, WINDOWHEIGHT - BOTTOM_PANEL + 115, player.snow, player.max_snow)

fights = {
    'END': False,
    'RUN': True,
    'RNG': False,
    'Blind': False,
    'attack_type': 'throws a snowball!',
    'creeper1': {
        'screen': screen,
        'enemies': [creeper],
        'total_chars': 2,
        'health_bars': [creeper_hp],
        'fight_begun': False,
        'fight_won': False
    },
    'wolf1': {
        'screen': screen,
        'enemies': [wolf],
        'total_chars': 2,
        'health_bars': [wolf_hp],
        'fight_begun': False,
        'fight_won': False
    },
    'creeper2': {
        'screen': screen,
        'enemies': [creeper2, creeper3],
        'total_chars': 3,
        'health_bars': [creeper2_hp, creeper3_hp],
        'fight_begun': False,
        'fight_won': False
    }
}
