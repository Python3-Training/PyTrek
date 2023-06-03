import random
import PyTrek.Glyphs as Glyphs
from PyTrek.AbsShip import AbsShip as AbsShip

class ShipKlingon(AbsShip):

    def __init__(self):
        super().__init__()
        self.xpos = 0
        self.ypos = 0
        self.shield_level = 0

    def get_glyph(self):
        return Glyphs.KLINGON

    def from_map(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.shield_level = random.randint(300, 599)

    @staticmethod
    def attack_if_you_can(game):
        '''
        IF you ever find yourself in the AREA, then have at USS?
        '''
        if game.is_cloked:
            return False
        from PyTrek.Calculators import Calc as Calc
        kships = game.game_map.get_area_klingons()
        if len(kships) > 0:
            for ship in kships:
                if game.enterprise.docked:
                    game.display("Enterprise hit by ship at sector [{0},{1}]. No damage due to starbase shields.".format(
                        ship.xpos + 1, ship.ypos + 1
                    ))
                else:
                    dist = Calc.distance(
                        game.game_map.xpos, game.game_map.ypos, ship.xpos, ship.ypos)
                    delivered_energy = 300 * \
                        random.uniform(0.0, 1.0) * (1.0 - dist / 11.3)
                    game.enterprise.shield_level -= int(delivered_energy)
                    if game.enterprise.shield_level < 0:
                        game.enterprise.shield_level = 0
                        game.destroyed = True
                    game.display("Enterprise hit by ship at sector [{0},{1}]. Shields dropped to {2}.".format(
                        ship.xpos + 1, ship.ypos + 1, game.enterprise.shield_level
                    ))
                    if game.enterprise.shield_level == 0:
                        return True
            return True
        return False
