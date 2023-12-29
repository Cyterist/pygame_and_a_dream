import pygame as pg
pg.init()
font = pg.font.Font(None, 55)


def debug(info, y=10, x=10):
    display_surface = pg.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pg.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)

def textbox_talk(words, text_size = 10, color = 'White', bg_color = 'Black', x = 600, y = 600):
    font = pg.font.Font(None, text_size)
    display_surface = pg.display.get_surface()
    textbox_surf = font.render(str(words), True, color)
    textbox_rect = textbox_surf.get_rect(topleft=(x, y))
    pg.draw.rect(display_surface, bg_color, textbox_rect)
    display_surface.blit(textbox_surf, textbox_rect)

def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width, allowed_height = 300):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # Calculate the total height of the text block
    total_height = sum(font.size(line)[1] for line in lines)
    
    # Calculate the position and size of the box
    box_width = 700
    box_height = max(total_height, allowed_height)
    box_x = x - box_width / 2
    box_y = y - total_height / 2 - 50  # Adjust for the text margins
    
    # Render the box
    box_rect = pg.Rect(box_x, box_y, box_width, box_height)
    pg.draw.rect(screen, (74, 85, 85), box_rect)  # Change color as needed

    # Render each line of text
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset - total_height / 2 - 50  # Adjust for the text margins

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh