'''foodPricePairs = [['pear', 0.80],['celery', 0.50],['apple',0.50]]

for item in foodPricePairs:
    lineStr = "{0}, {1}".format(item[0],item[1])
    print(lineStr)
    '''


import csv

foodPricePairs = [['pear', 0.80],['celery', 0.50],['apple',0.50]]

with open("food3.txt","a") as outFile:
    for item in foodPricePairs:
        lineStr = "{0}, {1}".format(item[0],item[1])
        lineStr = lineStr + "\n"
        outFile.write(lineStr )
outFile.close()
print ("Saved in food3.txt")
