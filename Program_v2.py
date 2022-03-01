#main program version 2 
#--> Dynamic inputs     --> Validation 

from Timer import *
from Sound import*
from Functions import *

option = 0

line = "TIMER!!!!\n"
Design(line)
print("\n")
TimeDelay(1)

while option != "1" and option != "2":
    line="1. Explanation of how program works\n2. Go start your timer\n"
    Design(line)
    option=input("(1 or 2):")
    print("\n")

if option == "1":
    Design("")
    print("EXPLANATION")
    print("-->Enter number of timers:3, means you set three timers that happen one after another.")
    print("-->Input the duration for three timers. Eg. Let 3 timers have duration 3 seconds. Then once every 3 seconds you will hear a beep.")
    print("-->USE: when u dont want to set the timer after every lapse.")
    print("Press Enter to continue to timer")
    Design("")
    input()

number= int(input("\n\nenter number of timers :"))
print("\n")

timings = [[0 for i in range(3)]for j in range(number)]
#print(timings)#


for i in range (0, number):

    repeat_hours = True
    repeat_minutes = True
    repeat_seconds = True

    while repeat_hours == True:
        try:
            line = "Timer ",i+1," input hours:"
            FluidText(line)
            hours = int(input())
            if hours < 0:
                line = "enter a VALID NUMBER\n"
                FluidText(line)
            else:
                repeat_hours = False
        except ValueError:
            line = "enter a NUMBER\n"
            FluidText(line)

    while repeat_minutes == True:
        try:
            line = "Timer ",i+1," input minutes:"
            FluidText(line)
            minutes = int(input())
            if minutes < 0 or minutes > 59:
                line = "enter a VALID NUMBER\n"
                FluidText(line)
            else:
                repeat_minutes = False
        except ValueError:
            line = "enter a NUMBER\n"
            FluidText(line)

    while repeat_seconds == True:
        try:
            line = "Timer ",i+1," input seconds:"
            FluidText(line)
            seconds = int(input())
            if seconds < 0 or seconds > 59:
                line = "enter a VALID NUMBER\n"
                FluidText(line)
            else:
                repeat_seconds = False
        except ValueError:
            line = "enter a NUMBER\n"
            FluidText(line)

    timings[i][0] = hours
    timings[i][1] = minutes
    timings[i][2] = seconds
    #print(timings)#
    Design("")

#print(timings)#
line="Timer will begin once you press enter\n"
FluidText(line)
input()
line="Timer has begun!\n\n"
FluidText(line)

for i in range (0, number):
    result_time = Timer(timings[i][0], timings[i][1], timings[i][2])

    if result_time == True:
        print("--> Timer ",i+1," has ended")
        play('./Alarm_Beep_1s.wav')   

print("\n")
line = "All timers are over!. You finished your task.\n"
Design(line)
print("press any key to close program\n")
input()