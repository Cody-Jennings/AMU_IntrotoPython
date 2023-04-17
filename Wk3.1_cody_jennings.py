# Program Name: Wk3.1_cody_jennings.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Correction Date: 20230411

#I believe this is more along the lines of what the assignment syntax was asking. Thank you for this opportunity and let me know if it is still incorrect.

#Welcome message to user
print("Welcome to Python Calculator V2!")

# Define functions for arithmetic options
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

while True:
    # Get lower and upper range limit from user input
    lr = -90
    hr = 100
    ulr = float(input("\nEnter your lower range between " + str(lr) + " and " + str(hr) + ": "))
    uhr = float(input("Enter your upper range between " + str(lr) + " and " + str(hr) + ": "))

    # Check if user input ranges are within limit range
    if checknum(lr, ulr, hr) and checknum(lr, uhr, hr):
        # Get first and second numbers from user input
        num1 = float(input("Enter your first number between " + str(ulr) + " and " + str(uhr) + ": "))
        num2 = float(input("Enter your second number between " + str(ulr) + " and " + str(uhr) + ": "))

        # Check if first and second numbers are within user input ranges
        if checknum(ulr, num1, uhr) and checknum(ulr, num2, uhr):
            # Calculate and display results using arithmetic functions
            print("\nThe Result of " + str(num1) + " + " + str(num2) + " = " + str(add(num1, num2)))
            print("The Result of " + str(num1) + " - " + str(num2) + " = " + str(sub(num1, num2)))
            print("The Result of " + str(num1) + " * " + str(num2) + " = " + str(mult(num1, num2)))
            if num2 != 0:
                print("The Result of " + str(num1) + " / " + str(num2) + " = " + str(div(num1, num2)))
            else:
                print("The Result of " + str(num1) + " / " + str(num2) + " = Can't divide by zero")
        else:
            print("\nInput values are outside set ranges!")
            print("Please check your numbers and try again.")
    else:
        print("\nInput ranges are outside limit ranges!")
        print("Please check your ranges and try again.")

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
