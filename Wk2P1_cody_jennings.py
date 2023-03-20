# Program Name: Wk2P1_cody_jennings.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Date: 20230318

# A simple calculator to accept two numbers and print the addition, subtraction, multiplication, and division of the two numbers.
# You are required to store each input number in a separate variable.


#Welcome message to user
print("Welcome to Python Calculator!")

#while loop to perform calculations based of user input
while True:
#user input values for all integers including decimals, negatives, etc   
    print("\nEnter First Number: ")
    firstNum = float(input())
    print("Enter Second Number: ")
    secondNum = float(input())
#values for each arithmatic operation    
    print("\nThe result of: " + str(firstNum)+ " + " +str(secondNum)+ " = " +str(firstNum+secondNum))
    print("The result of: " + str(firstNum)+ " - " +str(secondNum)+ " = " +str(firstNum-secondNum))
    print("The result of: " + str(firstNum)+ " * " +str(secondNum)+ " = " +str(firstNum*secondNum))
    print("The result of: " + str(firstNum)+ " / " +str(secondNum)+ " = " +str(firstNum/secondNum))
#nested while loop prompting user for additional calculations
    while True:
        choice = input("\nDo you want to perform another calculation? (y/n): ")
#user must input lowercase "y" or "n", if "y" then new calculation loop is started      
        if choice == 'y' or choice == 'n':
            break
#improper value if anything else and prompted again
        else:
            print("Improper value. Please enter 'y' or 'n' in lowercase.")
#if "n", then loop is broken and goodbye message is displayed
    if choice == 'n':
        print("\nHave a nice day!")
        break
