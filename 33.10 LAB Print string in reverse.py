"""
33.10 LAB Print string in reverse

Write a program that takes in a line of text as input, and outputs that line of text in reverse. 
The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

Ex: If the input is:

Hello there
Hey
done
then the output is:

ereht olleH
yeH

"""

user_input = str(input())
stop = ['Done', 'done', 'd']

while user_input not in stop:
    print(user_input[::-1])
    user_input = str(input())