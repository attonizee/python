from functools import reduce


numbers1 = [1, 4, 5, 30, 99]
numbers2 = list(map(lambda number: number % 5, numbers1))
print(numbers2)


numbers3 = [3, 4, 90, -2]
strokes1 = list(map(str, numbers3))
print(strokes1)


mass1 = ['some', 1, 'v', 40, '3a', str]
mass2 = list(filter(lambda x: not isinstance(x, str), mass1))
print(mass2)


mass3 = ['some', 'other', 'value']
chr1 = reduce(lambda x, y: x + y, list(map(lambda x: len(x), mass3)))
print(chr1)