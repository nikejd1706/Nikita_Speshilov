number = int(input("Please enter a number: "))
digits = 0
num = number


while num > 0:
    digits += 1
    num = int(num / 10)

print("There are ", digits, " digits in ", number)

