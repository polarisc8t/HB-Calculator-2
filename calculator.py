"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here


while True:
    

    # query user for an operator and numbers upon which to operate
    operand = raw_input("Please enter an operand followed by numbers to evaluate: ")
    
    # tokenize the user input from above
    operand = operand.split(" ")
    
    # reassign operand index 1 and 2 into a new list 
    numbers = operand[1:]

    # loop through the length of the list 'numbers'  
    for a in range(len(numbers)):
        # cast the type of numbers from string to int
        numbers[a] = int(numbers[a])

    # perform matching regarding operator from user input    
    if operand[0] == '+':
      # show user output  
      print add(numbers[0], numbers[1])

    elif operand[0] == '-':
        print subtract(numbers[0], numbers[1])

    elif operand[0] == '*':
        print multiply(numbers[0], numbers[1])

    elif operand[0] == '/':
        print divide(numbers[0], numbers[1])

    elif operand[0] == 'sqr':
        print square(numbers[0])

    elif operand[0] == 'cube':
        print cube(numbers[0])

    elif operand[0] == 'pow':
        print pow(numbers[0],numbers[1])

    elif operand[0] == 'mod':
        print mod(numbers[0], numbers[1])
        
    else: 
        print "Invalid operation!"    