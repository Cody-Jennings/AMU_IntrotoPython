# Program Name: Wk3.1_cody_jennings.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Correction Date: 20230430



#Welcome message to user
print("Welcome to Python Calculator V2!")


# Define functions for arithmetic operations
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

# Define function to check if a number is within a given range
def checknum(lb, n, ub):
    return lb < n < ub

def IsInRange(lr, hr, n):
    return checknum(lr, n, hr)

# Set the range limits
lr = -90
hr = 100

while True:
    # Prompt user for lower range until a valid input is provided
    while True:
        ulr = float(input("\nEnter your lower range between " + str(lr) + " and " + str(hr) + ": "))
        if checknum(lr, ulr, hr):
            break
        else:
            print("Invalid input. Please enter a number within the specified range.")

    # Prompt user for upper range until a valid input is provided
    while True:
        uhr = float(input("\nEnter your upper range between " + str(lr) + " and " + str(hr) + ": "))
        if checknum(lr, uhr, hr):
            break
        else:
            print("Invalid input. Please enter a number within the specified range.")

    # Prompt user for first number until a valid input is provided
    while True:
        num1 = float(input("\nEnter your first number between " + str(ulr) + " and " + str(uhr) + ": "))
        if IsInRange(ulr, uhr, num1):
            break
        else:
            print("Invalid input. Please enter a number within the specified range.")

    # Prompt user for second number until a valid input is provided
    while True:
        num2 = float(input("\nEnter your second number between " + str(ulr) + " and " + str(uhr) + ": "))
        if IsInRange(ulr, uhr, num2):
            break
        else:
            print("Invalid input. Please enter a number within the specified range.")

    # Calculate and display results using arithmetic functions
    print("\nThe Result of " + str(num1) + " + " + str(num2) + " = " + str(add(num1, num2)))
    print("The Result of " + str(num1) + " - " + str(num2) + " = " + str(sub(num1, num2)))
    print("The Result of " + str(num1) + " * " + str(num2) + " = " + str(mult(num1, num2)))
    if num2 != 0:
        print("The Result of " + str(num1) + " / " + str(num2) + " = " + str(div(num1, num2)))
    else:
        print("The Result of " + str(num1) + " / " + str(num2) + " = Can't divide by zero")

    # Prompt user to continue or exit
    while True:
        choice = input("\nDo you want to perform another calculation? (y/n): ")
        if choice == 'n':
            print("\nHave a nice day!")
            exit()
        elif choice == 'y':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
