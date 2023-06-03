import random
import PyTrek.MapGame as MapGame
import PyTrek.Glyphs as Glyphs
from PyTrek.MapSparse import SparseMap as SparseMap

def fill_map():
    map = SparseMap()
    map.init()
    for sector in range(1, 65):
        for xpos in range(8):
            for ypos in range(8):
                assert(map.plot(sector,xpos,ypos,Glyphs.ENTERPRISE))
    return map

def define_map():
    map = SparseMap()
    map.init()
    for ypos, area in enumerate(range(8)):
        for xpos, area in enumerate(range(8)):
            which = random.randint(0, 14)
            glyph = Glyphs.SPACE
            if which < 0:
                pass
            elif which < 8:
                glyph = Glyphs.STAR
            elif which < 13:
                glyph = Glyphs.STARBASE
            else:
                glyph = Glyphs.KLINGON

            map.plot(area, 
                     random.randint(0, 7), 
                     random.randint(0, 7),
                     glyph)
    return map

if __name__ == '__main__':
    map = fill_map()
    for sect, area in enumerate(map.areas(),1):
        assert(area.number == sect)

    for sector in map.areas():
        for line in sector.get_map():
            print(line, end='')
        print()





