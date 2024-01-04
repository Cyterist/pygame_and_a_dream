import pygame as pg
pg.init()
font = pg.font.Font('EquipmentPro.ttf', 52)


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

def renderTextCenteredAt(npc_name, text, screen, font = font, color = 'White', x=500, y=650, allowed_width=890, allowed_height = 300):
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
    box_width = 900
    box_height = max(total_height, allowed_height) - 150
    box_x = x - box_width / 2
    box_y = y - total_height / 2 - 40  # Adjust for the text margins

    # Render the box
    box_rect = pg.Rect(box_x, box_y, box_width, box_height)
    pg.draw.rect(screen, (74, 85, 85), box_rect)  # Change color as needed

    # Render the NPC's name above the text
    name_rect = pg.Rect(50, 425, 900, 285)
    pg.draw.rect(screen, (74, 85, 85), name_rect)
    name_font_size = 60
    name_font = pg.font.Font('EquipmentPro.ttf', name_font_size)
    name_surface = name_font.render(npc_name, True, color)
    name_x = x - name_surface.get_width() / 2
    name_y = box_y - name_surface.get_height() - 10  # Adjust for spacing
    screen.blit(name_surface, (name_x, 435))
    

    # Render each line of text
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - box_width / 2  # Adjusted to left-align the text within the box
        ty = y + y_offset - total_height / 2 - 45  # Adjust for the text margins

        font_surface = font.render(line, True, color)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh