import pygame as pg
from information import *
from debug import *
from fights import *
pg.init()
pg.font.init()

# 'n' is the name of the NPC, d is to represent if the dialog has already been seen
dialog = {
    # Starting sign
    'jack':{
        'n': 'Ben',
        'line1': "Hey, you're just the person I was looking for! See, I'm trying to build a snowman, but the only thing stopping me is that I don't have a hat! Can you believe it?",
        'line2': "You're such a good friend to me, so I know you'll find my hat. I know I lost my hat somewhere outside, but I can't remember where. Maybe it was stolen?",
        'line3': 'Well anyway, if you find my hat, please bring it back to me!',
        'line4': "Don't worry, I'm not going anywhere.",
        'WIN': "You found my hat! Thank you so much, now I can not only make a snowman, but put a hat on it too! You have truly brought meaning into my life by giving me this."
    },
    'npc2':{
        'n': 'Mean Hawks',
        'snow': 'Why would you hit me with a snowball? That was not a kind thing to do.',
        'hat': 'Yeah alright, you can have your hat back. Who would want that dirty old thing anyway?',
        'line1': "Maybe I do have your hat, maybe I don't. What are you going to do about it? You may as well give up while you're ahead, or else I'll make you give up.",
        'line2': "Don't say I didn't warn you.",
        'line3': "Talk about unfair! I can't throw snowballs like that.",
        'line4': "I'm not talking to you anymore.",
        'line5': "I'm not talking to you anymore.",
        'line6': "I'm not talking to you anymore."
    },
    'npc3':{
        'n': 'Hungry Wolf',
        'snow': 'Hitting me with snow just makes me hungry...',
        'hat': "Fine! Take your stupid hat and just get out of my sight. I went easy on you anyway.",
        'line1': "You want a hat? Yeah, just get a little bit closer and I'll give it to you, free of charge.",
        'line2': "Should've cried wolf.",
        'line3': "You looked like easy prey...",
        'line4': "I'm all bark, no bite."
    },
    'npc4':{
        'n': 'Harold',
        'snow': 'You hit me with a snowball too! That really hurt!',
        'hat': 'Oh, you were looking for a hat? Here, you can have this one! I found it on the bench over there, I promise!',
        'line1': "I was hoping you wouldn't see me. But since we're here, we may as well make the most of it and have a snowball fight!",
        'line2': "I won't go easy!",
        'line3': "You really challenged me! Next time I'll get you for sure.",
        'line4': "Don't you have something better to do?"
    },
    'd':{
        'jackRun': False,
        'npc2Run': False,
        'npc3Run': False,
        'npc4Run': False,
        'npc2Win': False,
        'npc3Win': False,
        'npc4Win': False,
        'npc2hit': False,
        'npc3hit': False,
        'npc4hit': False,
        'jackline1': True,
        'jackline2': False,
        'jackline3': False,
        'jackline4': False,
        'npc2line1': True,
        'npc2line2': False,
        'npc2line3': False,
        'npc2line4': False,
        'npc2line5': False,
        'npc2line6': False,
        'npc3line1': True,
        'npc3line2': False,
        'npc3line3': False,
        'npc3line4': False,
        'npc4line1': True,
        'npc4line2': False,
        'npc4line3': False,
        'npc4line4': False,
    }
}

def jack_dialog(self):
    dialog['d']['npc2Run'] = False
    dialog['d']['npc3Run'] = False
    dialog['d']['npc4Run'] = False
    if fights['creeper1']['fight_won'] and fights['creeper2']['fight_won'] and fights['wolf1']['fight_won']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['jack']['n'], dialog['jack']['WIN'], screen)
        if self.talking_cooldown >= 500:
            fights['END'] = True
    elif dialog['d']['jackline1']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['jack']['n'], dialog['jack']['line1'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['jackline2']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['jack']['n'], dialog['jack']['line2'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['jackline3']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['jack']['n'], dialog['jack']['line3'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['jackline4']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['jack']['n'], dialog['jack']['line4'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    
    
def npc2_dialog(self):
    dialog['d']['jackRun'] = False
    dialog['d']['npc3Run'] = False
    dialog['d']['npc4Run'] = False
    print(fights['creeper1']['fight_won'], fights['creeper2']['fight_won'], fights['wolf1']['fight_won'])
    if fights['creeper1']['fight_won'] and fights['creeper2']['fight_won'] and fights['wolf1']['fight_won']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['hat'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc2hit']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['snow'], screen)
        if self.talking_cooldown >= self.talking_wait + 175:
            self.talking = False
            self.talk = False
            dialog['d']['npc2hit'] = False
    elif dialog['d']['npc2line1']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['line1'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc2line2']:
        self.talking = True
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['line2'], screen)
        self.combat_cooldown += 1
        if self.combat_cooldown >= 50:
            self.creeper2 = True
            dialog['d']['npc2line2'] = False
            dialog['d']['npc2line3'] = True
            fights['creeper2']['fight_begun'] = True
            fights['creeper2']['fight_won'] = True
            self.combat_cooldown = 0
    elif dialog['d']['npc2line3']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['line3'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc2line4']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc2']['n'], dialog['npc2']['line4'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0

def npc3_dialog(self):
    dialog['d']['jackRun'] = False
    dialog['d']['npc2Run'] = False
    dialog['d']['npc4Run'] = False
    print(fights['creeper1']['fight_won'], fights['creeper2']['fight_won'], fights['wolf1']['fight_won'])
    if fights['creeper1']['fight_won'] and fights['creeper2']['fight_won'] and fights['wolf1']['fight_won']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc3']['n'], dialog['npc3']['hat'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc3hit']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc3']['n'], dialog['npc3']['snow'], screen)
        if self.talking_cooldown >= self.talking_wait + 175:
            self.talking = False
            self.talk = False
            dialog['d']['npc3hit'] = False
    elif dialog['d']['npc3line1']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc3']['n'], dialog['npc3']['line1'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc3line2']:
        self.talking = True
        renderTextCenteredAt(dialog['npc3']['n'], dialog['npc3']['line2'], screen)
        self.combat_cooldown += 1
        if self.combat_cooldown >= 50:
            self.creeper2 = True
            dialog['d']['npc3line2'] = False
            dialog['d']['npc3line3'] = True
            fights['wolf1']['fight_begun'] = True
            fights['wolf1']['fight_won'] = True
            self.combat_cooldown = 0
    elif dialog['d']['npc3line3']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc3']['n'], dialog['npc3']['line3'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc3line4']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc3']['n'], dialog['npc3']['line4'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
def npc4_dialog(self):
    dialog['d']['jackRun'] = False
    dialog['d']['npc2Run'] = False
    dialog['d']['npc3Run'] = False
    print(fights['creeper1']['fight_won'], fights['creeper2']['fight_won'], fights['wolf1']['fight_won'])
    if fights['creeper1']['fight_won'] and fights['creeper2']['fight_won'] and fights['wolf1']['fight_won']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc4']['n'], dialog['npc4']['hat'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc4hit']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc4']['n'], dialog['npc4']['snow'], screen)
        if self.talking_cooldown >= self.talking_wait + 175:
            self.talking = False
            self.talk = False
            dialog['d']['npc4hit'] = False
    elif dialog['d']['npc4line1']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc4']['n'], dialog['npc4']['line1'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc4line2']:
        self.talking = True
        renderTextCenteredAt(dialog['npc4']['n'], dialog['npc4']['line2'], screen)
        self.combat_cooldown += 1
        if self.combat_cooldown >= 50:
            dialog['d']['npc4line2'] = False
            dialog['d']['npc4line3'] = True
            fights['creeper1']['fight_begun'] = True
            fights['creeper1']['fight_won'] = True
            self.combat_cooldown = 0
    elif dialog['d']['npc4line3']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc4']['n'], dialog['npc4']['line3'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
    elif dialog['d']['npc4line4']:
        self.talking = True
        self.talking_cooldown += 1
        renderTextCenteredAt(dialog['npc4']['n'], dialog['npc4']['line4'], screen)
        if self.talking_cooldown >= self.talking_wait:
            self.end_talk = True
            self.talking_cooldown = 0
def end_conversation(self):
    if self.end_talk and dialog['d']['jackRun']:
        if dialog['d']['jackline1'] and not dialog['d']['jackline2']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['jackline2'] = True
            dialog['d']['jackline1'] = False
        elif dialog['d']['jackline2'] and not dialog['d']['jackline3'] and not dialog['d']['jackline4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['jackline3'] = True
            dialog['d']['jackline2'] = False
        elif dialog['d']['jackline3'] and not dialog['d']['jackline4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['jackline4'] = True
            dialog['d']['jackline3'] = False
        elif dialog['d']['jackline4']:
            dialog['d']['jackline4'] = False
            dialog['d']['jackline3'] = False
            dialog['d']['jackline2'] = True
            dialog['d']['jackline1'] = False
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
            dialog['d']['npc2Win'] = True
            dialog['d']['npc2line2'] = False
        elif dialog['d']['npc2line3'] and not dialog['d']['npc2line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc2line4'] = True
            dialog['d']['npc2line3'] = False
        elif dialog['d']['npc2line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc2line3'] = True
            dialog['d']['npc2line4'] = False
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
    if self.end_talk and dialog['d']['npc3Run']:
        if dialog['d']['npc3line1'] and not dialog['d']['npc3line2']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc3line2'] = True
            dialog['d']['npc3line1'] = False
        elif dialog['d']['npc3line2'] and not dialog['d']['npc3line3'] and not dialog['d']['npc3line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc3line3'] = True
            dialog['d']['npc3Win'] = True
            dialog['d']['npc3line2'] = False
        elif dialog['d']['npc3line3'] and not dialog['d']['npc3line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc3line4'] = True
            dialog['d']['npc3line3'] = False
        elif dialog['d']['npc3line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc3line3'] = True
            dialog['d']['npc3line4'] = False
    if self.end_talk and dialog['d']['npc4Run']:
        if dialog['d']['npc4line1'] and not dialog['d']['npc4line2']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc4line2'] = True
            dialog['d']['npc4line1'] = False
        elif dialog['d']['npc4line2'] and not dialog['d']['npc4line3'] and not dialog['d']['npc4line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc4line3'] = True
            dialog['d']['npc4Win'] = True
            dialog['d']['npc4line2'] = False
        elif dialog['d']['npc4line3'] and not dialog['d']['npc4line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc4line4'] = True
            dialog['d']['npc4line3'] = False
        elif dialog['d']['npc4line4']:
            self.talk = False
            self.talking = False
            self.end_talk = False
            dialog['d']['npc4line3'] = True
            dialog['d']['npc4line4'] = False
    self.cooldown = 0

