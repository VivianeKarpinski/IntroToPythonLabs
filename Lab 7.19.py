"""
7.19 LAB: Driving costs - functions

Write a function driving_cost() with input parameters miles_per_gallon, dollars_per_gallon, and miles_driven,
that returns the dollar cost to drive those miles. All items are type float. The function called with arguments
(20.0, 3.1599, 50.0) returns 7.89975

Define that function in a program whose imputs are the car's miles per gallon, and the price for gallon (both float).
Output the gas cost for 10 miles, 50 miles, and 400 miles, by calling your driving_cost() function three times

Output each floating-point value with two digits after decimal point, which can be achieved as follows:
print(f'{vour_value:.2f}')

"""
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven=10.0):
    total_cost = (miles_driven / miles_per_gallon) * dollars_per_gallon
    return(total_cost)

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven = 10):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven = 50):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven = 400):.2f}')