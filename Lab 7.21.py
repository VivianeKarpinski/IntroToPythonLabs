"""
7.21 LAB: Convert to binary - functions

Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing
the integer in binary. For integer x the algororithm is:

As long as x is greater than 0
    output x % 2 (remainder is either 0 or 1)
    x = x // 2

Note: The above algorithm outputs the 0s and 1s in reverse order. You will need a second function to reverse the string

EX: If the input is:
6

The output is:
110

The program must define and call the following two functions:

int_to_reverse_binary(): takes an integer as a parameter and returns a string of 1's and 0's representing the 
                        integer in binary (in reverse)

string_reverse(): takes an input string as a parameter and returns a string representing the string in reverse.

def int_to_reverse_binary(integer_value)
def string_reverse(input_string)

"""

def int_to_reverse_binary(integer_value):
    output = '' #will store the string at the end of function
    while integer_value > 0:
        output += str(integer_value % 2)
        integer_value //= 2
    return output #saves result into output variable

def string_reverse(input_string):
    return input_string[::-1]

#MAIN PROGRAM GOES HERE:

if __name__ == '__main__':
    user_integer_value = int(input())
    user_input_string = int_to_reverse_binary(user_integer_value)
    print(string_reverse(user_input_string))