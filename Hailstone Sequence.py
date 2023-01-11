"""
In this program, the hailstone() function takes an input number num,
and generates a sequence using the hailstone algorithm, which is as follows:

1. If the number is even, divide it by 2 to get the next number in the sequence.
2. If the number is odd, multiply it by 3 and add 1 to get the next number in the sequence.
3. Repeat this process until the number is equal to 1.
from- Su, Francis E., et al. “Hailstone Numbers.” Math Fun Facts. <https://www.math.hmc.edu/funfacts>

In the end it prints the number of steps that was required to reach 1
"""


def hailstone():

    # Setting the counter equals to 0 to count the number of times the loop runs
    count = 0
    # Asking a number as input from the user
    num = int(input("Enter a number: "))
    # Loop which runs till the final output number is 1
    while num != 1:
        # Counter increases by 1 each time the while loop runs
        count += 1
        # If the number is even the while loop enter this if command and produces an output number
        if num % 2 == 0:
            new_num = num / 2
            print(str(int(num)) + " is even, so I take half: " + str(int(new_num)))
            num = new_num
        # If the number is odd the while loop enter this if command and produces an output number
        elif num % 2 != 0:
            new_num = 3*num + 1
            print(str(int(num))+" is odd, so I make 3n + 1: "+str(int(new_num)))
            num = new_num
    # Printing the number of steps it takes to get 1 as the output number
    print("The process took "+str(int(count))+" steps to reach 1")


# This provided line is required at the end of a Python file
# to call the main() function.

hailstone()