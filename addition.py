
### Tell the user what the purpose is
##print("If you give me two numbers, I will tell you the sum.")
##
### Get two numbers from the user
##firstNumber = input("First number? ")
##secondNumber = input ("Second number? ")
##
### Convert the numbers to float
##firstNumber = float(firstNumber)
##secondNumber = float(secondNumber)
##
### Add the numbers
##total = firstNumber + secondNumber
##
### Display the result
##print("The sum is " , total)




# get percentage
percentage = input("Enter your percentage score: ")
percentageFloat = float(percentage)

# assign letter grade
if percentageFloat >= 90:
    grade = 'A'
elif percentageFloat >= 80:
    grade = 'B'
elif percentageFloat >= 70:
    grade = 'C'
elif percentageFloat >= 60 :
    grade = 'D'
elif percentageFloat >= 0:
    grade = 'F'
else:
    grade = "ERROR: A negative number was entered."


# display grad e
print("Your score of",percentage, "earned the letter grade" , grade)
