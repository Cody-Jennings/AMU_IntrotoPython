print("Use LA for a liberal arts major and S for a science major.")
major=input("What is your major? ")
print()
##Ask user first letter or last name
letter=input("Enter the first letter of your last name. Please use uppercase: ")
if major == "LA":
    if letter < "L":
        floor = 1
    else:
        floor = 2
elif major == "S":
    if letter < "L":
        floor = 3
    else:
        floor = 4
else:
    floor = 5
if floor < 5:
    print ("You room is on floor", floor)
else:
    print ("You did not enter valid information.") 
