import pygame as pg

RED = (255, 0 , 0)
GREEN = (0, 255, 0)
# Class for creating characters

class Character():
    
    def __init__(self, x, y, name, max_hp, dmg):
        self.name = name
        self.max_hp = max_hp
        self.dmg = dmg
        self.hp = max_hp
        self.alive = True
        self.image = pg.image.load(f'pics/{self.name}/default.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def attack(self, target):
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