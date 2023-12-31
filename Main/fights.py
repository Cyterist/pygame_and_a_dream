import pygame as pg
from information import *
from Character import *

# Fight details
fights = {
    'creeper1': {
        'screen': screen,
        'enemies': [creeper],
        'total_chars': 2,
        'health_bars': [creeper_hp],
        'fight_begun': False,
        'fight_won': False
    },
    #  self.combat.run(screen, [creeper, creeper2], 3, [creeper_hp, creeper2_hp]
    'creeper2': {
        'screen': screen,
        'enemies': [creeper, creeper2],
        'total_chars': 3,
        'health_bars': [creeper_hp, creeper2_hp],
        'fight_begun': False,
        'fight_won': False
    } 
}