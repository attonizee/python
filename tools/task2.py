digits = [1, 14, 12, 65, -15, 76, 90, 84, 32, 43, 57, 68, -44, 77]

result_digits = [digit for digit in digits if digit % 3 == 0 and digit > 0 and digit % 4 != 0]

print(result_digits)