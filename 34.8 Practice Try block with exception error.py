"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts one integer input representing the index value of any of the string elements in the
following list:

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

Output the string element of the index value entered. The solution should be place in a try block and implement an
exception of "Error" if an incompatible integer input is provided.

The solution should be in the format:
frameworks_element

If the input is
2

Then the expected output is
CherryPy

Alternatively, if integerinput is 
7

Then the expected output is
Error
"""

frameworks = ["Django", "Flask", "CherryPy", "Bottle", "Web2Py", "TurboGears"]

#use try block with exception "Error" when index value is not found in list
#solution accepts an integer input
#solution outputs the corresponding string value for the integer input

user_input = int(input())

try:
    print(frameworks[user_input])

except:
    print("Error")