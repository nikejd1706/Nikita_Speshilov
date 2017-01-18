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
    
        
    
    
