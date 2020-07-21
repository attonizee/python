#Function are objects

def add_five(num):
    print(num + 5)

print(add_five)

#Functions within functions

def add_six(num):
    def add_two(num):
        return num + 2

    num_plus_two = add_two(num)
    print(num_plus_two + 5)

add_five(10)

#Returning functions from functions

def get_math_function(operation): # + or -
    def add(n1, n2):
        return n1 + n2
    def sub(n1, n2):
        return n1 - n2

    if operation == '+':
        return add
    elif operation == '-':
        return sub

add_function = get_math_function('+')
sub_function = get_math_function('-')

#Decorating a function

def title_decorator(print_name_function):
    def wrapper():
        print('IT Specialist:')
        print_name_function()
    return wrapper


def print_my_name():
    print('Mike')

decorated_function = title_decorator(print_my_name)
decorated_function()

#Decorators

@title_decorator
def print_a_name():
    print('Anatolii')

print_a_name()

#Decorators w/ Parameters

def model_decorator(car_name):
    def wrapper(*args, **kwargs):
        print('Mercedes:')
        car_name(*args, **kwargs)
    return wrapper


@model_decorator
def name_car(name, year):
    print(f'The car {name} is {year} year old')

name_car('SLS', 5)