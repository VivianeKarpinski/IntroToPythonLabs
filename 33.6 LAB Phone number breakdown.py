"""
33.6 LAB: Phone number breakdown

Given an integer representing a 10-digit phone number, output the area code, prefix, and line number using the
format (800)555-1212

Ex input
8005551212

Ex output
(800)555-1212

Hint: use % to get desired rightmost digits
Hint: use // to dhift right by desired amount

Assume no phone number starts with a 0

"""

phone_number = int(input())

num_1 = phone_number // 10000000
num_2 = phone_number // 10000 % 1000
num_3 = phone_number % 10000

print(f'({num_1}) {num_2}-{num_3}')