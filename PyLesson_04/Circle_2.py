def setNums():
    global radius
def calcArea():
    global sum
    sum = ((radius**2)*3.14)

radius = float(input("Please enter the radius of your circles:"))

setNums()
calcArea()

print("The area of your circle with a radius {:.5f} is {:.5f}".format(radius,sum))
