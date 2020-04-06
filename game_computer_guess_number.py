#!/bin/python3
import random
#Range
min_value = 1
max_value = 100

#Computer attemps

user_answer = None

while user_answer != 1:
    number = random.randint(min_value, max_value)
    user_answer = int(input(f'Your number is {number}? 1 - Yes, 2 - Lower, 3 - Bigger: '))
    if user_answer == 2:
        min_value = number + 1
    elif user_answer == 3:
        max_value = number - 1
    
print(f'Your number is {number}. I am a winner!')
