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

