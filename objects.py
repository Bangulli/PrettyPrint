import sys

class ProgressBar:
    def __init__(self, step_size, symbol='='):
        self._step = step_size
        self._sym = symbol
        self._index = 1
        self._bins = str(int(100/self._step))
        self._formatter = "[%-"+self._bins+"s] %d%%"

    def update(self):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write((self._formatter) % (self._sym * self._index, self._step * self._index))
        sys.stdout.flush()
        self._index += 1

class Colour:
    def __init__(self):

        self.BLUE = '\033[94m'
        self.CYAN = '\033[96m'
        self.GREEN = '\033[92m'
        self.YELLOW = '\033[93m'
        self.RED = '\033[91m'
        self.WHITE = '\033[0m'

        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'
        self.HEADER = '\033[95m'

        self.cLookup = {
            'yellow':self.YELLOW,
            'green':self.GREEN,
            'blue':self.BLUE,
            'cyan':self.CYAN,
            'red':self.RED,
            'white':self.WHITE
        }
