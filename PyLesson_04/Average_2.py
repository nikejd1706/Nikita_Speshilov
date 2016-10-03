def setNums():
    global num1, num2, num3
def average():
    global sum
    sum = ((num1+num2+num3))/3
    output = "{:<6}{:6.2f}".format(num1, num2, num3)

num1 = float(input("Please enter the first number:"))
num2 = float(input("Please enter the second number:"))
num3 = float(input("Please enter the third number:"))

setNums()
average()

print("The average of",num1,",",num2,",",num3,"is",sum,)
