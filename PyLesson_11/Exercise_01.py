class MilesPerHour:
    def __init__(self, d, h, m):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0

    def setValues(self, d, h, m):
        self.distance = d
        self.hours = h
        self.minutes = m
        self.mph = 0
        

    def getDist(self):
        return self.distance
    def getHours(self):
        return self.hours
    def getMins(self):
        return self.minutes
    def getMPH(self):
        return self.distance/ (self.hours + self.minutes / 60.0)

def main():
    distance = int(input("Please enter the distance: "))
    hours = int(input("Please enter the hours: "))
    minutes = int(input("Please enter the minutes: "))

    speed = MilesPerHour(self, d, h, m)

    print("")
    
    
    
    
