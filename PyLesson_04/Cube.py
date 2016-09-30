def calcSurf(side):
    return((side**2)*6)
    


side = float(input("Please enter a side of the cube:"))
print("The surface area of a cube whose sides are",side,"in length is",calcSurf(side),".")
