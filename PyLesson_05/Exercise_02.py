global subtotal, disc, total

subtotal = 0;
disc = 0;
total = 0; 

def format (item, pr):
    print("*  {:<15}......${:10.2f}".format(item, pr))

def discount():
    #use the global keyword here to ensure that
    #python is using the global variable and not
    #creating a new one

    
    if subtotal >= 2000:
        disc = subtotal*0.15;
    if subtotal < 2000:
        disc = 0;


item1 = input("Please enter item 1:")
price1 = float(input("Please enter the price:"))

item2 = input("Please enter item 2:")
price2 = float(input("Please enter the price:"))

item3 = input("Please enter item 3:")
price3 = float(input("Please enter the price:"))

item4 = input("Please enter item 4:")
price4 = float(input("Please enter the price:"))

subtotal = price1+price2+price3+price4
print(subtotal)

discount()
tax = subtotal*.08
total = subtotal- disc + tax

print("          <<<<<_receipt_>>>>>          ")
format(item1, price1)
format(item2, price2)
format(item3, price3)
format(item4, price4)

format("Subtotal: ", subtotal)
format("Discount: ", disc)
print("_________________________________________")
print("Thank you for shopping!")


