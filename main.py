import patterns
import time
import output as out
import numpy as np

iterable = np.arange(1000)
bar = patterns.ProgressBar(iterable, 20, '=')
printer = out.Printer(timestamps=True)
for elem in bar:
    #print(elem)
    time.sleep(0.01)

