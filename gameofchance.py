import random


money = 100


def flipping_Coin():
    coin = ['Head', 'Tail']
    throw = random.choice(coin)
    rate = int(input('Enter your rate: '))
    choice = input('Enter the side of a coin: Head or Tail ')
    if throw.lower() == choice.lower():
        print(f'You win {rate}$. Monet droped {throw}')
        return rate
    else:
        print(f'You loose {rate}$. Monet dropped {throw} . Try again')
        return rate * -1


def rolling_Dice():
    dice1 = random.choice(range(1, 5))
    dice2 = random.choice(range(1, 5))
    result = dice1 + dice2
    user_rate = input('Make your stake: "odd" or "even" ')
    money_rate = int(input('Money on table!: '))
    if user_rate == 'even' and result % 2 == 0:
        print(f'You are win! You drop {result} and win {money_rate}$')
        return money_rate
    elif user_rate == 'odd' and result % 2 != 0:
        print(f'You are win! You drop {result} and win {money_rate}$')
        return money_rate
    else:
        print(f'You are wrong. You drop {result} and loose {money_rate}$')
        return money_rate * -1


def pick_Card():
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    player1 = random.choice(deck)
    deck.remove(player1)
    player2 = random.choice(deck)
    money_rate = int(input('Money on table!: '))
    if player1 > player2:
        print(f'You win! Your card amount is {player1}, your companion card amount is {player2} and  you win {money_rate}$')
        return money_rate
    elif player1 < player2:
        print(f'You loose. Your card amount is {player1}, your companion card amount is {player2} and you loose {money_rate}$')
        return money_rate * -1
    elif player1 == player2:
        print(f'The game is tie! Nobody win!')
        return 0 

if __name__ == '__main__':
    money += flipping_Coin()
    print(f'You played Flipping Coin. Your amount of money is {money}$')
    money += rolling_Dice()
    print(f'You played Rolling Dice. Your amount of money is {money}$')
    money += pick_Card()
    print(f'You played Pick Card. Your amount of money is {money}$')