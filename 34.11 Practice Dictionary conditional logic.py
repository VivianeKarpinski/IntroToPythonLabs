"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts a string input representing a grocery store item and an integer input 
identifying the number of items purchased on a recent visit. The following dictionary purchase lists 
available items as the key with the cost per item as the value.

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

Additionally,

If fewer than ten items are purchased, the price is the full cost per item.
If between ten and twenty items (inclusive) are purchased, the purchase gets a 5% discount.
If twenty-one or more items are purchased, the purchase gets a 10% discount.
Output the chosen item and total cost of the purchase to two decimal places.

The solution output should be in the format
item_purchased $total_purchase_cost

If the input is

bananas
12
then the expected output is

bananas $21.09
Alternatively, if the input is

cookies
144
then the expected output is

cookies $585.79
"""

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

user_item = str(input())
amount_of_items = int(input())

#calculate total of purchase
total = amount_of_items * purchase.get(user_item)

#discounts according to conditions described in task.
#If fewer than ten items are purchased, the price is the full cost per item
#If between ten and twenty items (inclusive) are purchased gets a 5% discount
if amount_of_items >= 10 and amount_of_items <= 20:
    discount_5 = total - (0.05 * total)
    total = discount_5

#If twenty-one or more items are purchased, the purchase gets a 10% discount.
elif amount_of_items >= 21:
    discount_10 = total - (0.1 * total)
    total = discount_10

print(f'{user_item} ${total:.2f}')