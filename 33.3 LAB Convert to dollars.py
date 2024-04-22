"""
33.3 LAB: Convert to dollars

Given four values representing counts of quarters, dimes, nickels and pennies, output the total amount of dollars
and cents.

Output each floating point value with two digits after the decimal point, which can be achieved as follows:
print(f'Amount: ${dollars:.2f}')

If input is
4
3
2
1

Then expected output is
Amount: $1.41

"""

#Get amount of quarters, dimes, nickels, and pennies
quarters = float(input())
dimes = float(input())
nickels = float(input())
pennies = float(input())

#Calculate total of money
dollars = float(
    (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    )
    
#Output statement:
print(f'Amount: ${dollars:.2f}')