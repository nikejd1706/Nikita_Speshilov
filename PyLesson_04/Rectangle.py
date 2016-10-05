def perimeter():
    return((length+width)*2)
def display():
    print("Your rectangle is {:.5f} square feet".format(perimeter()))

length = float(input("Please enter the length of your rectangle:"))
width = float(input("Please enter the width of your rectangle:"))

display()


          
