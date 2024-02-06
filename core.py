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



clear()

delay_print(linesdict[1])

time.sleep(2)

delay_print(linesdict[2])
clear()

delay_print(linesdict[3])
time.sleep(1.5)

delay_print(linesdict[4])
clear()

delay_print(linesdict[5])
time.sleep(1.3)
delay_print(linesdict[6])

clear()
delay_print(linesdict[7])
time.sleep(1)
delay_print(linesdict[8])
time.sleep(1.5)
delay_print(linesdict[9])


