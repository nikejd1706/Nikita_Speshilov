import random
class User:
    def __init__(self, fname, lname, av = ""):
        self.firstname = fname
        self.lastname = lname
        self.avatar = av
        self.userid = random.randint(0, 1000000)

    def setValues(self, fname, lname, av, user):
        self.firstname = fname
        self.lastname = lname
        self.avatar = av
        self.userid = user

    def getfirstName(self):
        return self.firstname

    def getlastName(self):
        return self.lastname

    def getavatar(self):
        return self.avatar

    def getuserID(self):
        return self.userid
    
    def __str__(self):
        return "User information...\nFirst Name: " + self.firstname + \
                                   "\nLast Name: " + self.lastname + \
                                   "\nAvatar: " + self.avatar + \
                                   "\nUser ID#: " + str(self.userid)

def main():
    fname = input("Please enter your first name: ")
    lname = input("Please enter your last name: ")
    question = input("Would you like to use a public avatar? Type y for yes or n for no.")

    if question == "n":
        user1 = User(fname, lname)
    else:
        av = input("Please enter your desired avatar name: ")
        user1 = User(fname, lname, av)
    print(user1)
main()

                                          
                            
        
        
        
        
        
