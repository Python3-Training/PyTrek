from math import sqrt
import random

from PyTrek.MapGame import *
from PyTrek.AbsShip import *
from PyTrek.Points import *
from PyTrek.Difficulity import Probabilities

class Calc():

    @staticmethod
    def surrounding(pos):
        '''
        Return the complete set of
        points surrounding a piece.
        Sanity checking is not performed.
        '''
        results = []
        if pos:
            above = pos.ypos - 1
            below = pos.ypos + 1
            left  = pos.xpos - 1
            right = pos.xpos + 1
            results.append([left, above])
            results.append([right, below])
            results.append([left, below])
            results.append([right, above])
            results.append([pos.xpos, above])
            results.append([pos.xpos, below])
            results.append([left, pos.ypos])
            results.append([right, pos.ypos])
        return results

    @staticmethod
    def distance(x1, y1, x2, y2):
        x = x2 - x1
        y = y2 - y1
        return sqrt(x * x + y * y)

    @staticmethod
    def sublight_navigation(game):
        dest_sys = game.read_xypos()
        if not dest_sys:
            game.display("Invalid course.")
            game.display()
            return


        dist = Calc.distance(game.game_map.xpos, game.game_map.ypos,
                             dest_sys.xpos, dest_sys.ypos)
        energy_required = int(dist)
        if energy_required >= game.enterprise.energy:
            game.display("Insufficient energy move to that location.")
            game.display()
            return

        game.display()
        game.display("Sub-light engines engaged.")
        game.enterprise.energy -= energy_required
        game.display()
        game.move_to(dest_sys)

        game.time_remaining -= 1
        game.star_date += 1

        game.enterprise.short_range_scan(game)

        if game.enterprise.docked:
            game.display("Lowering shields as part of docking sequence...")
            game.display("Enterprise successfully docked with starbase.")
            game.display()
        else:
            if game.game_map.count_area_klingons() > 0:
                ShipKlingon.attack_if_you_can(game)
                game.display()
            elif not game.enterprise.repair(game):
                game.enterprise.damage(game, Probabilities.LRS)

    @staticmethod
    def warp_navigation(game):
        if game.enterprise.navigation_damage > 0:
            max_warp_factor = 0.2 + random.randint(0, 8) / 10.0
            game.display(f"Warp engines damaged. Maximum warp factor: {max_warp_factor}")
            game.display()

        dest_sys = game.read_sector()
        if not dest_sys:
            game.display("Invalid course.")
            game.display()
            return

        game.display()

        if dest_sys.warp < 1:
            dest_sys.warp = 1

        dist = dest_sys.warp * 8
        energy_required = int(dist)
        if energy_required >= game.enterprise.energy:
            game.display("Insufficient energy to travel at that speed.")
            game.display()
            return
        else:
            game.display("Warp engines engaged.")
            game.display()
            game.enterprise.energy -= energy_required

        n = lambda dist, speed: round(0.5 + speed/dist) #Quick calculator for time passage

        game.time_remaining -= n(abs(game.game_map.sector - dest_sys.sector),dest_sys.warp) # before moving there, adjust time by lambda calc
        game.star_date += n(abs(game.game_map.sector - dest_sys.sector),dest_sys.warp)

        game.move_to(dest_sys)

        game.enterprise.short_range_scan(game)

        if game.enterprise.docked:
            game.display("Lowering shields as part of docking sequence...")
            game.display("Enterprise successfully docked with starbase.")
            game.display()
        else:
            if game.game_map.count_area_klingons() > 0:
                ShipKlingon.attack_if_you_can(game)
                game.display()
            elif not game.enterprise.repair(game):
                game.enterprise.damage(game, Probabilities.RANDOM)


    @staticmethod
    def show_starbase(game):
        game.display()
        bases = game.game_map.get_all(Glyphs.STARBASE)
        game.display()
        if bases:
            game.display("Starbases:")
            for info in bases:
                area = info[0]; base = info[1]
                game.display(f"\tSector #{area.number} at [{base.xpos},{base.ypos}].")
        else:
            game.display("There are no Starbases.")
        game.display()


    @staticmethod
    def show_torp_targets(game):
        game.display()
        kships = game.game_map.get_area_klingons()
        if len(kships) == 0:
            game.display("There are no enemies in this sector.")
            return

        game.display("Enemies:")
        for ship in kships:
            game.display(f"\tKlingon [{ship.xpos},{ship.ypos}].")
        game.display()

