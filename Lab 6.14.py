"""
LAB 6.14: Convert to Reverse Binary

Write a program that takes in a positive integer as input, and outputs a string of 1's and 0's representing the
integer in reverse binary. For integer x, the algorithm is:

As long as x is greater than 0
    Output x modulo 2 (remainder is either 0 or 1)
    Assign x with x divided by 2

Note: The algorithm above outputs 0's and 1's in reverse order.

Ex: if input is 6 the output is 011 (Without reversing 6 is 110 in binary)
"""

number = int(input('Enter your number\n'))
num_list = []
while number != 0:
    num_list.append((number % 2))
    number = number // 2

print(*num_list, sep ='')