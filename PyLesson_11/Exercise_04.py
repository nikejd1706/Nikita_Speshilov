class Human:
    def __init__(self, h, e, s):
        self.hair = h
        self.eyes = e
        self.skin = s

    def setHES(self, h, e, s):
        self.hair = h
        self.eyes = e
        self.skin = s

    def getHair(self):
        return self.hair

    def getEyes(self):
        return self.eyes

    def getSkin(self):
        return self.skin

def main():
    h = input("Please enter the hair color: ")
    e = input("Please enter the eye color: ")
    s = input("Please enter the skin color: ")

    newhuman = Human(h, e, s)

    print("My info...")
    print("Hair: ", newhuman.getHair())
    print("Eyes: ", newhuman.getEyes())
    print("Skin: ", newhuman.getSkin())

    newhuman.setHES("blonde", "Green", "Tan")

    print("Friend's info....")
    print("Hair: ", newhuman.getHair())
    print("Eyes: ", newhuman.getEyes())
    print("Skin: ", newhuman.getSkin())

main()
    
    
    
    
    
