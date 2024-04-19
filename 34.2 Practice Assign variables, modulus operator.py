"""
34.2 PRACTICE: Assign variables, modulus operator %

INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same
format as shown in the sample(s) below, inlcuding capitalization and whitespace.

TASK:
Create a solution that accepts an integer input representing any number of ounces. Output the converted total
number of tons, pounds, and remaining ounces based on the unput ounces value. There are 16 ounces in a pound
and 2,000 pounds in a ton.

The solution output should be in the format:

Tons: value_1
Pounds: values_2
Ounces: value_3

If the input is:
32035

Then the expected output is:
Tons: 1
Pounds: 2
Ounces: 3
"""

#There are 16 ounces in a pound and 2000 pounds in a ton
#Solution accepts an integer value representing any number of ounces
#Solution outputs the converted tons, pounds, and ounces represented by the input value of ounces

#Get amound of ounces with user
user_ounces = int(input())

#Calculations
total_pounds = user_ounces % 16
total_tons = user_ounces % 32000

print(total_pounds, total_tons)