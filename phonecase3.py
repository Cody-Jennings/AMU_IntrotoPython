

class phonecase:
    def __init__(self,number = 0, brand = "", model = ""):
        self.numberInStock = number
        self.brand = brand
        self.model = model

    def newShipment(self, numCases):
        self.numberInStock = self.numberInStock + numCases

    def soldCase(self, numSold):
        self.numberInStock = self.numberInStock - numSold

    def getNumberInStock(self):
        return self.numberInStock

    def setNumberInStock(self, num):
        self.numberInStock = num

    def getBrand(self):
        return self.brand

    def setBrand(self, brand):
        self.brand = brand

    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    def __str__(self):
        return str(self.numberInStock)+ " of " + self.brand + ":" + self.model

class SamsungCase(phonecase):
    def __init__(self, num = 0, model=""):
        self.numberInStock = num
        self.model = model
        self.brand = "Samsung"

    def setBrand(self,brand):
        print ("Sorry, this will always be Samsung.")
