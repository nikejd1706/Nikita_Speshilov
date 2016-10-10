def format (item, price):
    print("{:<15}{:10.2f}".format(item, price))

def discount1():
    global price
    if price >= 2000:
        return "Your discount is",subtotal^.15,"$"
    if price < 2000:
        return "0$"

    
item1 = input("Please enter item 1:")
price1 = float(input("Please enter the price:"))

item2 = input("Please enter item 2:")
price2 = float(input("Please enter the price:"))

item3 = input("Please enter item 3:")
price3 = float(input("Please enter the price:"))

item4 = input("Please enter item 4:")
price4 = float(input("Please enter the price:"))

subtotal = price1+price2+price3+price4
discount = discount1()
tax = (subtotal-discount)^.08
total = subtotal-discount+tax

print("          <<<<<_receipt_>>>>>          ")
format(item1, price1)
format(item2, price2)
format(item3, price3)
format(item4, price4)

format("Subtotal: ", subtotal)
format("Discount: ", discount)
print("_________________________________________")
print("Thank you for shopping!")


