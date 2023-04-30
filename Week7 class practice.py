class myListClass:
    def __init__(self, aList):
        self.myList = aList         

    def __add__ (self, other):
        # the __add__ method is used to define how + works
        instanceSum = 0
        for n in self.myList:
            instanceSum = instanceSum + n
        for n in other.myList:
            instanceSum = instanceSum + n
        return instanceSum

oneList = [3, 5, 7]
otherList = [10,20]
myListA = myListClass(oneList)
myListB = myListClass(otherList)
sum = myListA + myListB
print(sum)
