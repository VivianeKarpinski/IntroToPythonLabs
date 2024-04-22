"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". Each file 
contains two rows of comma-separated values. Import the built-in module csv file using open() function and
reader() method to create a dictionary:value pairs for each row of comma separated values in the specified file.
Output the file contents as two dictionaries.

The solution output should be in format
{'key' : 'value', 'key' : 'value, 'key' : 'value}
{'key' : 'value', 'key' : 'value, 'key' : 'value}

If the input is
input1.csv

Then the expected output is 
{'a' : '400', 'e' : '500', 'f' : '600'}
{'celery' : '2.81', 'milk' : '4.34', 'bread' : '5.63'}

"""

import csv
    
filename = input()
with open(filename, 'r') as f:
    line = csv.reader(f)
    for l in line:
            temp_list = [x.replace(' ', '') for x in l]
            dictionary = zip(temp_list[::2], temp_list[1::2])
            print(dict(dictionary))

