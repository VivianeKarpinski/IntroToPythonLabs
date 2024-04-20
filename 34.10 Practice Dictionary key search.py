"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts an integer input identifying how many shares of stock are to be purchased from 
Old Town Stock Exchange, followed by an equivalent number of strings inputs representing the stock selections.
The following dictionary stock lists available stock selections as the key with the cost per selection as the value.

stocks = {TSLA': 912.86 , 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28, 'EMBK': 12.29, 'LVLU': 2.33}

Output the total cost of the purchased shares of stock with two decimal places.

The solution output should be in the format
Total price: $cost_of_stocks

If the input is
3
SOFI
AMZN
LVLU

Then the expected output is
Total price: $150.53
"""

stocks = {'TSLA': 912.86, 'BBBY': 24.84, 'AAPL': 174.26, 'SOFI': 6.92, 'KIRK': 8.72, 'AURA': 22.12, 'AMZN': 141.28,
          'EMBK': 12.29, 'LVLU': 2.33}

number_of_selection = int(input())
stock_selection = [input() for _ in range(number_of_selection)]

res = 0
for stock in stock_selection:
    res += stocks[stock]

print(f'Total price: ${res:.2f}')