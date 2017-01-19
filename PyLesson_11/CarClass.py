class Car:
    def __init__(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    def setValues(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    def getPaint(self):
        return self.paint

    def getInterior(self):
        return self.interior

    def getEngine(self):
        return self.engine

    def getTires(self):
        return self.tires

def main():
    p = input("Please enter the desired paint: ")
    i = input("Please enter the desired interior: ")
    e = input("Please enter the desired engine: ")
    t = input("Please enter the desired tires: ")

    newcar = Car(p, i, e, t)

    print("Your vehicle is ready....")
    print("Paint: ", newcar.getPaint())
    print("Interior: ", newcar.getInterior())
    print("Engine: ", newcar.getEngine())
    print("Tires: ", newcar.getTires())

main()
    
    
