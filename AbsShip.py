# MISSION: PyTrek 2020.
# STATUS: Release
# VERSION: 1.0.0
# NOTES: See https://github.com/Python3-Training/PyTrek
# DATE: 2026-05-30 20:48:04
# FILE: AbsShip.py
# AUTHOR: See https://ko-fi.com/randallnagy
#
import abc
import random

from PyTrek import Glyphs as Glyphs
from PyTrek.Quips import Quips as Quips
from PyTrek.Sector import Sector as Sector

class AbsShip(abc.ABC):
    ''' The first step, into a much larger universe ... '''

    def __init__(self):
        self.shield_level = 0

    @abc.abstractmethod
    def get_glyph(self):
        pass

