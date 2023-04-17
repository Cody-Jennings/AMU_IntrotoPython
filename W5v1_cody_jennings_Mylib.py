# Program Name: W5v1_cody_jennings_Mylib.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Date: 20230416


# W5v1_cody_jennings_Mylib.py

def add(firstNum, secondNum):
    return firstNum + secondNum

def subtract(firstNum, secondNum):
    return firstNum - secondNum

def multiply(firstNum, secondNum):
    return firstNum * secondNum

def divide(firstNum, secondNum):
    if secondNum == 0:
        return "You cannot divide by zero"
    else:
        return firstNum / secondNum

def scalc(firstNum, secondNum, operator):
    """
    This function takes two numbers and an operator as input and returns the result of the arithmetic operation.
    """
    if operator == "+":
        return add(firstNum, secondNum)
    elif operator == "-":
        return subtract(firstNum, secondNum)
    elif operator == "*":
        return multiply(firstNum, secondNum)
    elif operator == "/":
        if secondNum == 0:
            return "Cannot divide by zero."
        else:
            return divide(firstNum, secondNum)
    else:
        return "Invalid operator."

