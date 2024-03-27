"""
5.16 LAB: Leap year

Write a program that determines if a year is a leap year or not

A YEAR IS LEAP IF:

1) The year is divisible by 4

2) If the year is a century year (1700, 1800, etc), the year must be evenly divisible by 400
"""

is_leap_year = False
   
input_year = int(input())

if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
    is_leap_year = True
else:
    is_leap_year = False

if is_leap_year is True:
    print(f'{input_year} - leap year')
else:
    print(f'{input_year} - not a leap year')
