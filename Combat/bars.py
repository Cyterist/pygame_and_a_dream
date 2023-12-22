from timing import *

RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
WHITE = (255,255,255)
TOTAL_BAR = 600

# white bar
white_bar = pg.Rect((350,75), (5, 30))
# Attack SR-MSY-MG-MSY-SR

attack_r1 = TimeBar(350, 80, RED, 50, 20)
attack_r2 = TimeBar(900, 80, RED, 50, 20)
attack_y1 = TimeBar(400, 80, YELLOW, 125, 20)
attack_y2 = TimeBar(775, 80, YELLOW, 125, 20)
attack_g = TimeBar(525, 80, GREEN, 250, 20)

attack_bars = [attack_r1, attack_y1, attack_g, attack_y2, attack_r2]



