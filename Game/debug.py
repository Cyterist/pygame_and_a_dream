import pygame as pg
pg.init()
font = pg.font.Font(None, 30)


def debug(info, y=10, x=10):
    display_surface = pg.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pg.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)

def textbox_talk(words, x = 600, y = 600):
    font = pg.font.Font(None, 80)
    display_surface = pg.display.get_surface()
    textbox_surf = font.render(str(words), True, 'White')
    textbox_rect = textbox_surf.get_rect(topleft=(x, y))
    pg.draw.rect(display_surface, 'Black', textbox_rect)
    display_surface.blit(textbox_surf, textbox_rect)
