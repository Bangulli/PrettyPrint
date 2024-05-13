import objects
import time
import PrettyPrint as pp
bar = objects.ProgressBar(1, '#')
printer = pp.Out()
for i in range (5):
    #bar.update()
    time.sleep(1)
    printer('peter', 'blue', timestamp=True)
