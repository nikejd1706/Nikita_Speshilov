username1 = "robot"
password1 = "jump"

def passCheck():
    username = input("Please enter the username: ")
    password = input("Please enter the password: ")
    
    if username == username1 and password == password1:
        print("You are granted access!")
    else:
        if username == username1:
            
            print("Your password is incorrect!")
            passCheck()
        elif password == password1:
            print("Your username is incorrect!")
            passCheck()
        else:
            print("Your username and password are incorrect!")
            passCheck()

passCheck()



    
    
    
