

def format(info, info1):
    print("{:<10}\t{:10}".format(info, info1))


info1 = input("Enter your first name:")
info2 = input("Enter your last name:")
info3 = input("Enter your title:")
info4 = input("Enter the school site:")
info5 = input("Enter the school year:")
info6 = input("What is your subject?")

print("*" * 20)
format(info4, info5)
format(info1, info2)
format(info3, info6)
print("*" * 20)
