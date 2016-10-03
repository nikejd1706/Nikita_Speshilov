def calcSurf():
    return((side**2)*6)
def display():
    print("The surface area of a cube whose sides are",side,"in length is",calcSurf(),".")
    

    


side = float(input("Please enter a side of the cube:"))

display()
