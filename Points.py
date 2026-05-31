# MISSION: PyTrek 2020.
# STATUS: Release
# VERSION: 1.0.0
# NOTES: See https://github.com/Python3-Training/PyTrek
# DATE: 2026-05-30 20:48:04
# FILE: Points.py
# AUTHOR: See https://ko-fi.com/randallnagy
#
class WarpDest():
    ''' Warp Speed: 
    One's based GALAXY navigation.
    Guaranteed SAFE placement.
    '''
    def __init__(self, sector=-1, warp=0):
        if sector > 64: sector = 64 # zOuter Limits =)
        if warp > 10: warp = 10
        if warp < 0:  warp = 0
        self.warp = warp
        self.sector = sector

    @staticmethod
    def parse(dest, sep=','):
        '''
        Parse: sector-num, speed-float - None on error
        Example: 5,1.1 
        '''
        dest = str(dest)
        cols = dest.split(sep)
        if len(cols) == 2:
            try:
                sector = int(cols[0].strip())
                if sector < 1:
                    sector = 1
                speed = float(cols[1].strip())
                if speed < 0: speed = 0.1
                if speed > 9: speed = 9.0
                return WarpDest(sector, speed)
            except:
                pass
        return None


class SubDest():
    ''' Sublight Navigation:
    Zero based, AREA placement.
    Caveat, User! ;-)
    '''
    def __init__(self, xpos=-1, ypos=-1):
        if xpos > 7:  xpos = 7
        if ypos > 7:  ypos = 7
        if xpos < 0:  xpos = 0
        if ypos < 0:  ypos = 0
        self.xpos = xpos
        self.ypos = ypos

    @staticmethod
    def parse(dest, sep=','):
        '''
        WARNING: USER 1's -> 0-BASED TRANSLATION HERE

        Parse: [a-h], ypos 
                or 
                #,#  
           Return None on error
        Example: b,5 
        '''
        dest = str(dest)
        cols = dest.split(sep)
        if len(cols) == 2:
            try:
                alph = cols[0].strip().lower()[0]
                num = 0
                if alph.isalpha():
                    num = ord(alph) - 96 # 'a' == 1
                else:
                    num = int(alph)
                xpos = num
                ypos = int(cols[1].strip()[0])
                return SubDest(xpos-1, ypos-1)
            except:
                pass
        return None


class Dest(WarpDest, SubDest):

    def __init__(self):
        WarpDest.__init__(self)
        SubDest.__init__(self)

    def is_null(self):
        return self.xpos == 0 and \
            self.sector == -1

    def clone(self):
        result = Dest()
        result.xpos = self.xpos
        result.ypos = self.ypos
        result.sector = self.sector
        result.warp = self.warp
        return result


if __name__ == '__main__':
    test = Dest()
    assert(test.is_null() == True)
    test.xpos = test.ypos = 123
    test.sector = 22
    test.warp = 22
    assert(test.is_null() == False)
    clone = test.clone()
    assert(clone.sector == test.sector)
    assert(clone.warp == test.warp)
    assert(clone.xpos == test.xpos)
    assert(clone.ypos == test.ypos)

