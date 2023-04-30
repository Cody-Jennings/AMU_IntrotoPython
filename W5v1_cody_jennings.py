# Program Name: W5v1_cody_jennings.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Date: 20230429

# Importing Mylib module
from W5v1_cody_jennings_Mylib import add, subtract, multiply, divide, scalc

#Welcome message to user.
print("Welcome to Python Calculator V2!")

# Define constants for the range limits
lowerLimit = -90
upperLimit = 100

# While loop to perform calculations based on user input.
while True:
    
    # User input for lower range limit that traps errors that aren't within set/default range of -90 thru 100. This includes numbers/letters/words in any punctuation, user will be asked for input until acceptable input is give
    while True:
        try:
            lower_range_limit = float(input("\nEnter your Lower range (-90 thru 100): "))
            if lower_range_limit < lowerLimit or lower_range_limit > upperLimit:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between -90 and 100.")

    # User input for upper range limit that traps errors that aren't within set/default range of -90 thru 100. This includes numbers/letters/words in any punctuation, user will be asked for input until acceptable input is given.
    while True:
        try:
            upper_range_limit = float(input("\nEnter your Higher range (-90 thru 100): "))
            if upper_range_limit < lowerLimit or upper_range_limit > upperLimit:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between -90 and 100.")

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

    # User input for operation.
    operator = input("\nEnter operator (+, -, *, /): ")

    # Perform arithmetic operations and display results.
    result = scalc(firstNum, secondNum, operator)
    if result == "\nCannot divide by zero.":
        print(result)
    else:
        print(f"\n{firstNum} {operator} {secondNum} = {result}")
    


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
