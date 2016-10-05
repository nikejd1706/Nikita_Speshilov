def average():
    return((num1+num2+num3)/3)

def display():
    print("The average of {:.5f}, {:.5f}, {:.5f}, is {:.5f}.".format(num1, num2, num3, average()))



num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter another number: "))
num3 = float(input("Please enter a final number: "))

display()
             
