"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK: Create a solution that accepts an integer input to compare the following list:

predef_list = [4, -27, 15, 33, -10]

Output boolean value indicating whether the input value is greater than the maximum value from predef_list

The solution output should be in the format
Greater Than Max? Boolean_value

If the input is
20

Then the expected output is
Greater Than Max? False

"""

predef_list = [4, -27, 15, 33, -10]

#Get max value from list

max_value = max(predef_list)

#Get number input from user
user_number = int(input())

#Boolean Value
b_value = False

#If statement to get boolean value
if user_number > max_value:
    b_value = True
    print(f"Greater Than Max? {b_value}")

else:
    print(f"Greater Than Max? {b_value}")