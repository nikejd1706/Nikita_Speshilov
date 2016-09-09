print("List your letter grades in every class that you take to calculate your GPA. Remember A=4 B=3 C=2 D=1 F=0")
first = int(input("What is your first period class grade?"))
second = int(input("What is your second period class grade?"))
third = int(input("What is your third period class grade?"))
fourth = int(input("What is your fourth period class grade?"))
fifth = int(input("What is your fifth period class grade?"))
sixth = int(input("What is your sixth period class grade?"))
classes = 6

print(first,"plus",second,"plus",third,"plus",fourth,"plus",fifth,"plus",sixth,"is" ,first+second+third+fourth+fifth+sixth)
totl =(first+second+third+fourth+fifth+sixth);
print(totl,"divided by " ,classes, "equals to" ,totl/classes,"GPA")

    
