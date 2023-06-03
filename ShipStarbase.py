import PyTrek.Glyphs as Glyphs
from PyTrek.AbsShip import AbsShip as AbsShip

class ShipStarbase(AbsShip):

    def __init__(self):
        super().__init__()

    def get_glyph(self):
        return Glyphs.STARBASE

    @staticmethod
    def dock_enterprise(ship):
        ship.energy = 3000
        ship.photon_torpedoes = 10
        ship.navigation_damage = 0
        ship.short_range_scan_damage = 0
        ship.long_range_scan_damage = 0
        ship.shield_control_damage = 0
        ship.computer_damage = 0
        ship.photon_damage = 0
        ship.phaser_damage = 0
        ship.shield_level = 0
        ship.docked = True

    @staticmethod
    def launch_enterprise(ship):
        ship.docked = False
