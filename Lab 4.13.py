"""4.13 LAB: Input and Formatted Output: House real estate summary

Sites like Zillow get input about house prices from a database and provide nice summaries for readers.

Write a program with two inputs, current price and last month's price (both integers).

Then, output a summary listing the price, the change since last month, and the estimated monthly mortgage
computed as (current_price * 0.051) / 12

Output eah floating-point value with two digits after the decimal point, which can be achieved as follows:
print(f'{your_value:.2f}')

"""

current_price = int(input('input current price\n'))
last_months_price = int(input("input last month's price\n"))

change = current_price - last_months_price
estimated_morgage = (current_price * 0.051) / 12

print(f'This house is ${current_price}. The change is ${change:} since last month.\nThe estimated monthly mortgage is ${estimated_morgage:.2f}.')