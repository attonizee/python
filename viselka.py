import random

WORDS = ['admin', 'developer', 'devops' ]
LIFES = 8


def random_word_init():
    return random.choice(WORDS)


def user_input():
    user_letter = input('Enter the letter: ')
    return user_letter


def word_status_init(word):
    status = []
    for letter in word:
        status.append(False)
    return status


def game_is_over(status, current_errors):
    if current_errors >= LIFES:
        return True

    for stat in status:
        if not stat:
            return False

    return True


def perform_check(word, status, letter):
    if letter not in word:
        return False

    for index, l in enumerate(word):
        if letter == l:
            status[index] = True

    return True
    

def print_word(word, status):
    for index, letter in enumerate(word):
        if status[index]:
            print(letter, end='')
        else:
            print('_', end=' ')

    print()


def main():
    word = random_word_init()
    status = word_status_init(word)
    current_errors = 0
    used = []
    print(f'I chosed the word, try to guess. You got {LIFES} lifes every mistake lower your lifes.')

    while not game_is_over(status, current_errors):
        print_word(word, status)
        print('Errors left ', LIFES - current_errors)
        letter = user_input()
        result = perform_check(word, status, letter)

        if not result:
            print(f'The letter {letter} not in word, try more')
            current_errors += 1
            used.append(letter)
            print(f'You already used letters {used}')

    if result:
        print_word(word, status)
        print('Congratulation, you win!')
    else:
        print('You are dead. Game over')
   

if __name__ == '__main__':
    main()
    
