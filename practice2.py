#!/bin/python3

#1

list1 = [2, 2, 5, 7, 7, 8, 2, 12, 12, 4]
list2 = [2, 7, 12, 3]
for number in list1[:]:
    if number in list2:
        list1.remove(number)
print(list1)

#2

date = '04.04.2020'
d, m, y = date.split('.')
print(d, m, y)

month = {'01': 'Jan',
    '02': 'Feb',
    '03': 'Mar',
    '04': 'Apr',
    '05': 'May',
    '06': 'Jun',
    '07': 'Jul',
    '08': 'Aug',
    '09': 'Sep',
    '10': 'Oct',
    '11': 'Nov',
    '12': 'Dec'
}

day = {
    '01': 'first',
    '02': 'second',
    '03': 'third',
    '04': 'fourth',
    '05': 'fifth',
    '06': 'sixth',
    '07': 'seventh',
    '08': 'eith',
    '09': 'ninth',
    '10': 'tenth',
    '11': 'eleventh',
    '12': 'twelfth',
    '13': 'thirteenth',
    '14': 'fourteenth',
    '15': 'fifteenth',
    '16': 'sixteenth',
    '17': 'seventeenth',
    '18': 'eighteenth',
    '19': 'nineteenth',
    '20': 'twenth',
    '21': 'twenty first',
    '22': 'twenty second',
    '23': 'twenty third',
    '24': 'twenty fourth',
    '25': 'twenty fifth',
    '26': 'twenty sixth',
    '27': 'twenty seventh',
    '28': 'twenty eith',
    '29': 'twenty ninth',
    '30': 'thirtieth',
    '31': 'thirty fist'

}

result = f'{day[d]} {month[m]} {y} year'
print(result)


#3

list3 = [1, 1, 1, 3, 5, 5, 6, 8, 10, 11, 11]
result = []
for number in list3:
    if list3.count(number) == 1:
        result.append(number)
print(result)

