def exponentiation(number):
    if number == 13:
        raise ValueError ('Dont use number 13')
    else:
       return number ** 2
    
user_number = int(input('Enter the number from 1 to 100: '))

try:
    result = exponentiation(user_number)
except ValueError:
    print('Dont use number 13')
else:
    print(result)