import argparse
import sys
import actionClasses

class CommandLineParser:
    def parseit(self):
        # self.parser = argparse.ArgumentParser(description = "MyGrades App")
        # self.parser.add_argument("Activity", help = "Provide a command. Options: register, addGrade, getGrade, getResults")
        # self.args = self.parser.parse_args()
        # print(sys.argv)
        if (len(sys.argv) == 1):
            print("Hi! This is the Grades app. It uses the command line.")
            print("You must input at least one argument for it to work. Type 'python Main x', where x is one of 'register, 'addGrade', 'getGrade', 'getResults'.")
            print("Please try again.") 
            exit()
        if (len(sys.argv)>2):
            print("Too many arguments!")

        switcher = {
            'register':actionClasses.register(),
            'addGrade':actionClasses.addGrade(),
            'getGrade':actionClasses.getGrade(),
            'getResults':actionClasses.getResults(),
        }

        desired_action = switcher.get(sys.argv[1])
        return desired_action
        
        

        
        

