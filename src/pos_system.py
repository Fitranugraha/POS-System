
class Item:
    def __init__(self, name, price, tax):
        self.name = name
        self.price = price
        self.tax = tax

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getTax(self):
        return self.tax

class BuyList:
    def __init__(self):
        self.buy_list = []
        self.total = 0

    def addItem(self, item_name, price):
        self.buy_list.append(Item(item_name, price, 0.1))

    def removeItem(self, item_name):
        for item in self.buy_list:
            if(item.getName() == item_name):
                self.buy_list.remove(item)

    def getAllItems(self):
        return self.buy_list

    def getTotalPrice(self):
        total_price = 0
        for product in self.buy_list:
            total_price += product.getPrice() + product.getPrice() * product.getTax()

        return total_price

class POS:

    def __init__(self):
        self.user = ""

    def setUser(self):
        return self

    def getUser(self):
        return self.user

    def newBuyList(self):
        self.buyList = BuyList()

    def getBuyList(self):
        return self.buyList

    def printBuyList(self):
        i = self.buyList.getAllItems()
        for item in i:
            print(item.getName())
            print(item.getPrice())
            print(item.getTax())
            print(" ")
