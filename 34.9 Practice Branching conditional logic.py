"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts an integer input representing water temperature in degrees Fahrenheit. 
Output a description of the water state based on the following scale:

- If the temperature is below 33F, the water is "Frozen".
- If the water is between 33F and 80F (Including 33), the water is "Cold".
- If the water is between 80F (Including 80) and 115F, the water is "Warm"
- If the water is between 115F and 211 (Including 115F) the water is "Hot"
- If the water is greater than or equal to 212F, the water is "Boiling"

Additionally, output a safety comment only during the following circumstances
- If the water is exactly at 212F, the safety comment is "Caution: Hot!"
- If the water temperature is less than 33F, the safety comment is "Watch out for ice!"

If the input is
118

Then the expected output is 
Hot

Alternatively if the expected output is
Frozen
Watch out for ice!

"""

#solution accepts integer input representing a water temperature
user_temp_input = int(input())

#If temperature is below 33F the water is "Frozen"
if user_temp_input < 33:
    print("Frozen")
    print("Watch out for ice!")
#If the water is between 33° F and 80° F (including 33), the water is “Cold”.
elif user_temp_input >= 34 and user_temp_input < 80:
    print("Cold")

#If the water is between 80° F and 115° F (including 80), the water is "Warm".
elif user_temp_input >= 80 and user_temp_input < 115:
    print("Warm")

#If the water is between 115° F and 211° (including 115) F, the water is “Hot"
elif user_temp_input >= 115 and user_temp_input < 211:
    print("Hot")

#If the water is greater than or equal to 212° F, the water is “Boiling”.
elif user_temp_input == 212:
    print("Boiling")
    print("Caution: Hot!")
s
elif user_temp_input >= 213:
    print("Boiling")