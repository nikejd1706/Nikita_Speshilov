def calcArea():
    return((radius**2)*3.14)

def display():
    print("The area of a circle with a radius of {:.5f} is {:.5f}".format(radius,calcArea()))

radius = float(input("Please enter the radius of a circle:"))

display()
