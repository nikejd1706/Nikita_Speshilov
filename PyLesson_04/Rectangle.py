def perimeter():
    return((length+width)*2)
def display():
    print("Your rectangle is%8.2F"%perimeter(),"sq ft around.")
    



length = float(input("Please enter the length of your rectangle:"))
width = float(input("Please enter the width of your rectangle:"))

display()


          
