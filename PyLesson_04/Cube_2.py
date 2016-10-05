def setNums():
    global side
def surfaceArea():
    global sum
    sum = ((side**2)*6)
   

side = float(input("Please enter the side of a cube to calculate the surface area:"))

setNums()
surfaceArea()
        

print("The surface area of a cube whose sides are {:.5f} is {:.5f}".format(side,sum))
