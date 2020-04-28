import math

old_numbers = [1, 14, 12, 65, -15, 76, 90, 84, 32, 43, 57, 68, -44, 77]

def sqrt_list(list):
    result_numbers = [int(math.sqrt(number)) if number > 0 else number for number in list]
    return result_numbers

result = sqrt_list(old_numbers)

print(old_numbers)
print(result)