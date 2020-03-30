#!/usr/bin/python3
import os
import sys

print("First programm")
print("Hello")
name = input ("Your name :")

print(name, ", welcome to Python!")
answer = input("Let's work? (Y/N)")

if answer.lower() == 'y':
    print("Good man")
    print("Let's start")
    print("Choose  what to do")
    print("1) OS info")
    print("2) Process")
    work = int(input("Your choice: "))


    if work == 1:
            print("OS platform" + sys.platform)
            print(os.curdir)
    elif work == 2:
            print("Starting Word")
    else:
            print("Wrong choice")

elif answer.lower() == 'n':
    print("Goodbye")
else:
    print("Wrong answer")
