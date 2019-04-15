#!/usr/bin/python

from playsound import playsound # NOTE: does not work with python3
import os
import time
import random
import sys

"""
Validates that minutes is in range of 0-59 and hours is in range of 0-23.
"""
def checkClockParams(param, low, high):
    try:
        assert param >= min and param <= max
    except AssertionError:
        sys.exit("{} must be between {} and {}. \n".format(param, low, high))


"""
The alarm has 2 modes: later (for a certain amount of time in minutes:seconds from the current time) and
at (at a specific hour:minute of the day). 
"""
def setAlarm(mode, sound):
    if mode == "later":
        try:
            mins = int(raw_input("How many minutes? "))
            secs = int(raw_input("How many seconds? "))
            time.sleep(60 * mins + secs)
            playsound(sound)
        except TypeError:
            sys.exit("Please enter integer value(s) for minutes and seconds\n")
    elif mode == "at":
        try:
            hrs = int(raw_input("Hour? 0-23 "))
            checkClockParams(hrs, 0, 23)
            mins = int(raw_input("Minute? 0-59 "))
            checkClockParams(mins, 0, 59)
            while True:
                structTime = time.localtime()
                if structTime.tm_hour == hrs and structTime.tm_min == mins:
                    playsound(sound)
                    break
        except TypeError:
            sys.exit("Please enter integer value(s) for hour and minute\n")
    else:
        sys.exit("Not a valid mode\n")


"""
Lists all sound files in a provided subdirectory with default sounds provided and allows user to choose
one or go random. Returns the relative pathname of the sound track.  
"""
def getSoundFile(direc):
    sounds = os.listdir(direc)
    for sound in sounds:
        print(sound)

    if raw_input("Pick a sound or random? Yes/No:").lower() == "yes":
        file = raw_input("Enter a selection:")
        if file not in sounds:
            sys.exit("Not a valid selection.\n")
    else:
        file = random.choice(sounds)
    return direc + "/" + file


def main():
    print("Welcome to Alarm Clock!\n")

    ext = raw_input(".wav or .mp3 format?:").lower()
    if ext == ".wav":
        sound = getSoundFile("Sounds/wav")
    elif ext == ".mp3":
        sound = getSoundFile("Sounds/mp3")
    else:
        sys.exit("{} is not a valid audio format!".format(ext))

    mode = raw_input("Set for x minutes/seconds later or at a particular time? later/at ").lower()
    setAlarm(mode, sound)

if __name__ == "__main__":
    main()