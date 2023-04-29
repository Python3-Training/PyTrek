import abc

class abs_display(abc.ABC):
    '''
    The plan is to have several places to 
    display information. The idea is to 
    use only one display to show a certain 
    type of message. 
    
    Networked screens (let alone game 
    play) would also be a great idea.
    
    Here is how we could to that:
    https://www.oreilly.com/library/view/tcpip-and-udpip/9781484294543/

    Event logging might be in there somewhere
    as well?
    '''

    ST_DEFAULT = 'd'
    ST_CONSOLE = 'c'
    ST_NETWORK = 'n'
    
    def __init__(self, type_ = ST_DEFAULT, width = 80, height = 24):
        super().__init__()
        self.screen_type = type_
        self.width = width
        self.height = height
        self.xpos = self.ypos = -1

    @abc.abstractmethod
    def display(self, message):
        pass

    def show_strings(self, string_list):
        '''
        Enumerate an array of strings into 
        self.display.
        '''
        for string in string_list:
            self.display(string)
        self.display()

    def show_banner(self, string_list, star = '*'):
        '''
        Enumerate an array of strings into a 
        single-character self.display box.
        '''
        if not star:
            star = '*'
        star = star[0]
        sz = len(max(string_list, key=len))
        max_ = sz + 4
        self.display(star * max_)
        for str_ in string_list:
            self.display(star + ' ' + str_.center(sz) + ' ' + star)
        self.display(star * max_)
        return sz

