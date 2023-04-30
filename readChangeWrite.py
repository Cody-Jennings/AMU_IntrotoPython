

import csv
outStr = ""
lineStr = ""
with open("food.txt","r", newline="\n") as inFile:
    myReader = csv.reader(inFile)
    for item in myReader:
        oldCost = item[1]
        oldCost = float(oldCost)
        newCost = oldCost * 1.25
        lineStr = "{0}, {1}".format(item[0],newCost)
        lineStr = lineStr + "\n"
        outStr = outStr + lineStr
inFile.close()

#write
with open("foodNew.txt","w") as outFile:
    outFile.write(outStr)
outFile.close()

'''


import os

os.remove("food.txt")
print ("Food.txt was removed")  this deletes a file
'''
