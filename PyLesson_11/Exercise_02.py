import math

class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.x1coordinate = x1
        self.y1coordinate = y1
        self.x2coordinate = x2
        self.y2coordinate = y2

    def setValues(self, x1, y1, x2, y2):
        self.x1coordinate = x1
        self.y1coordinate = y1
        self.x2coordinate = x2
        self.y2coordinate = y2

    def getDist(self):
        dist = Math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
        return dist

def main():
    x1 = int(input("Please enter the first x value: "))
    y1 = int(input("Please enter the first y value: "))
    x2 = int(input("Please enter the second x value: "))
    y1 = int(input("Please enter the second y value: "))

    newDistance = Distance(x1coordinate, y1coordinate, x2coordinate, y2coordinate)

    print("distance =" newDistance.getDist()".")

main()
        
        
        
