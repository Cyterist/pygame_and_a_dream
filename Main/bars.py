from timing import *
from information import *

TOTAL_BAR = 600

# white bar
white_bar = pg.Rect((350,75), (6, 30))

# Attack SR-MSY-MG-MSY-SR

attack_r1 = TimeBar(350, 80, RED, 50, 20)
attack_r2 = TimeBar(900, 80, RED, 50, 20)
attack_y1 = TimeBar(400, 80, YELLOW, 125, 20)
attack_y2 = TimeBar(775, 80, YELLOW, 125, 20)
attack_g = TimeBar(525, 80, GREEN, 250, 20)

attack_bars = [attack_r1, attack_y1, attack_g, attack_y2, attack_r2]

# Hard hitting ability MR-MY-SG-MY-MR
hard_r1 = TimeBar(350, 80, RED, 135, 20)
hard_r2 = TimeBar(815, 80, RED, 135, 20)
hard_y1 = TimeBar(485, 80, YELLOW, 135, 20)
hard_y2 = TimeBar(680, 80, YELLOW, 135, 20)
hard_g = TimeBar(620, 80, GREEN, 60, 20)

hard_bars = [hard_r1, hard_y1, hard_g, hard_y2, hard_r2]




