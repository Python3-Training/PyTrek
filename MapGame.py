import random
import PyTrek.TrekStrings as TrekStrings

from PyTrek import Glyphs as Glyphs
from PyTrek.ShipKlingon import ShipKlingon as ShipKlingon
from PyTrek.Points import *
from PyTrek.Sector import Sector as Sector
from PyTrek.ErrorCollision import ErrorEnterpriseCollision as ErrorEnterpriseCollision

import PyTrek.MapSparse as MapSparse

class GameMap(MapSparse.SparseMap):

    def __init__(self):
        '''
        Prepare a 'Trekian GameMap for future 
        initialization.
        '''
        super().__init__()
        self.sector = -1
        self.xpos = self.ypos = -1
        self.game_stars      = -1
        self.game_klingons   = -1
        self.game_starbases  = -1
        self.last_nav = Dest()
        
    def place(self, takers):
        ''' 
        Randomly place game-objects, into the map.
        '''
        if not sum(takers):
            return None
        takers =list(takers)
        for which, nelem in enumerate(takers):
            if not nelem:
                continue
            to_take = random.randint(0, nelem)
            if nelem == 1:
                to_take = 1
            if not to_take:
                continue
            taken = 0
            while taken != to_take:
                ss = random.randrange(1, 64) # Ignore "Outer Limits"
                area = self.get_area(ss)
                should_take = random.randint(1, 8)
                if which == 0:
                    if area.count_glyphs(Glyphs.STARBASE) != 0:
                        continue
                    area.place_glyph(Glyphs.STARBASE)
                elif which == 1:
                    area.place_glyph(Glyphs.STAR)
                elif which == 2:
                    if area.count_glyphs(Glyphs.KLINGON) > 3:
                        continue
                    area.place_glyph(Glyphs.KLINGON)
                taken += 1
                if taken == to_take:
                    break;
            takers[which] -= taken
        return tuple(takers)

    def enterprise_in(self, dest=None):
        ''' 
        Place the ENTERPRISE at the destination, else a 
        random one.
        
        Will raise an ErrorEnterpriseCollision, upon same.

        Returns the final x, y location upon success 
        '''
        area = self.pw_area()
        if not dest:
            return area.place_glyph(Glyphs.ENTERPRISE)
        berror = False
        if area:
            for p in area._pieces:
                if p.xpos == dest.xpos and p.ypos == dest.ypos:
                    pos = area.place_glyph(Glyphs.ENTERPRISE)
                    berror = p.glyph
            pos = area.place_glyph(Glyphs.ENTERPRISE, dest)
            if berror:
                raise ErrorEnterpriseCollision(berror)
            if pos:
                return pos
        return False

    def enterprise_location(self):
        ''' 
        Get Enterprise location. False if not found. 
        '''
        area = self.pw_area()
        if area:
            for obj in area._pieces:
                if obj.glyph == Glyphs.ENTERPRISE:
                    return obj.xpos, obj.ypos
        return False

    def enterprise_out(self)->None:
        ''' 
        Remove the ENTERPRISE from the present AREA 
        '''
        pos = self.enterprise_location()
        if pos:
            self.clear_area(*pos)

    def place_glyph(self, glyph, dest=None)->bool:
        ''' 
        Place the glyph at the destination, else a random one 
        '''
        area = self.pw_area()
        if area:
            pos = area.place_glyph(self, glyph, dest)
            if pos:
                return True
        return False

    def clear_area(self, xpos, ypos)->None:
        ''' 
        Remove ANYTHING from the present AREA 
        '''
        area = self.pw_area()
        if area:
            area.remove(xpos, ypos)

    def pw_area(self)->MapSparse.SparseMap.Area:
        ''' 
        Return the internal / sparsely populated AREA object.
        Return an empty / default AREA upon coordinate error.
        '''
        if self.sector > 0:
            for area in self.areas():
                if area.number == self.sector:
                    return area
        return MapSparse.SparseMap.Area()

    def scan_sector(self, sector)->Sector:
        '''
        Return Sector() information (e.g. LRS) for a specific AREA.
        Return empty Sector() upon error.
        '''
        area = self.get_area(sector)
        if area:
            return Sector.from_area(area)
        return Sector()

    def count_area_klingons(self)->int:
        '''
        How many surround, U.S.S?
        '''
        return self._count_area(Glyphs.KLINGON)

    def count_area_starbases(self)->int:
        '''
        How many surround, U.S.S?
        '''
        return self._count_area(Glyphs.STARBASE)

    def count_area_stars(self)->int:
        '''
        How many surround, U.S.S?
        '''
        return self._count_area(Glyphs.STAR)

    def _count_area(self, glyph)->int:
        ''' 
        Tally the number of glyphs in the DEFAULT AREA 
        '''
        count = 0
        area = self.pw_area()
        if area:
            for obj in area._pieces:
                if obj.glyph == glyph:
                    count += 1
        return count

    def update_counts(self)->None:
        '''
        Update this map's official game-pieces-in-play tally
        '''
        self.game_klingons = self.game_starbases = self.game_stars = 0
        for area in self.areas():
            self.game_klingons  += area.count_glyphs(Glyphs.KLINGON)
            self.game_starbases += area.count_glyphs(Glyphs.STARBASE)
            self.game_stars     += area.count_glyphs(Glyphs.STAR)

    def remove_area_items(self, piece_array)->None:
        '''
        Remove a collection of pieces (e.g. ships), 
        from the PRESENT / default AREA.
        '''
        area = self.pw_area()
        for obj in piece_array:
            area.remove(obj.xpos, obj.ypos)
        self.update_counts()

    def get_area_klingons(self)->list:
        '''
        Return this Area's data for Kingons, in an array.
        '''
        results = []
        area = self.pw_area()
        for data in area.query(Glyphs.KLINGON):
            ship = ShipKlingon()
            ship.from_map(data.xpos, data.ypos)
            results.append(ship)
        return results

    def get_area_objects(self)->list:
        '''
        Return the actual pieces, as maintained in the Area. 
        WARNING: Changes to this collection WILL update Area
        content.
        '''
        area = self.pw_area()
        return area._pieces

    def get_game_id(self, piece)->str:
        '''
        Uniquely identify a game piece / object.
        '''
        area = self.pw_area()
        num = (area.number * 100) + (piece.ypos * 8) + piece.xpos
        return f"{piece.glyph[1]}x{num}"

    def get_all(self, glyph)->list:
        '''
        Return [ [AREA, PIECE], ... ] for every glyph found.
        '''
        results = []
        for area in self.areas():
            for piece in area.query(glyph):
                results.append([area, piece])
        return results

    def get_pw_sector(self)->Sector:
        '''
        Create a Sector() report for the DEFAULT AREA
        '''
        area = self.pw_area()
        return Sector.from_area(area)

    def get_map(self)->list:
        ''' 
        Generate AREA map of the present sector.
        '''
        area = self.pw_area()
        return area.get_map()

    def _go_to(self, dest):
        ''' 
        Either a WARP ~or~ a SUBSPACE destination is ok.
        Place the main player (Enterprise, for now) into the Area.
        Returns the final, effective, arrival Dest().
        '''
        if not dest:
            return
        if not self.last_nav.is_null():
            self.enterprise_out()
        pos = None
        if isinstance(dest, WarpDest):
            if dest.sector > 0:
                self.sector = dest.sector
            dest.sector = self.sector
            pos = self.enterprise_in() # SAFE WARP-IN!
            self.last_nav.sector = dest.sector
            self.last_nav.warp = dest.warp
        else:
            if dest.xpos != -1:
                self.xpos = dest.xpos
                self.ypos = dest.ypos
            dest.xpos = self.xpos
            dest.ypos = self.ypos
            pos = self.enterprise_in(dest) # CAPIN' KNOWS BEST?
            dest.xpos = pos[0]
            dest.ypos = pos[1]
        self.xpos = pos[0]
        self.ypos = pos[1]
        self.last_nav.xpos = pos[0]
        self.last_nav.ypos = pos[1]
        return self.last_nav.clone()

    def randomize(self, bases=None, stars=None, aliens=None)->None:
        '''
        Randomly place the inventoried items into the map.
        If no bases ot aliens are specified, a random number
        will be selected. Stars are not required. Not having 
        any stars is ok.
        '''
        if not aliens:
            aliens = random.randint(5, 10)
        if not bases:
            bases = random.randint(2, 4)
        self.game_starbases = bases
        self.game_klingons = aliens
        self.game_stars = stars
        self.init()
        takers = bases, stars, aliens
        while takers:
            for lrs in self._map:
                takers = self.place(takers)
                if not takers:
                    break



