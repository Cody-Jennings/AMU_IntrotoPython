# Program Name: Wk3_cody_jennings.py
# Student Name: Cody Jennings
# Course: ENTD220
# Instructor: Ahmed Abaza
# Date: 20230325
# It seems I added what was to be done for week 3, last week. I added these loops and functions on my own to week 2s assignment when it was not required. Let me know if I need to edit this code since I already turned it in for week 2.


#Welcome message to user
print("Welcome to Python Calculator V2!")

#While loop to perform calculations based on user input
while True:
    
#User input
    lower_range_limit = float(input("\nEnter your Lower range (-90 thru 100):"))

#lower_range_limit Checks
    if int(lower_range_limit) < int(-90) or int(lower_range_limit) > int(100):
        print("Input values are outside set ranges!")
        print("Please check your numbers and try again.")
        print("\nThanks for using Python Calculator V2!")
    else:
        upper_range_limit = float(input("Enter your Higher range (-90 thru 100): "))

#upper_range_limit Checks
    if int(upper_range_limit) < int(-90) or int(upper_range_limit) > int(100):
        print("Input values are outside set ranges!")
        print("Please check your numbers and try again.")
        print("\nThanks for using Python Calculator V2!")
    else:
        firstNum = float(input(f"Enter your First number ({lower_range_limit} - {upper_range_limit}): "))
        secondNum = float(input(f"Enter your Second number ({lower_range_limit} - {upper_range_limit}): "))

#Input number checks
    if int(firstNum) < int(lower_range_limit) or int(firstNum) > int(upper_range_limit) or int(secondNum) < int(lower_range_limit) or int(secondNum) > int(upper_range_limit):
        print("\nInput values are outside set ranges!")
        print("Please check your numbers and try again.")
        print("\nThanks for using Python Calculator V2!")
    else:
        
#Values for each arithmetic operation
        print("\nThe result of: " + str(firstNum)+ " + " +str(secondNum)+ " = " +str(firstNum+secondNum))
        print("The result of: " + str(firstNum)+ " - " +str(secondNum)+ " = " +str(firstNum-secondNum))
        print("The result of: " + str(firstNum)+ " * " +str(secondNum)+ " = " +str(firstNum*secondNum))
        if firstNum == 0 or secondNum == 0:
            print("The result of: " + str(firstNum)+ " / " +str(secondNum)+ " = You cannot divide by zero")
            print("\nThanks for using Python Calculator V2!")
        else:
            print("The result of: " + str(firstNum)+ " / " +str(secondNum)+ " = " +str(firstNum/secondNum))
            print("\nThanks for using Python Calculator V2!")

#Nested while loop prompting user for additional calculations
    while True:
        choice = input("\nDo you want to perform another calculation? (y/n): ")
        
#User must input lowercase "y" or "n", if "y" then new calculation loop is started      
        if choice == 'y' or choice == 'n':
            break
        
#Improper value if anything else and prompted again
        else:
            print("Improper value. Please enter 'y' or 'n' in lowercase.")
            
#If "n", then loop is broken and goodbye message is displayed
    if choice == 'n':
        print("\nHave a nice day!")
        break

