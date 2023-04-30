# Program Name: Wk7_cody_jennings_Mylib.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Correction Date: 20230430


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
    def scalc(self, firstNum, secondNum, operator=None):
        valid_operators = ["+", "-", "*", "/"]
        if operator is None:
            while True:
                operator = input("Enter an operator (+, -, *, /): ")
                if operator in valid_operators:
                    break
                else:
                    raise ValueError("Invalid operator.")
        if operator == "+":
            return self.add(firstNum, secondNum)
        elif operator == "-":
            return self.subtract(firstNum, secondNum)
        elif operator == "*":
            return self.multiply(firstNum, secondNum)
        elif operator == "/":
            return self.divide(firstNum, secondNum)
        else:
            raise ValueError("Invalid operator.")

# This function takes two numbers and returns the results of all arithmetic operations.    
    def allInOne(self, firstNum, secondNum):
        return {
            "add": self.add(firstNum, secondNum),
            "subtract": self.subtract(firstNum, secondNum),
            "multiply": self.multiply(firstNum, secondNum),
            "divide": self.divide(firstNum, secondNum)
        }



