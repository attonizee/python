import datetime
from functools import wraps


def cancel_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} is cancelled')
        
    return wrapper


def speed_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        res = func(*args, **kwargs)
        end = datetime.datetime.now()
        print(func.__name__, end - start)
        return res
    return wrapper


def counter_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print(f'{func.__name__} was called {wrapper.count} times')
        return res
    wrapper.count = 0
    return wrapper


def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator created')
        print(f'Function {func.__name__} started')
        res = func(*args, **kwargs)
        print(f'Function {func.__name__} ended')
        return res
    return wrapper


def except_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as e:
            print('Something wrong', e)
        else:
            return res
    return wrapper


@cancel_decorator
def function1():
    print('Do some')


@logging_decorator
@counter_decorator
@speed_decorator
def function2(name, age):
    print(f'My name {name} and i am {age} years old')


@except_decorator
def function3(some):
    print('Something', some)


if __name__ == '__main__':
    function1()
    function2('Leo', 25)
    function2('Max', 24)
    function3('Its fine')
