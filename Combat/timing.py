import pygame as pg

class TimeBar():

    def __init__(self, x, y, color, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height

        self.bar = pg.Rect((self.x, self.y), (self.width, self.height))

    def check_collision(self, rect):
        if self.bar.colliderect(rect):
            return True
        else:
            return False

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.bar)

