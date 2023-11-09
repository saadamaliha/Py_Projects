# Py_Projects
1. Ancient Game of Nimm
     The ancient game of Nimm starts with a pile of 20 stones between the players.
     The two players alternate turns.
     On a given turn, a player may take either 1 or 2 stone from the center pile.
     The two players continue until the center pile has run out of stones.
   
2. Carbon Dating
   The program takes the % of C-14 and C-12 present in a sample, and it calculates the age of the fossil
  
3. Mental Health Bot
     This program provides basic information (definition, symptoms, causes, treatment options)
      about mental health conditions like depression, anxiety and ADHD
4. Learning Bot
       This is a random math generating program. It generates addition and subtraction problems.
5. Vocabulary Builder
    This program is a vocabulary learning tool that helps users practice and memorize advanced English words and their meanings.
    It uses a list of tuples, called vocab, that contains a set of 50 advanced English words and their corresponding meanings.
6. Py Calculator
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

7. Hailstone Sequence
    The Hailstone sequence is also known as The Collatz Conjecture. It was a problem proposed by mathematician L. Collatz.
    It is known as the hailstone sequence because the sequence resembles the pattern of formation of hailstones.
    Hailstones get blown up by the winds in the cloud, come down when they form ice pellets, and again get blown by the winds.
    Similarly, the sequence increases and decreases its value alternatively. Thus, according to the sequence, we may start with any whole number but will always end up with the sequence of 4, 2, 1.

    In this program, the hailstone() function takes an input number num,
    and generates a sequence using the Collatz algorithm, which is as follows:

        1. If the number is even, divide it by 2 to get the next number in the sequence.
        2. If the number is odd, multiply it by 3 and add 1 to get the next number in the sequence.
        3. Repeat this process until the number is equal to 1.
        from- Su, Francis E., et al. “Hailstone Numbers.” Math Fun Facts. <https://www.math.hmc.edu/funfacts>
        In the end it prints the number of steps that was required to reach 1
8. Sentinel
      Asks the user for a number until they enter -1
      Reports the total value of all the numbers at the end
9. Car game
    A simple car game that takes commands from the user to 'start', 'stop', and 'quit'
11. Guess My Number
    Generates a random number between 1 and 99.
    Has the user keep guessing until they figure out
    what the number is. Tells the user after each guess
    if their guess was too high or too low.
