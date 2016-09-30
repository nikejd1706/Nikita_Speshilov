def calcArea(radius):
    return((radius**2)*3.14)

radius = float(input("Please enter the radius of a circle:"))
print("The area of a circle with a radius of",radius,"is",calcArea(radius),".")
