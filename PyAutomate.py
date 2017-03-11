# PyAutomate
# Copyright (c) Alexander Richards
# Licensed under CC Attribution

#Import time for time.wait
import time
#Import sys for sys.argv
import sys

while True:
    #Figure out if any Args have been given
    if not len(sys.argv) >= 3:
        #If not, print Usage
        print("PyAutomate 0.1")
        print("Usage: python pyautomate.py [time] [false/true] [path]")
        print("")
        print("Time betwenn executions - [time] - In Seconds")
        print("Repeat or not? - [false/true] - HAS to be true or false")
        print("File to run - [path] - Full Directory")
        raise SystemExit
    #Run the parser if more than 3 are given
    
    if len(sys.argv) >= 3:
        #Get the Time to wait and convert to float
        timetowait = float(sys.argv[1])
        
        #If repeat is false, Run after X amount of time
        if sys.argv[2] == "false":
            time.sleep(timetowait)
            exec(open(str(sys.argv[3])).read())
            raise SystemExit

        #If repeat is true, Run every X amount of time
        if sys.argv[2] == "true":
            while True:
                time.sleep(timetowait)
                exec(open(str(sys.argv[3])).read())
