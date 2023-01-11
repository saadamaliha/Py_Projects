"""
This program is a simple command-line calculator that allows users to perform basic arithmetic operations on two numbers.
It defines four functions, add(), subtract(), multiply() and divide() which take in two numbers as arguments and
perform the corresponding mathematical operations on them.

The divide() function includes an additional check to ensure that the divisor is not zero.
If the divisor is zero, it raises a "ValueError" exception with the message "Cannot divide by zero!"

The main function of the program, calculator(), uses a while loop to repeatedly prompt the user for input.
The loop will continue running until the user enters "q" to quit. It prompts the user for two numbers, num1 and num2,
to perform the arithmetic operation on, and an operator (+,-,*,/).
It then checks the value of the operator and calls the corresponding function
add, subtract, multiply or divide, passing the num1 and num2 as arguments.
If the operator entered is not a valid operator, the program will return "Invalid operator" .

The divide function also uses a try except block to catch the ValueError exception raised when the divisor is zero
and display the error message accordingly .

"""


def add(x, y):
    """
    Add two numbers and return the result
    """
    return x + y


def subtract(x, y):
    """
    Subtract two numbers and return the result
    """
    return x - y


def multiply(x, y):
    """
    Multiply two numbers and return the result
    """
    return x * y


def divide(x, y):
    """
    Divide two numbers and return the result.
    Raise error if divisor is zero
    """
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


def calculator():
    """
    The main calculator function
    """
    while True:
        # get the first number from the user
        num1 = float(input("Enter first number (q to quit): "))
        if num1 == "q":
            break
        # get the second number from the user
        num2 = float(input("Enter second number: "))
        # get the operator from the user
        operator = input("Select operation (+, -, *, /): ")
        if operator == "+":
            print(add(num1,num2))
        elif operator == "-":
            print(subtract(num1,num2))
        elif operator == "*":
            print(multiply(num1,num2))
        elif operator == "/":
            try:
                print(divide(num1,num2))
            except ValueError as e:
                print(e)
        else:
            print("Invalid operator")


calculator()
