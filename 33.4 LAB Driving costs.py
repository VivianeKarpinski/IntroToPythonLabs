"""
33.4 LAB: Driving costs

Driving is expensive. Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon)
as floating point input, and output the gas cost for 20 miles, 75 miles and 500 miles

Output each floating-point value with two digits after decimal point, which can be achieved as follows:
print(f'{yourvalue:.2f}')

Ex input:
20.0
31.1599

Ex output:
316 11.85 79.00

"""

#Take in needed inputs
miles_per_gallon = float(input())
gas_cost = float(input())

#Find out price per mile
price_per_mile = gas_cost / miles_per_gallon

#Find cost for 20 miles, 75 miles, and 500 miles
twenty_miles = float(price_per_mile * 20)
seventy_five_miles = float(price_per_mile * 75)
five_hundred_miles = float(price_per_mile * 500)

#Print results
print(f'{twenty_miles:.2f} {seventy_five_miles:.2f} {five_hundred_miles:.2f}')