"""Asks the user for a number until they enter -1
Reports the total value of all the numbers at the end
"""
SENTINEL = -1

number = int(input('Type a number: '))
total = 0
while number != SENTINEL:
    total += number
    number = int(input('Type a number: '))
print('Total is ' + str(total))