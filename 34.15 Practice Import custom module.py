"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts an integer representing the age of a pig. Import the existing module PigAge and uses
pre-built pigAge_converter() function to calculate the human equivalent age of a pig. A year in a pig's life is
equivalent to five years in a human's life. Output the human-equivalent age of the pig.

The solution should be in the format

input_pig_age is converted_pig_age in human years

If the input is
8

Then the expected output is
8 is 40 in human years

"""

import pigAge

input_pig_age = int(input())

#Calculate age in human years
converted_pig_age = pigAge.pigAge_converter(input_pig_age)

#Print information in right format

print(f'{input_pig_age} is {converted_pig_age} in human years')