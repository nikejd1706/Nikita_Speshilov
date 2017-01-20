import random
class Item:
    def __init__(self, manuf, name, categ = "", price = ""):
        self.manufacturer = manuf
        self.itemname = name
        self.itemcategory = categ
        self.itemprice = price
        self.UPC = random.randint(1000000000, 9999999999)

    def setValues(self, manuf, name, categ, price, UPC):
        self.manufacturer = manuf
        self.itemname = name
        self.itemcategory = categ
        self.itemprice = price
        self.UPC = upcNum

    def getManufacturer(self):
        return self.manufacturer

    def getitemName(self):
        return self.itemname

    def getCategory(self):
        return self.itemcategory

    def getPrice(self):
        return self.itemprice

    def getUPC(self):
        return self.UPC

    def __str__(self):
        return "Item information...\nItem Manufacturer: " + self.manufacturer + \
                                   "\nItem Name: " + self.itemname + \
                                   "\nItem Category: " + self.itemcategory + \
                                   "\nItem Price: " + str(self.itemprice) + \
                                   "\nUPC: " + str(self.UPC)

def main():
    manuf = input("Please enter the item manufacturer: ")
    name = input("Please enter the item name: ")
    question = input("Will you be entering category and price information? Type y for yes or n for no.")

    if question == "n":
        item1 = Item(manuf, name)
    else:
        categ = input("Please enter the item category: ")
        price = float(input("Please enter the item price: "))
        item1 = Item(manuf, name, categ, price)
    print(item1)
main()
