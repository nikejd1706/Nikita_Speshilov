def average():
    output = "{:<6}{:6.2f}".format(num1, num2, num3)
    return((num1+num2+num3)/3)
def display():
    print("The average of",num1,",",num2,",",num3,"is",average(),".")



num1 = float(input("Please enter a number:"))
num2 = float(input("Please enter another number:"))
num3 = float(input("Please enter a final number:"))

display()
             
