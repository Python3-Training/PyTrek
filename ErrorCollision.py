# MISSION: PyTrek 2020.
# STATUS: Release
# VERSION: 1.0.0
# NOTES: See https://github.com/Python3-Training/PyTrek
# DATE: 2026-05-30 20:48:04
# FILE: ErrorCollision.py
# AUTHOR: See https://ko-fi.com/randallnagy
#
class ErrorEnterpriseCollision(Exception):
    '''
    ... because some problems simply have to wait ... =)
    '''
    def __init__(self, glyph):
        super().__init__()
        self.glyph = glyph


