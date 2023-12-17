import pygame as pg
import pygame.freetype as pgft
from pygame.sprite import Sprite

#Highlight color
YELLOW = (255, 255, 0)

# easy text creator
def create_surface_text(text, font_size, text_color, surface_color):
    font = pgft.SysFont("Arial", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor = text_color, bgcolor=surface_color)
    return surface.convert_alpha()

# Class to make UI buttons
class UIButton(Sprite):
    def __init__(self, center_position, text, font_size, surface_color, text_color):
        
        super().__init__()
        
        self.mouse_over = False

        default = create_surface_text(text, font_size, text_color, surface_color)

        highlighted = create_surface_text(text, font_size, YELLOW, surface_color)

        self.images = [default, highlighted]
        self.rects = [default.get_rect(center=center_position), highlighted.get_rect(center=center_position)]
        
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]
    
    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
    
    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
        else:
            self.mouse_over = False
    
    def clicked(self,mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos) and mouse_up:
            return True
        else:
            return False
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)
        
