# Program Name: Wk6_cody_jennings.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Date: 20230416


# Importing Mylib module
from Wk6_cody_jennings_Mylib import add, subtract, multiply, divide, scalc, allInOne

#Welcome message to user.
print("\nWelcome to Python Calculator V2!")

# While loop to perform calculations based on user input.
while True:
    
    # User input for lower range limit that traps errors that aren't within set/default range of -90 thru 100. This includes numbers/letters/words in any punctuation, user will be asked for input until acceptable input is give
    while True:
        try:
            lower_range_limit = float(input("\nEnter your Lower range (-90 thru 100): "))
            if lower_range_limit < -90 or lower_range_limit > 100:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between -90 and 100.")

    # User input for upper range limit that traps errors that aren't within set/default range of -90 thru 100. This includes numbers/letters/words in any punctuation, user will be asked for input until acceptable input is given.
    while True:
        try:
            upper_range_limit = float(input("\nEnter your Higher range (-90 thru 100): "))
            if upper_range_limit < -90 or upper_range_limit > 100:
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
        result = allInOne(firstNum, secondNum)["add"]
        print(f"\n{firstNum} + {secondNum} = {result}")
    elif menu_choice == "2":
        result = allInOne(firstNum, secondNum)["subtract"]
        print(f"\n{firstNum} - {secondNum} = {result}")
    elif menu_choice == "3":
        result = allInOne(firstNum, secondNum)["multiply"]
        print(f"\n{firstNum} * {secondNum} = {result}")
    elif menu_choice == "4":
        result = allInOne(firstNum, secondNum)["divide"]
        print(f"\n{firstNum} / {secondNum} = {result}")
    elif menu_choice == "5":
        operator = input("\nEnter operator (+, -, *, /): ")
        result = scalc(firstNum, secondNum, operator)
        if result == "\nCannot divide by zero.":
            print(result)
        else:
            print(f"\n{firstNum} {operator} {secondNum} = {result}")         
    elif menu_choice == "6":
        all_in_one_result = allInOne(firstNum, secondNum)
        print(f"\n{firstNum} + {secondNum} = {all_in_one_result['add']}")
        print(f"{firstNum} - {secondNum} = {all_in_one_result['subtract']}")
        print(f"{firstNum} * {secondNum} = {all_in_one_result['multiply']}")
        print(f"{firstNum} / {secondNum} = {all_in_one_result['divide']}")
    

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
