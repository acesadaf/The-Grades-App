import actionClasses
import database
import Main_Menu

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
            if x==1:
                self.LogIn()
                
            elif x ==3:
                exit()
            else:
                print("Please press either 1, 2 or 3!")
            if x == 2:
                self.CreateUser()


    def CreateUser(self):
        conn = database.create_connection()
        MyCursor = conn.cursor()

        print('Hi! Whats your name?')
        self.name = input()
        already_exists = True
        while(already_exists!=False):
            print('Type in a username.')
            self.username = input()
            CheckString = "Select * from Users where username = '{}'".format(self.username)
            MyCursor.execute(CheckString)
            rows = MyCursor.fetchall()
            if(len(rows) == 0):
                already_exists = False
            else:
                print('Sorry, this username already exists. Please try something else.')     

        print('Great! Now key in a nice complicated password.')
        
        self.password = input()
        
        InsertString = "insert into Users values('{}', '{}', '{}')".format(self.username, self.name, self.password)
        conn.execute(InsertString)
        conn.commit()
        database.close_connection(conn)
        #make_user

    def LogIn(self):
        conn = database.create_connection()
        print('Type in your username.')
        self.username = input()
        print('Type in your password.')
        self.password = input()
        CheckString = "Select * from Users where username = '{}' and password = '{}'".format(self.username, self.password)
        MyCursor = conn.cursor()
        MyCursor.execute(CheckString)
        rows = MyCursor.fetchall()
        database.close_connection(conn)
        if(len(rows)==1):
            print("Success!")
            print("Welcome, {}".format(self.username))
            Menu = Main_Menu.Main_Menu(self.username)
        else:
            print("Username/Password doesn't match")
            print("Press 1 to try again, 2 to quit")
            key="placeholder"
            while (1):
                key = input()
                if(key =='1' or key =='2'):
                    break 
                else:
                    print('Enter either 1 or 2')
            if key == '1':
                self.LogIn()
            else:
                quit() 
        




        




        

        

