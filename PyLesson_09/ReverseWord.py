myList = ["cheese", "money", "pizza", "trash", "football"]

print("In order....")

output = ""
for i in myList:
    output += i + " "
print(output)

print("\n________________")
print("Reversed....")


def reverse(myList):
    output = " "
    for i in range(len(myList),0,-1):
            output += myList[i-1] + " "
    print(output)

reverse(myList)
  

        
        

    
