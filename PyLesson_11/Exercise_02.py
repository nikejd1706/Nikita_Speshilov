import math
class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.x1c = x1
        self.y1c = y1
        self.x2c = x2
        self.y2c = y2
        self.distance = 0

    def setValues(self, x1, y1, x2, y2):
        self.x1c = x1
        self.y1c = y1
        self.x2c = x2
        self.y2c = y2
        self.distance = 0

    def getMPH(self):
        return math.sqrt((self.x2c-self.x1c)*(self.x2c-self.x1c)+(self.y2c-self.y1c)*(self.y2c-self.y1c))
        

def main():
    x1 = int(input("Please enter the first x value: "))
    y1 = int(input("Please enter the first y value: "))
    x2 = int(input("Please enter the second x value: "))
    y2 = int(input("Please enter the second y value: "))

    distance = Distance(x1, y1, x2, y2)

    print("distance =", distance.getMPH())

main()
        
        
        
