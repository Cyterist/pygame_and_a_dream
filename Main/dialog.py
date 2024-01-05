import pygame as pg
from information import *
from debug import *
from fights import *

# 'n' is the name of the NPC, d is to represent if the dialog has already been seen
dialog = {
    # Starting sign
    'npc1':{
        'n': 'WARNING!',
        'n2': 'Sign',
        'line1': 'Dangerous snow bandits lay ahead. Tread carefully.',
        'line2': 'Throwing snowballs is a good way to protect oneself.',
        'line3': 'Be careful where you throw them though, because they may destroy what they hit.',
        'line4': 'Unless of course, that is your intention.'
    },
    'npc2':{
        'n': 'Jimmy',
        'line1': 'Theme of giving? More like giving up',
        'line2': "You didn't give up!?",
        'line3': "That's it, you're gonna get it if you don't give up!",
        'line4': "Don't say I didn't warn you.",
        'line5': "Talk about unfair! I can't throw snowballs like that.",
        'line6': "I'm not talking to you anymore."
    },
    'd':{
        'npc1Run': False,
        'npc2Run': False,
        'npc1line1': True,
        'npc1line2': False,
        'npc1line3': False,
        'npc1line4': False,
        'npc2line1': True,
        'npc2line2': False,
        'npc2line3': False,
        'npc2line4': False,
        'npc2line5': False,
        'npc2line6': False
    }
}

def sign_dialog(self):
    dialog['d']['npc2Run'] = False
    if dialog['d']['npc1line1']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc1']['n'], dialog['npc1']['line1'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc1line2']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc1']['n2'], dialog['npc1']['line2'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc1line3']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc1']['n2'], dialog['npc1']['line3'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc1line4']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc1']['n2'], dialog['npc1']['line4'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0

def test_dialog(self):
    dialog['d']['npc1Run'] = False
    if dialog['d']['npc2line1']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['line1'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc2line2']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['line2'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc2line3']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['line3'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc2line4']:
        self.talking = True
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['line4'], screen)
        self.combat_cooldown += 1
        if self.combat_cooldown >= 50:
            self.creeper2 = True
            dialog['d']['npc2line4'] = False
            dialog['d']['npc2line5'] = True
            fights['creeper2']['fight_begun'] = True
            self.combat_cooldown = 0
    elif dialog['d']['npc2line5']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['line5'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc2line6']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['line6'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
def end_conversation(self):
    if self.end_talk and dialog['d']['npc1Run']:
        if dialog['d']['npc1line1'] and not dialog['d']['npc1line2']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc1line2'] = True
            dialog['d']['npc1line1'] = False
        elif dialog['d']['npc1line2'] and not dialog['d']['npc1line3'] and not dialog['d']['npc1line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc1line3'] = True
            dialog['d']['npc1line2'] = False
        elif dialog['d']['npc1line3'] and not dialog['d']['npc1line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc1line4'] = True
            dialog['d']['npc1line3'] = False
        elif dialog['d']['npc1line4']:
            dialog['d']['npc1line4'] = False
            dialog['d']['npc1line3'] = False
            dialog['d']['npc1line2'] = False
            dialog['d']['npc1line1'] = True
    if self.end_talk and dialog['d']['npc2Run']:
        if dialog['d']['npc2line1'] and not dialog['d']['npc2line2']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc2line2'] = True
            dialog['d']['npc2line1'] = False
        elif dialog['d']['npc2line2'] and not dialog['d']['npc2line3'] and not dialog['d']['npc2line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc2line3'] = True
            dialog['d']['npc2line2'] = False
        elif dialog['d']['npc2line3'] and not dialog['d']['npc2line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc2line4'] = True
            dialog['d']['npc2line3'] = False
        elif dialog['d']['npc2line4']:
            pass
        elif dialog['d']['npc2line5']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc2line6'] = True
            dialog['d']['npc2line5'] = False
        elif dialog['d']['npc2line6']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc2line1'] = False
            dialog['d']['npc2line2'] = False
            dialog['d']['npc2line3'] = False
            dialog['d']['npc2line4'] = False
            dialog['d']['npc2line5'] = True
            dialog['d']['npc2line6'] = False
    self.cooldown = 0