import argparse
import sys
parser = argparse.ArgumentParser(description = "MyGrades App")
args = parser.parse_args()
print(sys.argv)
if (len(sys.argv) == 1):
    print("Hi! This is the Grades app. It uses the command line. You must input at least one argument for it to work")
