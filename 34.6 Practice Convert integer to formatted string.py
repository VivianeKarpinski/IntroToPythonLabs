"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts an integer input representing a 9-digit unformatted student identification number.
Output the identification number as string with no spaces.

The solution output should be in the format:
111-22-3333

If the input is
154175430

Then the output is
154-17-5430

"""
#Get 9-digit input from user
user_9_digit = int(input())

#Reformatting the input
formatted_input = str(int(user_9_digit / 1000000)) + "-" + str(int((user_9_digit / 10000) % 100)) + "-" + str(int(user_9_digit % 10000))

print(formatted_input)