to = int(input("Please enter the number you want to count to: "))
by = int(input("Please enter the number you want to count by: "))

output = ""
for i in range(by, to+1, by):
    output = output + str(i) + " "
print(output)
        



