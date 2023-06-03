from PyTrek import Glyphs as Glyphs
from PyTrek.Quips import Quips as Quips

class Stats():
    '''
    Reports do not generate damage.
    '''
    @staticmethod
    def show_ship_status(game):
        game.display()
        game.display(f"               Time Remaining: {game.time_remaining}")
        game.display(f"      Klingon Ships Remaining: {game.game_map.game_klingons}")
        game.display(f"                    Starbases: {game.game_map.game_starbases}")
        game.display(f"           Warp Engine Damage: {game.enterprise.navigation_damage}")
        game.display(f"   Short Range Scanner Damage: {game.enterprise.short_range_scan_damage}")
        game.display(f"    Long Range Scanner Damage: {game.enterprise.long_range_scan_damage}")
        game.display(f"       Shield Controls Damage: {game.enterprise.shield_control_damage}")
        game.display(f"         Main Computer Damage: {game.enterprise.computer_damage}")
        game.display(f"Photon Torpedo Control Damage: {game.enterprise.photon_damage}")
        game.display(f"                Phaser Damage: {game.enterprise.phaser_damage}")
        game.display()

    @staticmethod
    def show_galactic_status(game):
        game.display()
        str_ = f"| KLINGONS: {game.game_map.game_klingons:>04} | " + \
               f"STARBASES: {game.game_map.game_starbases:>04} | " + \
               f"STARS: {game.game_map.game_stars:>04} |"
        dots = len(str_) * '-'
        game.display(dots)
        game.display(str_)
        game.display(dots)

    @staticmethod
    def show_exit_status(game):
        if game.destroyed:
            msg = "MISSION FAILED: SHIP DESTROYED"
            game.show_banner([msg], '!')
        elif game.enterprise.energy == 0:
            msg = "MISSION FAILED: OUT OF ENERGY."
            game.show_banner([msg], '!')
        elif game.game_map.game_klingons == 0:
            msg = "MISSION ACCOMPLISHED","ENEMIES DESTROYED","WELL DONE!"
            game.show_banner(msg)
        elif game.time_remaining == 0:
            msg = "MISSION FAILED: OUT OF TIME."
            game.show_banner([msg], '!')
        else:
            ary = ["::::::::: MISSION ABORTED :::::::::", Quips.jibe_quit()]
            game.show_banner(ary, ':')

