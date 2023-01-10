
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
