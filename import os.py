from lines import linesdict
import time
import sys
import os

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.03)
        
def clear():
    time.sleep(3.5)
    os.system('cls')

delay_print(linesdict[1])

time.sleep(2)

delay_print(linesdict[2])
clear()

delay_print(linesdict[3])
time.sleep(1.5)

delay_print(linesdict[4 ])
clear()
