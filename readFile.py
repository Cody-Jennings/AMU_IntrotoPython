
'''
import csv

with open("food.txt","r") as inFile:
    strIn = inFile.read()
    print (strIn)
inFile.close()
'''


import csv

with open("food.txt","r", newline="\n") as inFile:
    myReader = csv.reader(inFile)
    for item in myReader:
        print(item)
inFile.close()

