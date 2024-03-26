"""
5.15 LAB: Seasons

Write a program that takes date as an input and outputs the date's season in the northerns hemisphere.
The input is a string to reprent the month and an int to represent the day

Ex: If input is:
April
11

The output is:
Spring

In addition check if the string and int are valid (an actual month and day)

Ex: If input is:
Blue
65

The output is:
Invalid

"""

input_month = input('Insert Month')
input_day = int(input('Insert Date'))

months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

#If month is not in months list print invalid
if not (input_month in months):
    print('invalid')

#Seasons in January
elif input_month == 'January':
    if not (1 <= input_day <= 31):
        print('invalid')
    else:
        print('Winter')

#Seasons in February
elif input_month == 'February':
    if not (1 <= input_day <= 29):
        print('Invalid')
    else:
        print('Winter')

#Seasons in March
elif input_month == 'March':
    if not (1 <= input_day <= 31):
        print('Invalid')
    elif (1 <= input_day <= 19):
        print('Winter')
    elif (20 <= input_day <= 31):
        print('Spring')

#Seasons in April
elif input_month == 'April':
    if not (1 <= input_day <= 30):
        print('Invalid')
    else:
        print('Spring')

#Seasons in May
elif input_month == 'May':
    if not (1 <= input_day <= 31):
        print('Invalid')
    else:
        print('Spring')

#Seasons in June
elif input_month == 'June':
    if not (1 <= input_day <= 30):
        print('Invalid')
    elif (1 <= input_day <= 20):
        print('Spring')
    elif (21 <= input_day <= 30):
        print('Summer')

#Seasons in July
elif input_month == 'July':
    if not (1 <= input_day <= 31):
        print('Invalid')
    else:
        print('Summer')

#Seasons in August
elif input_month == 'August':
    if not (1 <= input_day <= 31):
        print('Invalid')
    else:
        print('Summer')

#Seasons in September
elif input_month == 'September':
    if not (1 <= input_day <= 30):
        print('Invalid')
    elif (1 <= input_day <= 21):
        print('Summer')
    elif (22 <= input_day <=30):
        print('Autumn')