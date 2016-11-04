string = input("Please enter a String: ")

def printString():
    for i in range(0,len(string),1):
        print(string[i:len(string)])
printString()
