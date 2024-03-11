"""4.12 LAB: Input and formatted output: Caffeine Levels

A half-life is the amount of time it takes for a substance or entity to fall to half its original value
Caffeine has a half-life of about 6 hours in humans. 

Given caffeine amount (in mg) as input, output the caffeine level after 6, 12, and 24 hours.
Use a string formatting expression with conversion specifiers to output the caffeine amount as 
floating-point numbers.

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

"""

caffeine_mg = float(input('input caffeine\n'))

six_hours = caffeine_mg / 2
twelve_hours = six_hours / 2
tf_hours = twelve_hours / 4

print(f'After 6 hours: {six_hours:.2f} mg\nAfter 12 hours: {twelve_hours:.2f} mg\nAfter 24 hours: {tf_hours:.2f} mg')