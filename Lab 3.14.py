"""3.14 LAB: Using math functions

Given three floating-point numbers x, y, and z.

1) output x to the power of z
2) x to the power of (y to the power of z)
3) the absolute value of (x minus y)
4) the square root of (x to the power of z)

Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f} {your_value4:.2f}')

"""

import math

x = float(input())
y = float(input())
z = float(input())

calc_1 = math.pow(x, z)
calc_2 = math.pow(x, math.pow(y, z))
calc_3 = math.fabs(x - y)
calc_4 = math.sqrt(math.pow(x, z))

print(f'{calc_1:.2f} {calc_2:.2f} {calc_3:.2f} {calc_4:.2f}')