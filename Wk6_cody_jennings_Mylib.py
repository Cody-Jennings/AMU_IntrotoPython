# Program Name: Wk6_cody_jennings_Mylib.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Correction Date: 20230430


# Wk6_cody_jennings_Mylib.py

def add(firstNum, secondNum):
    return firstNum + secondNum

def subtract(firstNum, secondNum):
    return firstNum - secondNum

def multiply(firstNum, secondNum):
    return firstNum * secondNum

def divide(firstNum, secondNum):
    if secondNum == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    else:
        return firstNum / secondNum
  
# This function takes two numbers and an operator as input and returns the result of the arithmetic operation.

def scalc(firstNum, secondNum, operator=None):
    valid_operators = ["+", "-", "*", "/"]
    if operator is None:
        while True:
            operator = input("Enter an operator (+, -, *, /): ")
            if operator in valid_operators:
                break
            else:
                raise ValueError("Invalid operator.")
    if operator == "+":
        return add(firstNum, secondNum)
    elif operator == "-":
        return subtract(firstNum, secondNum)
    elif operator == "*":
        return multiply(firstNum, secondNum)
    elif operator == "/":
        return divide(firstNum, secondNum)
    else:
        raise ValueError("Invalid operator.")

# This function takes two numbers and returns the results of all arithmetic operations.    
def allInOne(firstNum, secondNum):
    return {
        "add": add(firstNum, secondNum),
        "subtract": subtract(firstNum, secondNum),
        "multiply": multiply(firstNum, secondNum),
        "divide": divide(firstNum, secondNum)
    }
