integer = int(input("Please enter an integer: "))
size = int(input("Please enter the size of the table: "))

def graphTable():
    for i in range(1, size):
        print(i,i*integer)
graphTable()

