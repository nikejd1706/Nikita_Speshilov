string = input("Please enter a String: ")

def printString():
    for i in range(len(string),0,-1):
        print(string[i:len(string)])
printString()
