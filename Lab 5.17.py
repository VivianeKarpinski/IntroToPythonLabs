"""
5.17 LAB: Golf Scores

Golf scores record the number of strokes used to get the ball in the hole. The expected number of strokes varies
from hole to hole an is called par (i.e 3, 4, or 5). Each score's name is based on the actual strokes taken compared
to par

Eagle: Number of strokes two less than par
Birdie: Number of strokes is one less than par
Par: Number of strokes equals to par
Bogey: Number of strokes is one more than par

Given two integers that represent par and the number of strokes used, write a program that prints the appropriate
score name. Print Error if par is not 3, 4, or 5
"""

par = (int(input('enter par\n')))
strokes = int(input('enter number of strokes\n'))

#if par is not 3, 4, or 5 print Error
if not (3 <= par <= 5):
    print('Error')

#Check of player got an Eagle.
#Eagle = number of strokes is two less than par
elif strokes == (par - 2):
    print('Eagle')

#Check if player got a Birdie
#Birdie = number of strokes is one less than par
elif strokes == (par - 1):
    print('Birdie')

#Check if player got a Par
#Par = number of strokes is equal to par
elif strokes == par:
    print('Par')

#Check if player got a Bogey
#Bogey = number of strokes is one more than par
elif strokes == (par + 1):
    print('Bogey')

