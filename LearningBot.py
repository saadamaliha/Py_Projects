# This is a simple math problem generating program.

import random

print("""Welcome to MathChamp, your mental math tool. 
To start, type 'start'
To quit, type 'quit'
""")
started = True
while started is True:
    command = input(">").lower()
    if command == "start":
        print("Game started")
        count = 0
        while count < 3:
            integer1 = random.randint(10, 99)
            integer2 = random.randint(10, 99)
            print('What is ' + str(integer1) + ' + ' + str(integer2) + '?')
            calculate = integer1 + integer2
            answer = int(input('Your answer: '))
            if answer == calculate:
                count += 1
                print('Correct! You got ' + str(count) + ' in a row!')
            else:
                print('Incorrect. The expected answer is ' + str(calculate))
        while 3 <= count < 6:
            integer1 = random.randint(10, 99)
            integer2 = random.randint(10, 99)
            print('What is ' + str(integer1) + ' - ' + str(integer2) + '?')
            calculate = integer1 - integer2
            answer = int(input('Your answer: '))
            if answer == calculate:
                count += 1
                print('Correct! You got ' + str(count) + ' in a row!')
                started = False
            else:
                print('Incorrect. The expected answer is ' + str(calculate))

    else:
        print("See you again.")
        break
