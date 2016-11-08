number = int(input("Please enter a number: "))
num = number
rev = 0

def getReverse():
    while num > 0:
        rev *= 10
        rev += 1
        num = int(num / 10)

print(number,"reversed is",rev)
    
