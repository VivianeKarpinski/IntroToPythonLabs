"""
Write a program whose input is two integers. Output the first integer and subsequent increments of 5 
as long as the value is less than or equal to the second integer. End with a newline.

Ex: If the input is:
-15
10

The output is
-15 -10 -5 0 5 10

"""

num1 = int(input())
num2 = int(input())

if num1 < num2:  
    for i in range(num1, num2+1, 5):
        print(i, end = ' ')

    print()
else:
    print('Second integer can\'t be less than the first.')