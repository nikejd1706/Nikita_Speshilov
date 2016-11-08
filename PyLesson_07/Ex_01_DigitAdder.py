number = int(input("Please enter a number: "))
summ = 0;
num = number

while num > 0:
    summ += num%10
    num = int(num / 10)
print("The sum of the digits in",number,"is",summ)
        
    
