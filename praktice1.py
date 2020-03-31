#1
#number = int(input('Enter the number '))
#add = 2
#print(number + add)

#2

#while True:
#    number = int(input('Enter number beetween 0 and 10 '))
#    if number > 0 and number < 10:
#        print(number ** 2)
#        break
#    else:
#        print('Wrong number, enter beetween 0 and 10')
#3
name = input('Enter your name ')
second_name = input('Enter your second name ')
age = int(input('Enter your age '))
weight = int(input('Enter your weight '))

if age <= 30 and weight => 50 and weight <= 120:
    print('The patient {}, {}, age {}, weight {} in a good condition'.format(name, second_name, age, weight))
elif (age > 30 and age <= 40) and (weight < 50 or  weight > 120):
    print('The patient {}, {}, age {}, weight {} need to work under himself'.format(name, second_name, age, weight))
elif age > 40 and (weight < 50 or weight > 120):
    print('The patient {}, {}, age {}, weight {} need to see the doctor'.format(name, second_name, age, weight))
else:
    print('The {}, {}, age {}, weight {} is a strange guy'.format(name, second_name, age, weight))