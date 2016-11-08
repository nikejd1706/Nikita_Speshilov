number = int(input("Please enter a number: "))
digits = 0
average = 0
num = number
summ = 0

while num > 0:
    summ += num % 10
    digits += 1
    num = int(num / 10)
average = summ / digits
print("The average of the digits in",number,"is",average)

