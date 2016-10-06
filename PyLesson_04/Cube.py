def calcSurf():
    return((side**2)*6)
def display():
    print("The surface area of a cube whose sides are {:.5f} in length is {:.5f}".format(side,calcSurf()))
        

side = float(input("Please enter a side of the cube:"))

display()
