# Program Name: Wk5_cody_jennings_Mylib.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Date: 20230409


def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    return num1 / num2

def scalc(p1):
    # Split p1 into its components: first number, second number and operator
    num1, num2, operator = p1.split(',')
    
    # Convert the first and second numbers to floats
    num1 = float(num1)
    num2 = float(num2)
    
    # Call the appropriate arithmetic operation function based on the operator
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return subtract(num1, num2)
    elif operator == '*':
        return multiply(num1, num2)
    elif operator == '/':
        return divide(num1, num2)
    else:
        return "Invalid operator"
