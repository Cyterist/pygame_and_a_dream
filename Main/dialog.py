import pygame as pg
from information import *
from debug import *

# 'n' is the name of the NPC, d is to represent if the dialog has already been seen
dialog = {
    'npc1':{
        'n': 'Information Sign',
        'line1': 'This should theoretically split the text into lines that actually fit on the page. Combine it with a textbox art, and this could look good.',
        'line2': 'You won the fight!',
        'line3': 'Keep talking to me to learn more!',
        'line4': 'no'
    },
    'npc2':{
        'n': 'Jimmy',
        'line1': 'Theme of giving? More like giving up',
        'line2': "You didn't give up!?"
    },
    'd':{
        'npc1line1': False,
        'npc1line2': False,
        'npc1line3': False,
        'npc1line4': False
    }
}