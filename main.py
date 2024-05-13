import patterns
import time
import output as out

bar = patterns.ProgressBar(20, 20, '=')
printer = out.Printer(timestamps=True)
for i in range (20):
    bar.update()
    time.sleep(1)
    #printer.error('printed successfully')
    #printer('peter', 'cyan', underline=True, bold=True)
