# Program Name: W8_cody_jennings_Mylib.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Date: 20230430

# Class with calculator functions
class Calculator():
    
    def add(self, firstNum, secondNum):
        return firstNum + secondNum

    
    def subtract(self, firstNum, secondNum):
        return firstNum - secondNum

    
    def multiply(self, firstNum, secondNum):
        return firstNum * secondNum

    
    def divide(self, firstNum, secondNum):
        if secondNum == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        else:
            return firstNum / secondNum

# This function takes two numbers and an operator as input and returns the result of the arithmetic operation.   
    def scalc(self, firstNum, secondNum, operator):
        if operator == "+":
            return self.add(firstNum, secondNum)
        elif operator == "-":
            return self.subtract(firstNum, secondNum)
        elif operator == "*":
            return self.multiply(firstNum, secondNum)
        elif operator == "/":
            return self.divide(firstNum, secondNum)
        else:
            print ("Invalid operator.")

# This function takes two numbers and returns the results of all arithmetic operations.    
    def allInOne(self, firstNum, secondNum):
        return {
            "add": self.add(firstNum, secondNum),
            "subtract": self.subtract(firstNum, secondNum),
            "multiply": self.multiply(firstNum, secondNum),
            "divide": self.divide(firstNum, secondNum)
        }
    
# This class has two functions takes the results of the users input numbers and menu choices and writes to a txt file or reads from txt file. and returns the results of all arithmetic operations.
class wrfile():
    def write_to_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)

    def read_from_file(self, filename):
        with open(filename, 'r') as file:
            return file.read()
