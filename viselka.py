import random

words = ['admin', 'developer', 'devops' ]
lifes = 8
errors = 0
used = []
word = random.choice(words)
result_word = '_ ' * len(word)



play = ''
while play != 'n':
    play = input('Do you wanna play? y/n ')
    print(f'I chosed the word, try to guess. You got {lifes} lifes every mistake lower your lifes.')
    print(f'The word is looks\n {result_word}\n')
    while errors < lifes and result_word != word:    
        user_letter = (input('Enter the letter: '))
        if user_letter in word:
            part = ''
            for i in range(len(word)):
                if user_letter == word[i]:
                    part += user_letter
                else:
                    part += result_word[i]
            result_word = part
            print(f'The word is now\n {result_word}\n')
        else:
            print(f'The letter {user_letter} not in word, try more')
            errors += 1
            used.append(user_letter)
            print(f'You already used letters {used}')

    if result_word == word:
        print(f'Congratulation, you win! The word is: "{result_word}"')
    elif errors == lifes:
        print('You are dead. Game over')
    else:
        print('Something wrong!')
        


        
        

