"""3.12 LAB: Divide input integers

Write a program that reads integers user_num and div_num as input

and outputs user_num divided by div_num three times using floor divisions

"""

user_num = int(input())
div_num = int(input())

print(user_num // div_num, user_num // div_num // div_num, user_num // div_num // div_num // div_num)