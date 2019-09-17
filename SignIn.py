import actionClasses
import database

class SignIn(actionClasses.action):
    name = 'placeholder'
    username = 'placeholder'
    password = 'placeholder'

    # def __init__(self, name, username, password):
    #     self.name = name
    #     self.username = username
    #     self.password = password

     #inherits action class
    def begin(self):
        print("You have arrived at the Registration page. Welcome!")
        print("Press 1 to login, 2 to register as a new user, or 3 to quit")
        while (1):
            x = int(input())
            if x==1 or x==2:
                break
            elif x ==3:
                exit()
            else:
                print("Please press either 1, 2 or 3!")
        if x == 2:
            self.CreateUser()


    def CreateUser(self):
        print('Hi! Whats your name?')
        self.name = input()
        print('Type in a username.')
        self.username = input()
        print('And now a nice complicated password')
        self.password = input()
        #make_user

        




        

        

