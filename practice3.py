#!/bin/python3

#1

def info(name, age, city):
    result = (f'{name}, {age} years old, live in {city}')
    return result
print(info('Max', 25, 'Kiev'))

#2

def max_number(num1, num2, num3):
    result = max([num1, num2, num3])
    return result

print(max_number(9, 3, 7))

#3

player = {'name': None, 'health': 100, 'damage': 50, 'armor': 1.5}
enemy = {'name': None, 'health': 150, 'damage': 33, 'armor': 1.2}

player['name'] = input('Enter player name: ')
enemy['name'] = input('Enter enemy name: ')

def damage(damage, armor):
    return damage / armor


def attack(attacker, target):
    dam = damage(attacker['damage'], target['armor']) 
    target['health'] -= dam
    return target['health']

attack(player, enemy)
print(enemy)

 
   


    
