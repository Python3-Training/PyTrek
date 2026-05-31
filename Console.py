# MISSION: PyTrek 2020.
# STATUS: Release
# VERSION: 1.0.0
# NOTES: See https://github.com/Python3-Training/PyTrek
# DATE: 2026-05-30 20:48:04
# FILE: Console.py
# AUTHOR: See https://ko-fi.com/randallnagy
#
from PyTrek.AbsDisplay import abs_display
from PyTrek.Points import *

class Con(abs_display):
    '''
    The best place to start is by encapsulating the default
    display. Will add screen metadata for it all, later.
    '''
    def __init__(self):
        super().__init__(abs_display.ST_CONSOLE)

    def display(self, message = ''):
        print(message)

    def read(self, prompt=''):
        return input(prompt)

    def read_double(self, prompt):
        text = input(prompt)
        try:
            value = float(text)
            return value
        except:
            pass
        return False

    def read_sector(self, prompt= "Helm: sector 1-64, speed 1.0-9.0?"):
        text = input(prompt + ': ')
        return WarpDest.parse(text)

    def read_xypos(self, prompt= "Helm: a-h, 1-8?"):
        text = input(prompt + ': ')
        return SubDest.parse(text)


if __name__ == '__main__':
    con = Con()
    con.display("Testing!")
    con.show_banner(["Testing, too!"])
    con.show_banner(["Testing", " .......... too!"])
