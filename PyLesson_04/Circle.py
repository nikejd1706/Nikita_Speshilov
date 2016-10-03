def calcArea(radius):
    return((radius**2)*3.14)
def display():
    print("The area of a circle with a radius of",radius,"is",calcArea(radius),".")

radius = float(input("Please enter the radius of a circle:"))

display()
