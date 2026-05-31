# MISSION: PyTrek 2020.
# STATUS: Release
# VERSION: 1.0.0
# NOTES: See https://github.com/Python3-Training/PyTrek
# DATE: 2026-05-30 20:48:04
# FILE: Difficulity.py
# AUTHOR: See https://ko-fi.com/randallnagy
#
import random

class Probabilities:
    '''
    Extracting allows for easier customization.
    '''
    _LEVEL  = 4    
    RANDOM  = -1
    NAV     = 0
    SRS     = 1
    LRS     = 2
    SHIELDS = 3
    COMPUTER = 4
    PHOTON   = 5
    PHASERS  = 6

    @staticmethod
    def set_difficulity(game, level):
        '''
        The HIGHER the level, the MORE difficult 
        the game will be. 0 = EASY, 6 = HIGHEST
        '''
        if level < 0: level = 0
        if level > 6: level = 6
        Probabilities._LEVEL = level

    @staticmethod
    def calc_damage(game, item):
        '''
        How mch damage?
        '''
        return random.randint(1, 3)

    @staticmethod
    def should_damage_enterprise(game, item):
        '''
        Should we damage?
        Lowest level (above) eliminates damage to ITEM
        '''
        if game.is_testing:
            return False
        if item == Probabilities.SHIELDS:
            return False
        if random.randint(0, 6) < Probabilities._LEVEL:
            return True
        return False



