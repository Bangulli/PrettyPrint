import sys

class ProgressBar:
    '''
    The ProgressBar class
    '''
    def __init__(self, step_size, symbol='='):
        '''
        Creates a progress bar object. The bar will get updated on update call
        :param step_size: The amount of bins [1-100] controls the amount of ticks to fill the bar
        :param symbol: The symbol used to to create the bar in the printout
        '''
        self._step = step_size
        self._sym = symbol
        self._index = 1
        self._bins = str(int(100/self._step))
        self._formatter = "[%-"+self._bins+"s] %d%%"

    def update(self):
        '''
        Adds a tick to the progress bar
        :return:
        '''
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write((self._formatter) % (self._sym * self._index, self._step * self._index))
        sys.stdout.flush()
        self._index += 1

class Colour:
    def __init__(self):
        '''
        Initializes the Colour class. Used to get color and formatting descriptors for printers
        '''
        self.BLUE = '\033[94m'
        self.CYAN = '\033[96m'
        self.GREEN = '\033[92m'
        self.YELLOW = '\033[93m'
        self.RED = '\033[91m'
        self.WHITE = '\033[0m'

        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

        self.cLookup = {
            'yellow':self.YELLOW,
            'green':self.GREEN,
            'blue':self.BLUE,
            'cyan':self.CYAN,
            'red':self.RED,
            'white':self.WHITE
        }
