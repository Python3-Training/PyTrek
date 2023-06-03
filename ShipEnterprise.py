import random
from PyTrek.AbsShip import AbsShip
from PyTrek.ShipStarbase import ShipStarbase
from PyTrek.Sector import Sector
from PyTrek.Difficulity import Probabilities
from PyTrek import Glyphs as Glyphs
from PyTrek.Quips import Quips as Quips

class ShipEnterprise(AbsShip):

    def __init__(self):
        super().__init__()
        self.energy = 0
        self.docked = False
        self.condition = "GREEN"
        self.navigation_damage = 0
        self.short_range_scan_damage = 0
        self.long_range_scan_damage = 0
        self.shield_control_damage = 0
        self.computer_damage = 0
        self.photon_damage = 0
        self.phaser_damage = 0
        self.photon_torpedoes = 0
        ShipStarbase.dock_enterprise(self)
        ShipStarbase.launch_enterprise(self)

    def get_glyph(self):
        return Glyphs.ENTERPRISE

    def damage(self, game, item):
        '''
        Damage the Enterprise.
        '''
        if not Probabilities.should_damage_enterprise(game, item):
            return
        damage = Probabilities.calc_damage(game, item)
        if item < 0:
            item = random.randint(0, 6)
        if item == 0:
            self.navigation_damage = damage
            game.display(Quips.jibe_damage('warp engine'))
        elif item == 1:
            self.short_range_scan_damage = damage
            game.display(Quips.jibe_damage('short range scanner'))
        elif item == 2:
            self.long_range_scan_damage = damage
            game.display(Quips.jibe_damage('long range scanner'))
        elif item == 3:
            self.shield_control_damage = damage
            game.display(Quips.jibe_damage('shield control'))
        elif item == 4:
            self.computer_damage = damage
            game.display(Quips.jibe_damage('main computer'))
        elif item == 5:
            self.photon_damage = damage
            game.display(Quips.jibe_damage('torpedo controller'))
        elif item == 6:
            self.phaser_damage = damage
            game.display(Quips.jibe_damage('phaser'))
        game.display()

    def repair(self, game):
        '''
        Repair damage to the Enterprise.
        '''
        if self.navigation_damage > 0:
            self.navigation_damage -= 1
            if self.navigation_damage == 0:
                game.display("Warp engines have been repaired.")
            game.display()
            return True
        if self.short_range_scan_damage > 0:
            self.short_range_scan_damage -= 1
            if self.short_range_scan_damage == 0:
                game.display("Short range scanner has been repaired.")
            game.display()
            return True
        if self.long_range_scan_damage > 0:
            self.long_range_scan_damage -= 1
            if self.long_range_scan_damage == 0:
                game.display("Long range scanner has been repaired.")
            game.display()
            return True
        if self.shield_control_damage > 0:
            self.shield_control_damage -= 1
            if self.shield_control_damage == 0:
                game.display("Shield controls have been repaired.")
            game.display()
            return True
        if self.computer_damage > 0:
            self.computer_damage -= 1
            if self.computer_damage == 0:
                game.display("The main computer has been repaired.")
            game.display()
            return True
        if self.photon_damage > 0:
            self.photon_damage -= 1
            if self.photon_damage == 0:
                game.display("Photon torpedo controls have been repaired.")
            game.display()
            return True
        if self.phaser_damage > 0:
            self.phaser_damage -= 1
            if self.phaser_damage == 0:
                game.display("Phasers have been repaired.")
            game.display()
            return True
        return False

    def short_range_scan(self, game):
        if self.short_range_scan_damage > 0:
            game.display(Quips.jibe_damage('short ranged scanner'))
            game.display()
        else:
            quad = game.game_map.get_pw_sector()
            Sector.display_area(game, quad)
        game.display()
        if not game.enterprise.repair(game):
            game.enterprise.damage(game, Probabilities.SRS)

    def long_range_scan(self, game):
        if self.long_range_scan_damage > 0:
            game.display(Quips.jibe_damage('long ranged scanner'))
            game.display()
            return

        pw_sector = game.game_map.sector
        if pw_sector < 4:
            pw_sector = 5
        elif pw_sector > 60:
            pw_sector = 60
        lines = []
        for peek in range(pw_sector-4, pw_sector + 5):
            quad = game.game_map.scan_sector(peek)
            lines.append(f"SEC: {quad.number:>03}")
            lines.append(f"{Glyphs.KLINGON}: {quad.area_klingons:>03}")
            lines.append(f"{Glyphs.STARBASE}: {quad.area_starbases:>03}")
            lines.append(f"{Glyphs.STAR}: {quad.area_stars:>03}")
        dots = '     +' + ('-' * 35) + '+'
        game.display(dots)
        game.display('     |          LONG RANGE SCAN          |')
        game.display(dots)
        for ss in range(0,(len(lines)-1),12):
            for offs in range(4):
                line = f'     | {lines[ss+offs]:<9} | {lines[ss+4+offs]:<9} | {lines[ss+8+offs]:<9} |'
                game.display(line)
            game.display(dots)
        game.display()
        if not game.enterprise.repair(game):
            game.enterprise.damage(game, Probabilities.SRS)

