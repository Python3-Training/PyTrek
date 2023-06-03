import abc
import random

from PyTrek9000 import Glyphs as Glyphs
from PyTrek9000.Quips import Quips as Quips
from PyTrek9000.Sector import Sector as Sector

class AbsShip(abc.ABC):
    ''' The first step, into a much larger universe ... '''

    def __init__(self):
        self.shield_level = 0

    @abc.abstractmethod
    def get_glyph(self):
        pass

