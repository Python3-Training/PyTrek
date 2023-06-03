import random

from PyTrek import TrekStrings
from PyTrek import Glyphs
from PyTrek.ShipKlingon import ShipKlingon
from PyTrek.ShipEnterprise import ShipEnterprise
from PyTrek.Calculators import Calc
from PyTrek.Reports import Stats
from PyTrek.Quips import Quips
from PyTrek.Difficulity import Probabilities

class Control():

    @staticmethod
    def computer(game):
        if game.enterprise.computer_damage > 0:
            game.display(Quips.jibe_damage('computer'))
            game.display()
            return
        game.show_strings(TrekStrings.CPU_CMDS)
        command = game.read("Enter computer command: ").strip().lower()
        if command == "rec":
            Stats.show_galactic_status(game)
        elif command == "sta":
            Stats.show_ship_status(game)
        elif command == "tor":
            Calc.show_torp_targets(game)
        elif command == "bas":
            Calc.show_starbase(game)
        else:
            game.display()
            game.display("Invalid computer command.")
            game.display()
        game.enterprise.damage(game, Probabilities.COMPUTER)


    @staticmethod
    def phasers(game):
        if game.enterprise.phaser_damage > 0:
            game.display(Quips.jibe_damage("phaser"))
            game.display()
            return
        kships = game.game_map.get_area_klingons()
        if len(kships) == 0:
            game.display("There are no Klingon ships in this sector.")
            game.display()
            return
        game.display("Phasers locked on target.")
        phaser_energy = game.read_double("Enter phaser energy (1--{0}): ".format(game.enterprise.energy))
        if not phaser_energy or phaser_energy < 1 or phaser_energy > game.enterprise.energy:
            game.display("Invalid energy level.")
            game.display()
            return
        game.display()
        game.display("Firing phasers...")
        destroyed_ships = []
        for ss, ship in enumerate(kships):
            game.enterprise.energy -= int(phaser_energy)
            if game.enterprise.energy < 0:
                game.enterprise.energy = 0
                break
            dist = Calc.distance(game.game_map.xpos, 
                                 game.game_map.ypos, 
                                 ship.xpos, ship.ypos)
            delivered_energy = phaser_energy * (1.0 - dist / 11.3)
            ship.shield_level -= int(delivered_energy)
            if ship.shield_level <= 0:
                game.display(f"Enemy ship destroyed at [{ship.xpos + 1},{ship.ypos + 1}].")
                game.display(Quips.jibe_defeat('enemy'))
                destroyed_ships.append(ship)
            else:
                game.display(f"Hit ship at [{ship.xpos + 1},{ship.ypos + 1}].")
                game.display(f"Enemy shield down to {ship.shield_level}.")
        game.game_map.remove_area_items(destroyed_ships)
        if game.game_map.count_area_klingons() > 0:
            game.display()
            ShipKlingon.attack_if_you_can(game)
        game.display()
        game.enterprise.damage(game, Probabilities.PHASERS)


    def shields(game):
        game.display("--- Shield Controls ----------------")
        game.display("add = Add energy to shields.")
        game.display("sub = Subtract energy from shields.")
        game.display()
        command = game.read("Enter shield control command: ").strip().lower()
        game.display()
        if command == "add":
            adding = True
            max_transfer = game.enterprise.energy
        elif command == "sub":
            adding = False
            max_transfer = game.enterprise.shield_level
        else:
            game.display("Invalid command.")
            game.display()
            return
        transfer = game.read_double(
            "Enter amount of energy (1--{0}): ".format(max_transfer))
        if not transfer or transfer < 1 or transfer > max_transfer:
            game.display("Invalid amount of energy.")
            game.display()
            return
        game.display()
        if adding:
            game.enterprise.energy -= int(transfer)
            game.enterprise.shield_level += int(transfer)
        else:
            game.enterprise.energy += int(transfer)
            game.enterprise.shield_level -= int(transfer)
        game.display("Shield strength is now {0}. Energy level is now {1}.".format(game.enterprise.shield_level, game.enterprise.energy))
        game.display()
        game.enterprise.damage(game, Probabilities.SHIELDS)


    def torpedos(game):
        if game.enterprise.photon_damage > 0:
            game.display(Quips.jibe_damage('photon launcher'))
            game.display()
            return
        if game.enterprise.photon_torpedoes == 0:
            game.display("Photon torpedoes exhausted.")
            game.display()
            return
        if game.game_map.count_area_klingons() == 0:
            game.display("There are no Klingon ships in this sector.")
            game.display()
            return
        shot = game.read_xypos()
        if not shot:
            game.display("Invalid shot.")
            game.display()
            return
        game.display()
        game.display("Photon torpedo fired...")
        game.enterprise.photon_torpedoes -= 1
        hit = False
        for ship in game.game_map.get_area_objects():
            if game.is_testing:
                print(f'{ship.glyph}({ship.xpos},{ship.ypos}), shot({shot.xpos},{shot.ypos})')
            if ship.xpos == shot.xpos and ship.ypos == shot.ypos:
                if ship.glyph == Glyphs.KLINGON:
                    num = game.game_map.get_game_id(ship)
                    game.display(f"Klingon ship #{num} destroyed.")
                    game.display(Quips.jibe_defeat('enemy'))
                    game.game_map.remove_area_items([ship])
                    hit = True
                    break
                elif ship.glyph == Glyphs.STARBASE:
                    game.game_map.game_starbases -= 1
                    num = game.game_map.get_game_id(ship)
                    game.display("Federation Starbase #{num} destroyed!")
                    game.display(Quips.jibe_defeat('commander'))
                    game.game_map.remove_area_items([ship])
                    hit = True
                    break
                elif ship.glyph == Glyphs.STAR:
                    num = game.game_map.get_game_id(ship)
                    game.display(f"Torpedo vaporizes star #{num}!")
                    game.display(Quips.jibe_defeat('academic'))
                    game.game_map.remove_area_items([ship])
                    hit = True
                    break
        if not hit:
            game.display("Torpedo missed.")
        if game.game_map.count_area_klingons() > 0:
            game.display()
            ShipKlingon.attack_if_you_can(game)
        game.display()
        game.enterprise.damage(game, Probabilities.PHOTON)

