import pygame as pg
from information import *
from debug import *
pg.init()
# Class for creating characters

class Character():
    
    def __init__(self, x, y, name, max_hp, max_snow, dmg):
        self.name = name
        self.max_hp = max_hp
        self.max_snow = max_snow
        self.dmg = dmg
        self.hp = max_hp
        self.snow = max_snow
        self.alive = True
        self.image = pg.image.load(f'pics/{self.name}/default.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def collect_snow(self):
        self.snow = self.max_snow
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
class Player(Character):
    super.__init__

    def attack(self, target, modifier):
        if target is not None:
            target.hp -= self.dmg + modifier
            if target.hp <= 0:
                target.hp = 0
                target.alive = False
        elif target is None:
            print('Warning: Attempted to attack a NoneType object.')
    

    
    def harder_hitting_ability(self, target, modifier):
        target.hp -= round(self.dmg*1.5) + modifier
        self.snow -= 10
        if target.hp < 1:
            target.hp = 0
            target.alive = False
        

class Enemy(Character):
        
    super.__init__
        
    def attack(self, target):
        if target is not None:
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


# CHARACTERS
        
player = Player(200, 400, 'player', 30, 30, 1)
creeper = Enemy(850, 390, 'creeper', 30, 30, 1)
creeper2 = Enemy(1050, 390, 'creeper', 30, 30, 1)
creeper3 = Enemy(850, 390, 'creeper', 30, 30, 1)

player_hp = HealthBar(200, WINDOWHEIGHT - BOTTOM_PANEL + 55, player.hp, player.max_hp)
creeper_hp = HealthBar(1000, WINDOWHEIGHT - BOTTOM_PANEL + 55, creeper.hp, creeper.max_hp)
creeper2_hp = HealthBar(1000, WINDOWHEIGHT - BOTTOM_PANEL + 115, creeper2.hp, creeper2.max_hp)
creeper3_hp = HealthBar(1000, WINDOWHEIGHT - BOTTOM_PANEL + 55, creeper3.hp, creeper3.max_hp)
player_snow = SnowMeter(200, WINDOWHEIGHT - BOTTOM_PANEL + 115, player.snow, player.max_snow)
