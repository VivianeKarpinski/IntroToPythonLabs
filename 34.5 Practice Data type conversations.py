"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts five integer inputs. Output the sum of the five inputs three times, converting the
inputs to the requesed data type prior to finding the sum.

1) First output: sum of five inputs maintained as integer values
2) Second output: sum of five inputs converted to float values
3) Third output: sum of five inputs converted to string values (concatenate)

The solution should be in the format:

Integer: integer_sum_value
Float: float_sum_value
String: string_sum_value

If the input is
1
3
6
2
7

Then the expected output is
Integer: 19
Float: 19.0
String: 13627

"""

user_num1 = float(input())
user_num2 = float(input())
user_num3 = float(input())
user_num4 = float(input())
user_num5 = float(input())

#Sum as integer then print value
integer_sum_value = int(user_num1 + user_num2 + user_num3 + user_num4 + user_num5)
print(f"Integer: {integer_sum_value}")

#Sum as float then print value
float_sum_value = float(user_num1 + user_num2 + user_num3 + user_num4 + user_num5)
print(f"Float: {float_sum_value}")

#Print series of input as string by concanenating
str_user_num1 = str(int(user_num1))
str_user_num2 = str(int(user_num2))
str_user_num3 = str(int(user_num3))
str_user_num4 = str(int(user_num4))
str_user_num5 = str(int(user_num5))

print(f"String: {str_user_num1 + str_user_num2 + str_user_num3 + str_user_num4 + str_user_num5}")