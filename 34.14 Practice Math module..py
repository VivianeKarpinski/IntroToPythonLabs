"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts an integer input. Import the built-in module math and use its factorial() method to
calculate the factorial of the integer input. Output the value of the factorial, as well as a Boolean value 
identifying whether the factorial output is greater than 100

The solution output should be in the format:
factorial_value
Boolean_value

If the input is
10

Then the expected output is
3628800
True

Alternatively, if the input is
3

Then the expected output is
6
False

"""

import math

user_input = int(input())
boolean_value = False

#Calculate factorial
factorial_value = math.factorial(user_input)

#If factorial is greater than 100 True if less than False
if factorial_value > 100:
    boolean_value = True

else:
    boolean_value = False

print(factorial_value)
print(boolean_value)

