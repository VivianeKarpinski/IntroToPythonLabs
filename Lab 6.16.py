"""
6.16 LAB: Brute force equation solver

Numerous engineering and scientific applications require finding solution to a set of equations
EX: 8x + 7y = 38 and 3x - 5y = -1 have a solution x =3 and y = 2

Given integer coefficients of two linear equations with variables x and y, use brute force to find
an integer solution for x and y in range -10 to 10

EX: If the input is
8
7
38
3
-5
-1

Then the output is
x = 3 , y = 2

Use this brute force approach:
For every value of x from -10 to 10
    For every value of y from - 10 to 10
        Check if the current x and y satisfy both equations. If so, output the solution and finish

EX: If there is no solution, output
There is no solution

Assume the two equations have no more than one solution.

"""

"""Read in first equation, ax + by = c"""
a = int(input())
b = int(input())
c = int(input())

"""Read in second equation, dx + ey = f"""
d = int(input())
e = int(input())
f = int(input())

check = False

for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
        if a * x + b * y == c and d * x + e * y == f:
            check = True
            print('x =',x, ',', 'y =', y)

if check == False:
    print('There is no solution')

