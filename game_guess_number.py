#!/bin/python3

#Create number
import random

number = random.randint(1, 100)
#print(number)
#Ask to guess number from user
user_number = None
count = 0

levels = {1: 10, 2: 5, 3: 3}
level = int(input('Choose difficulty leve(1 - 10 attemps, 2 - 5 attemps, 3 - 3 attemps): '))
max_count = levels[level]

user_count = int(input('Enter number of users: '))
users = []
for i in range(user_count):
    users.append(input(f'Enter user {i} name: '))
print(f'The our players {users}')

is_the_winner = False
winner_name = None

while not is_the_winner:
    count += 1
    if count > max_count:
        print('Your attemps is over. You lose')
        break
    print(f'Attemp №{count}')
    for user in users:
        print(f'Now is {user} try')
        user_number = int(input('Computer  made a number, try to guess it. Enter number from 1 to 100: '))
        if user_number == number:
            is_the_winner = True
            winner_name = user
            break
        elif user_number < number:
            print('Wrong, your number is lower, try more')
        elif user_number > number:
            print('Your number is bigger, try more')
        else:
            ('Wrong number, enter from 1 to 100')
else:
    print(f'Congratulation! {winner_name} is win!')
    