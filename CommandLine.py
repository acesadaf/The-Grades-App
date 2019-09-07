import argparse
import sys
class CommandExecutor:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description = "MyGrades App")
        self.args = self.parser.parse_args()
        print(sys.argv)
        if (len(sys.argv) == 1):
            print("Hi! This is the Grades app. It uses the command line. You must input at least one argument for it to work")

