import argparse
import sys
import actionClasses
import SignIn

class CommandLineParser:
    def parseit(self):
        # self.parser = argparse.ArgumentParser(description = "MyGrades App")
        # self.parser.add_argument("Activity", help = "Provide a command. Options: register, addGrade, getGrade, getResults")
        # self.args = self.parser.parse_args()
        # print(sys.argv)
        if (len(sys.argv) == 1):
            print("Hi! This is the Grades app. It uses the command line.")
            print("You must input at least one argument for it to work. Type 'python Main x', where x is one of 'Login' or 'Register'.")
            print("Please try again.") 
            exit()
        if (len(sys.argv)>2):
            print("Too many arguments!")
            exit()

        # switcher = {
        #     'register':SignIn.SignIn(),
        #     'addGrade':actionClasses.addGrade(),
        #     'getGrade':actionClasses.getGrade(),
        #     'getResults':actionClasses.getResults(),
        # }
        SignInScreen = SignIn.SignIn()
        if(sys.argv[1]== "Login"):
            SignInScreen.LogIn()
        elif(sys.argv[1]== "Register"):
            SignInScreen.CreateUser()
        else:
            print("Incorrect Command. Commands are either Login or Register")

        return







        # desired_action = switcher.get(sys.argv[1])
        # return desired_action
        
        

        
        

