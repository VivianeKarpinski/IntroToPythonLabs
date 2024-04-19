"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accept an integer input representing the index value for any of the elements in the following
list:

various_data_types = [516, 112.49, True, "meow", ("Western, "Governors", "University"), {"apple" : 1, "pear" : 5}]

Using the built-in function type() and getting its name by using the name attribute, output data type based on the
input index value of the list element.

The solution output should be in the format:

Element index_value: data_type

If the input is:
4

then the expected output is
Element 4: tuple

"""

various_data_types = [516, 112.49, True, "meow", ("Western", "Governors", "University"), {"apple": 1, "pear": 5}]

#use built-in function type()
#get name by using the built-in attribute __name__
#solution accepts integer input representing list element index
#solution outputs data type of list element based on input index value

index_value = int(input())

name = various_data_types[index_value]

data_type = type(name).__name__

print("Element {}: {}".format(index_value, data_type))