import patterns
import format
import ansi
import output as out
import numpy as np

'''iterable = np.arange(1000)
bar = patterns.ProgressBar(iterable, 20, '=')
printer = out.Printer(timestamps=True)
for elem in bar:
    #print(elem)
    time.sleep(0.01)
'''

printer = out.Printer()
'''
fmt = format.PPFormat([ ansi_util.Font('font2')])
printer('peter', fmt)'''

for key in ansi._EFFECTS:
    printer(key, format.PPFormat([format.ColourText([255,100,100]), format.Effect(key)]))
    print('\n')