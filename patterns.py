import sys

class ProgressBar:
    '''
    The ProgressBar class, meant to be init before a finite loop with known iteration count,
    to show the progress of the loop
    Consider that there should be no other prints during the use of this pattern, because that will fuck up the print with newlines
    '''
    def __init__(self, iterations, bins=20, symbol='='):
        self._step = round(iterations/bins)
        self._sym = symbol
        self._index = 1
        self._bins = 100/bins
        self._formatter = "[%-"+str(bins)+"s] %d%%"

    def update(self):
        '''
        Adds a tick to the progress bar. will simply stop updating if the loop goes out of bounds of the previously stated max iteration count
        :return:
        '''
        if self._index <= self._bins:
            sys.stdout.write('\r') # resets the cursor
            sys.stdout.write((self._formatter) % (self._sym * self._index, self._bins * self._index)) # writes the formatted string
            sys.stdout.flush() # flush buffer to print text immediately
            self._index += 1


