#main program version 2 
# fixed inputs. speciallized based on clients request
#--> Dynamic inputs     --> Validation 

from Timer import *
from Sound import *
from Functions import *
import datetime

line = "TIMER!!!!\n"
Design(line)
print("\n")
TimeDelay(1)

print("\n")

timings = [[0, 4, 0], [0, 2, 0], [0, 2, 0], [0, 2, 0], [0, 1, 0], [0, 7, 0], [0, 8, 0], [0, 4, 0], [0, 1, 0], [0, 2, 0]]
#timings = [[0, 0, 4], [0, 0, 2], [0, 0, 2], [0, 0, 2], [0, 0, 1], [0, 0, 7], [0, 0, 8], [0, 0, 4], [0, 0, 1], [0, 0, 2]]

line = "Timer will begin once you press enter\n"
FluidText(line)
input()
line="Timer has begun!\n\n"
FluidText(line)

current_time_start = datetime.datetime.now()
print(current_time_start)
prev_cycle_time = current_time_start

for i in range (0, len(timings)):
    print("{0}:{1}:{2} timer started".format(timings[i][0], timings[i][1], timings[i][2]))
    result_time = Timer(timings[i][0], timings[i][1], timings[i][2])

    if result_time == True:
        print("--> Timer ",i+1," has ended")
        play('./Alarm_1Beep.wav')   
        current_time_end = datetime.datetime.now()
        print(current_time_end)
        difference = current_time_end - prev_cycle_time
        print(difference)
        prev_cycle_time = current_time_end
        
    print("\n")
line = "All timers are over!. You finished your task.\n"
Design(line)
print("press any key to close program\n")
input()

