
import PrettyPrint.figures as fig
import time
indicator = fig.RunningIndicator(mode='rotate', update_frq=1)
while 1:
    indicator()
    time.sleep(0.5)


'''
from PrettyPrint import *
printer = Printer()
printer('hello world')
iterable = range(1000)
bar = ProgressBar(iterable, 20)
for i in bar:
    time.sleep(0.5)
'''

