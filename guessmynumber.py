"""
Generates a random number between 1 and 99.
Has the user keep guessing until they figure out
what the number is. Tells the user after each guess
if their guess was too high or too low.
"""
import random

secret_number = random.randint(1,99)
print('I am thinking of a number between 1 and 99')
guess = int(input('Take a guess: '))
while guess != secret_number:
    if guess > secret_number:
        print('Too high')
    else:
        print('Too low')
    print('')
    guess = int(input('Take another guess: '))
print('Congratulations! The number was ' + str(secret_number))


