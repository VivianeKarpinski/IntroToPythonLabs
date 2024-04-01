"""
7.18 Lab training: Unit tests to evaluate your program

Complete a program that takes a weight in kilograms as input, converts the weight to pounds and then outputs
the weight in pounds. 1 kilogram = 2.204 pound(lbs)

The program must define the following function:
def kilo_to_pounds(kilos) - take kilos as a parameter convert kilos from kilograms to pounds, and return
the weight in pounds.

EX: If the input of the program is:
10

10 is passed to kilo_to_pounds() and the output of the program is
22.040 lbs

The program below has an error in kilo_to_pounds() function

1) Try submitting the program for grading. Notice that the first two test cases fail, but the third case passes.
the first test case fails because the program outputs the kilo_to_pounds() function, which has an error. 
The second test case uses a Unit test to test the kilo_to_piounds() function which fails.

2) Chage kilo_to_pounds() function to multiply the variable kilos by 2.204 instead of dividing. Now all test cases
should pass.

"""

def kilo_to_pounds(kilos):
    # This statement intentionally has an error. 
    return (kilos * 2.204)


# Main part of the program starts here. Do not remove the line below.
if __name__ == '__main__':
    kilos = float(input())
    
    pounds = kilo_to_pounds(kilos)
    print(f'{pounds:.3f} lbs')