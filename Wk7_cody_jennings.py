# Program Name: Wk7_cody_jennings.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Correction Date: 20230429


# Importing Mylib module
import Wk7_cody_jennings_Mylib as W7cjm 

#creating object from the class
finalCalc = W7cjm.Calculator()

#Welcome message to user.
print("\nWelcome to Python Calculator V2!")

# Define constants for the range limits
lowerLimit = -90
upperLimit = 100

# While loop to perform calculations based on user input.
while True:
    
    # User input for lower range limit that traps errors that aren't within set/default range of -90 thru 100. This includes numbers/letters/words in any punctuation, user will be asked for input until acceptable input is give
    while True:
        try:
            lower_range_limit = float(input(f"\nEnter your Lower range ({lowerLimit} thru {upperLimit}): "))
            if lower_range_limit < lowerLimit or lower_range_limit > upperLimit:
                raise ValueError
            break
        except ValueError:
            print(f"Invalid input. Please enter a number between {lowerLimit} thru {upperLimit}.")

    # User input for upper range limit that traps errors that aren't within set/default range of -90 thru 100. This includes numbers/letters/words in any punctuation, user will be asked for input until acceptable input is given.
    while True:
        try:
            upper_range_limit = float(input(f"\nEnter your Higher range ({lowerLimit} thru {upperLimit}): "))
            if upper_range_limit < lowerLimit or upper_range_limit > upperLimit:
                raise ValueError
            break
        except ValueError:
            print(f"Invalid input. Please enter a number between {lowerLimit} thru {upperLimit}.")

    # User input for first number that traps errors that aren't within user's input range limits. This includes numbers/letters/words in any punctuation, user will be asked for input until acceptable input is given.
    while True:
        try:
            firstNum = float(input(f"\nEnter your First number ({lower_range_limit} - {upper_range_limit}): "))
            if firstNum < lower_range_limit or firstNum > upper_range_limit:
                raise ValueError
            break
        except ValueError:
            print(f"Invalid input. Please enter a number between ({lower_range_limit} - {upper_range_limit})")

    # User input for second number that traps errors that aren't within user's input range limits. This includes numbers/letters/words in any punctuation, user will be asked for input until acceptable input is given.
    while True:
        try:
            secondNum = float(input(f"\nEnter your Second number ({lower_range_limit} - {upper_range_limit}): "))
            if secondNum < lower_range_limit or secondNum > upper_range_limit:
                raise ValueError
            break
        except ValueError:
            print(f"Invalid input. Please enter a number between ({lower_range_limit} - {upper_range_limit})")

    # Menu for allInOne function
    print("\nMENU:")
    print("1) Add first and second number")
    print("2) Subtract first and second number")
    print("3) Multiply first and second number")
    print("4) Divide first and second number")
    print("5) Use scalc on first and second number")
    print("6) Perform all operations using allInOne function on first and second number")

    # User input for menu choice
    while True:
        menu_choice = input("\nEnter menu choice (1-6): ") 
        if menu_choice in ["1", "2", "3", "4", "5", "6"]:  
            break
        else:
            print("Invalid input. Please enter a number between 1 and 6.") 

    # Perform selected operation based on user's menu choice
    if menu_choice == "1":
        operator = "+"
        sum = finalCalc.add(firstNum,secondNum)
        print(f"\nThe result of {firstNum} {operator} {secondNum} = {sum}")
    elif menu_choice == "2":
        operator = "-"
        sum = finalCalc.subtract(firstNum,secondNum)
        print(f"\nThe result of {firstNum} {operator} {secondNum} = {sum}")
    elif menu_choice == "3":
        operator = "*"
        sum = finalCalc.multiply(firstNum,secondNum)
        print(f"\nThe result of {firstNum} {operator} {secondNum} = {sum}")
    elif menu_choice == "4":
        operator = "/"
        try:
            sum = finalCalc.divide(firstNum, secondNum)
            print(f"\nThe result of {firstNum} {operator} {secondNum} = {sum}")
        except ZeroDivisionError:
            print(f"\n{firstNum} {operator} {secondNum} = You cannot divide by zero.")
    elif menu_choice == "5":
        while True:
            operator = input("\nEnter operator (+, -, *, /): ")
            try:
                sum = finalCalc.scalc(firstNum, secondNum, operator)
                print(f"\n{firstNum} {operator} {secondNum} = {sum}")
                break
            except ZeroDivisionError:
                print(f"\n{firstNum} {operator} {secondNum} = You cannot divide by zero.")
                break
            except ValueError as err:
                print(err)
    elif menu_choice == "6":
        try:
            all_in_one_result = finalCalc.allInOne(firstNum, secondNum)
            print(f"\nThe result of: {firstNum} + {secondNum} = {all_in_one_result['add']}")
            print(f"The result of: {firstNum} - {secondNum} = {all_in_one_result['subtract']}")
            print(f"The result of: {firstNum} * {secondNum} = {all_in_one_result['multiply']}")
            if secondNum == 0:
                print(f"The result of: {firstNum} / {secondNum} = You cannot divide by zero")
            else:
                print(f"The result of: {firstNum} / {secondNum} = {all_in_one_result['divide']}")
        except ZeroDivisionError:
            print(f"\nThe result of: {firstNum} + {secondNum} = {finalCalc.add(firstNum, secondNum)}")
            print(f"The result of: {firstNum} - {secondNum} = {finalCalc.subtract(firstNum, secondNum)}")
            print(f"The result of: {firstNum} * {secondNum} = {finalCalc.multiply(firstNum, secondNum)}")
            print(f"The result of: {firstNum} / {secondNum} = You cannot divide by zero")
        except TypeError:
            print(f"\nThe result of: {firstNum} + {secondNum} = {finalCalc.add(firstNum, secondNum)}")
            print(f"The result of: {firstNum} - {secondNum} = {finalCalc.subtract(firstNum, secondNum)}")
            print(f"The result of: {firstNum} * {secondNum} = {finalCalc.multiply(firstNum, secondNum)}")
            print(f"The result of: {firstNum} / {secondNum} = Cannot divide by zero.")

   
# Ask user if they want to perform another calculation. Displaying error if lower "y" or "n" is not selected, this includes numbers/letters/words in any punctuation, user will be asked for input until acceptable input is given.
    while True:
        choice = input("\nDo you want to perform another calculation? (y/n): ")
        if choice == 'y' or choice == 'n':
            break
        else:
            print("Improper value. Please enter 'y' or 'n' in lowercase.")

# If "n", then break the loop and display goodbye message.
    if choice == 'n':
        print("\nThanks for using Python Calculator V2!")
        break

