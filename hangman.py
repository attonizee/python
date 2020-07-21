import random


HANGMAN_PICS = ['''
    +---+
    |   |
        |
        |
        |
       ===''', '''
    +---+
    |   |
    O   |
        |
        |
       ===''', '''
    +---+
    |   |
    O   |
    |   |
        |
       ===''', '''
    +---+
    |   |
    O   |
   /|   |
        |
       ===''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    |   |
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    |   |
    O   |
   /|\  |
   / \  |
       ===''', '''
    +---+
    |   |
   (O   |
   /|\  |
   / \  |
       ===''', '''
    +---+
    |   |
   (O)  |
   /|\  |
   / \  |
       ===''']

words = {'professions': 'devops developer designer admin accountant marketolog'.split(),
'animals': 'lion zebra rabbit horse dog cat aligator'.split()}


def Get_Random_Word(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return wordDict[wordKey][wordIndex], wordKey


def display_Board(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Wrong Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()


def get_Guess(alreadyGuessed):
    while True:
        print('Enter one letter: ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please, enter ONE letter')
        elif guess in alreadyGuessed:
            print('You entered this letter already. Try another.')
        elif guess not in 'qwertyuiopasdfghjklzxcvbnm':
            print('Please, enter the letter!')
        else:
            return guess


def play_Again():
    print('Do you wanna play again? (y\\n)')
    return input().lower().startswith('y')


def difficulty_Level():
    difficulty = ''
    while True:
        print('Choose difficulty level. E - easy, M - Medium, H - Hard')
        difficulty = input().upper()

        if difficulty == 'E':
            break

        elif difficulty == 'M':
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
            break

        elif difficulty == 'H':
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
            del HANGMAN_PICS[5]
            del HANGMAN_PICS[3]
            break
        else:
            print('Make right choice')


def main():
    print('H A N G M A N')
    difficulty_Level()
    missedLetters = ''
    correctLetters = ''
    secretWord, secretSet = Get_Random_Word(words)
    gameIsDone = False

    while True:
        print(f'Secret word from category {secretSet}')

        display_Board(missedLetters, correctLetters, secretWord)

        guess = get_Guess(missedLetters + correctLetters)

        if guess in secretWord:
            correctLetters = correctLetters + guess
            found_All_Letters = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetters:
                    found_All_Letters = False
                    break
            if found_All_Letters:
                print(f'Yes. You get it. The word is {secretWord}')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                display_Board(missedLetters, correctLetters, secretWord)
                print(f'You lose. The word is {secretWord}')
                gameIsDone = True
        if gameIsDone:
            if play_Again():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord, secretSet = Get_Random_Word(words)
            else:
                break


if __name__ == '__main__':
    main()
