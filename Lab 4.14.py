"""4.14 LAB: Simple Statistics

Given 4 floating-point numbers. Use a string formatting expression with onversion specifiers to output
their product and their average as integers(rounded), than as floating-point numbers

Output each rounded integer using the following:
print(f'{yout_value:.0f}')

Output each floating-point value with three digits after the decimal point, which can be achieved as follows:
print(f{your_valued:.3f}')

"""

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

# Calculate their product and average
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4

# Output the product and average as integers (rounded)
print(f'{product:.0f} {average:.0f}')

# Output the product and average as floating-point numbers
print(f'{product:.3f} {average:.3f}')
