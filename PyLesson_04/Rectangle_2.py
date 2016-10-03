def setNums():
    output = "{:<6}{:6.2f}".format(length, width)
    global length, width
def calcPerim():
    global sum
    sum = (length*2)+(width*2)
    


length = float(input("Enter the length:"))
width = float(input("Ener the width:"))

setNums()
calcPerim()

print("The perimeter of your rectangle is",sum,)
