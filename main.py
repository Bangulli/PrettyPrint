from PrettyPrint.figures import *
import time

indicator = RunningIndicator(mode='dots', update_frq=100)
while 1:
    indicator()
    time.sleep(0.1)
