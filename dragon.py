import random
import time


def display_Intro():
    print('''Вы находитесь в землях, заселенных драконами.
    Перед собой вы видите две пещеры. В одной из них - дружелюбный дракон, 
    который готов поделиться с вами сокровищами. Во второй -
     жадный и голодный дракон, который мигом Вас съест.''')

    print()


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('В какую пещеру вы войдете? (нажмите клавишу 1 или 2) ')
        cave = input()
    return cave


def check_cave(chosen_Cave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Ее темнота заставляет Вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...')
    print()
    time.sleep(2)

    friendly_Cave = random.randint(1, 2)

    if chosen_Cave == str(friendly_Cave):
        print('...делится с Вами сокровищами!')
    else:
        print('...моментально Вас съедает!')


play_Again = 'да'
while play_Again == 'да' or play_Again == 'д':
    display_Intro()
    cave_Number = choose_cave()
    check_cave(cave_Number)

    print('Попытаете удачу еще раз? (да или нет) ')
    play_Again = input()

