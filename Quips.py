# MISSION: PyTrek 2020.
# STATUS: Release
# VERSION: 1.0.0
# NOTES: See https://github.com/Python3-Training/PyTrek
# DATE: 2026-05-30 20:48:04
# FILE: Quips.py
# AUTHOR: See https://ko-fi.com/randallnagy
#
import random

DAMAGE_PREFIX = [
    "The main ",
    "That @#$#@& ",
    "Our cheap ",
    "Darn-it captain, that ",
    "Yikes, the ",
    ]
DAMAGE_SUFFIX = [
    " has died. We're on it!",
    " is out. We're working on it!",
    " is almost repaired!",
    " is dead.",
    " is fried. Working as fast as we can!",
    " is toast. Working as fast as I can!",
    " is being replaced.",
    " is dead. Please leave a message.",
    ]
DEFEAT_PREFIX = [
    "A defeated ",
    "The vengeful ",
    "An angry ",
    "The ejecting ",
    "A confused ",
    "Another ",
    "Yet another ",
    ]
DEFEAT_SUFFIX = [
    " says: `I'll be back!`",
    " cries: ... 'a lucky shot!'",
    " sighs bitterly.",
    " dies.",
    " is rescued.",
    " is history.",
    " is no more.",
    " is recycled.",
    " is eliminated.",
    " was aborted. Few lives, matter?",
    " ejects.",
    " crew is rescued.",
    " crew is spaced.",
    " crew is recycled.",
    " crew is recovered.",
    " yells: 'thy mother mates poorly!'",
    " snarls: 'lucky shot.'",
    " laughs: 'you'll not do THAT again!'",
    " says nothing.",
    " screams: 'thy father is a Targ!'",
    " yells: 'thine family eats bats!'",
    " snarls: 'thine people eat vermin!'",
    " curses: 'thy fathers spreadeth pox!'",
    " yells: 'thy mother is progressive!'",
    ]
MISTAKES = [
    "... the crew was not impressed ...",
    "... that's going to leave a mark ...",
    "... next time carry the 1?",
    "... math lives matter ...",
    "... its coming out of your pay ...",
    "... this is not a bumper car ...",
    "... life can be tough that way ...",
    "... who ordered THAT take-out?",
    "... random is, what random does ...",
    "... you've got their attention ...",
    "... next time, just text them?",
    "... how rude!",
    "... yes, karma CAN hurt ...",
    "... life is but a dream!",
    "... game over.",
    "... starfleet will talk about this for years.",
    "... who is going to pay for that?",
    "... galactic insurance premiums skyrocket ...",
    "... captain goes down with the starship ...",
    "... we'll notify your next-of-kin.",
    "... that was not in the script ...",
    "... you never did THAT in the simulator ...",
    ]

QUITS = [
    "-Let's call it a draw?",
    "-You call yourself a 'Trekkie?",
    "Kobayashi Maru. Python for you?",
    "(Spock shakes his head)",
    "(Duras, stop laughing!)",
    "(... and the Klingons rejoice)",
    "(... and our enemies, rejoice)",
    "Kobayashi Maru... Got Python?",
    "(Kirk shakes his head)",
    ]

class Quips():
    
    @staticmethod
    def jibe(noun, prefix, suffix):
        prand = random.randrange(0, len(prefix))
        srand = random.randrange(0, len(suffix))
        return prefix[prand] + noun + suffix[srand]

    @staticmethod
    def jibe_quit():
        return QUITS[random.randrange(0, len(QUITS))]
    
    @staticmethod
    def jibe_damage(noun):
        if random.randrange(0, 100) > 25:
            return f"{noun.capitalize()} damaged. Repairs are underway."
        return Quips.jibe(noun, DAMAGE_PREFIX, DAMAGE_SUFFIX)
    
    @staticmethod
    def jibe_defeat(noun):
        if random.randrange(0, 100) > 25:
            return f"Another {noun.lower()} defeated."
        return Quips.jibe(noun, DEFEAT_PREFIX, DEFEAT_SUFFIX)
    
    @staticmethod
    def jibe_fatal_mistake():
        return MISTAKES[random.randrange(0, len(MISTAKES))]





