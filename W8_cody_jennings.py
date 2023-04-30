# Program Name: W8_cody_jennings.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Correction Date: 20230430



# Importing Mylib module
import W8_cody_jennings_Mylib as W8cjm 

# Creating object from the Calculator class
finalCalc = W8cjm.Calculator()

# Creating object from the wrfile class
writeorread = W8cjm.wrfile()

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

    # Menu for allInOne function
    print("\nMENU:")
    print("1) Add first and second number")
    print("2) Subtract first and second number")
    print("3) Multiply first and second number")
    print("4) Divide first and second number")
    print("5) Use scalc on first and second number")
    print("6) Perform all operations using allInOne function on first and second number")
    print("\nWrite to a file will become an option if 1-6 are selected")
    print("Read from a file will become an option if 1-6 are selected")
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
        calc_result = finalCalc.add(firstNum,secondNum)
        print(f"\nThe result of {firstNum} {operator} {secondNum} = {calc_result}")
    elif menu_choice == "2":
        operator = "-"
        calc_result = finalCalc.subtract(firstNum,secondNum)
        print(f"\nThe result of {firstNum} {operator} {secondNum} = {calc_result}")
    elif menu_choice == "3":
        operator = "*"
        calc_result = finalCalc.multiply(firstNum,secondNum)
        print(f"\nThe result of {firstNum} {operator} {secondNum} = {calc_result}")
    elif menu_choice == "4":
        operator = "/"
        try:
            calc_result = finalCalc.divide(firstNum, secondNum)
            print(f"\nThe result of {firstNum} {operator} {secondNum} = {calc_result}")
        except ZeroDivisionError:
            calc_result = "You cannot divide by zero"
            print(f"\n{firstNum} {operator} {secondNum} = {calc_result}")

    elif menu_choice == "5":
        operator = input("\nEnter operator (+, -, *, /): ")
        try:
            calc_result = finalCalc.scalc(firstNum, secondNum, operator)
            print(f"\n{firstNum} {operator} {secondNum} = {calc_result}")
        except ZeroDivisionError:
            print(f"\n{firstNum} {operator} {secondNum} = You cannot divide by zero.")
    elif menu_choice == "6":
        try:
            all_in_one_result = finalCalc.allInOne(firstNum, secondNum)
            expression = f"The result of: {firstNum} + {secondNum} = {all_in_one_result['add']}\n"
            expression += f"The result of: {firstNum} - {secondNum} = {all_in_one_result['subtract']}\n"
            expression += f"The result of: {firstNum} * {secondNum} = {all_in_one_result['multiply']}\n"
            if secondNum == 0:
                expression += f"The result of: {firstNum} / {secondNum} = You cannot divide by zero\n"
            else:
                expression += f"The result of: {firstNum} / {secondNum} = {all_in_one_result['divide']}\n"
            with open("result.txt", "w") as file:
                file.write(expression)
            
            print(f"\nThe result of: {firstNum} + {secondNum} = {all_in_one_result['add']}")
            print(f"The result of: {firstNum} - {secondNum} = {all_in_one_result['subtract']}")
            print(f"The result of: {firstNum} * {secondNum} = {all_in_one_result['multiply']}")
            if secondNum == 0:
                print(f"The result of: {firstNum} / {secondNum} = You cannot divide by zero")
            else:
                print(f"The result of: {firstNum} / {secondNum} = {all_in_one_result['divide']}")
            
        except ZeroDivisionError:
            expression = f"The result of: {firstNum} + {secondNum} = {finalCalc.add(firstNum, secondNum)}\n"
            expression += f"The result of: {firstNum} - {secondNum} = {finalCalc.subtract(firstNum, secondNum)}\n"
            expression += f"The result of: {firstNum} * {secondNum} = {finalCalc.multiply(firstNum, secondNum)}\n"
            expression += f"The result of: {firstNum} / {secondNum} = You cannot divide by zero\n"
            with open("result.txt", "w") as file:
                file.write(expression)
            
            print(f"\nThe result of: {firstNum} + {secondNum} = {finalCalc.add(firstNum, secondNum)}")
            print(f"The result of: {firstNum} - {secondNum} = {finalCalc.subtract(firstNum, secondNum)}")
            print(f"The result of: {firstNum} * {secondNum} = {finalCalc.multiply(firstNum, secondNum)}")
            print(f"The result of: {firstNum} / {secondNum} = You cannot divide by zero")
            
        except TypeError:
            expression = f"The result of: {firstNum} + {secondNum} = {finalCalc.add(firstNum, secondNum)}\n"
            expression += f"The result of: {firstNum} - {secondNum} = {finalCalc.subtract(firstNum, secondNum)}\n"
            expression += f"The result of: {firstNum} * {secondNum} = {finalCalc.multiply(firstNum, secondNum)}\n"
            expression += f"The result of: {firstNum} / {secondNum} = Cannot divide by zero.\n"
            with open("result.txt", "w") as file:
                file.write(expression)
            
            print(f"\nThe result of: {firstNum} + {secondNum} = {finalCalc.add(firstNum, secondNum)}")
            print(f"The result of: {firstNum} - {secondNum} = {finalCalc.subtract(firstNum, secondNum)}")
            print(f"The result of: {firstNum} * {secondNum} = {finalCalc.multiply(firstNum, secondNum)}")
            print(f"The result of: {firstNum} / {secondNum} = Cannot divide by zero")

    # Secondary Menu
    print("\n Secondary MENU:")
    print("1) Write the result to a file")
    print("2) Read the result from a file")

    # User Input from menu choice 2
    while True:
        secondmenu_choice = input("\nEnter second menu choice (1-2): ") 
        if secondmenu_choice in ["1", "2"]: 
            break
        else:
            print("Invalid input. Please enter a number between 1 and 2.")

    # Perform selected operation based on user's menu choice
    if secondmenu_choice == "1":
        
        # Write to file       
        if menu_choice in ["1", "2", "3", "4", "5"]:
            expression = f"The result of {firstNum} {operator} {secondNum} = {calc_result}"
        elif menu_choice == "6":
            try:
                all_in_one_result = finalCalc.allInOne(firstNum, secondNum)
                expression = f"The result of: {firstNum} + {secondNum} = {all_in_one_result['add']}\n"
                expression += f"The result of: {firstNum} - {secondNum} = {all_in_one_result['subtract']}\n"
                expression += f"The result of: {firstNum} * {secondNum} = {all_in_one_result['multiply']}\n"
                if secondNum == 0:
                    expression += f"The result of: {firstNum} / {secondNum} = You cannot divide by zero\n"
                else:
                    expression += f"The result of: {firstNum} / {secondNum} = {all_in_one_result['divide']}\n"
            except ZeroDivisionError:
                expression = f"The result of: {firstNum} + {secondNum} = {finalCalc.add(firstNum, secondNum)}\n"
                expression += f"The result of: {firstNum} - {secondNum} = {finalCalc.subtract(firstNum, secondNum)}\n"
                expression += f"The result of: {firstNum} * {secondNum} = {finalCalc.multiply(firstNum, secondNum)}\n"
                expression += f"The result of: {firstNum} / {secondNum} = You cannot divide by zero\n"
        writeorread.write_to_file("result.txt", expression)
        print("\nUser input has been saved")
    elif secondmenu_choice == "2":
        # Read from file
        with open("result.txt", "r") as file:
            if menu_choice in ["1", "2", "3", "4", "5"]:
                operation = file.readline().strip()
                print("\nResult from file:")
                print(operation)
            elif menu_choice == "6":
                result = file.read()
                print("\nResult from file:")
                print(result)
        
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
