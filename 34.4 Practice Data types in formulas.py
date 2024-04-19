"""
INSTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output exactly the same format
shown in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts any three integers inputs representing the base (b1, b2) and height (h) measurements
of a trapezoid in meters. Output the exact area of the trapezoid in square meters as float value. The exact area
of a trapezoid can be calculated by finding the average of the two base measurements, then multiplying by the height
measurement.

Trapezoid Area Formula:
A = [(b1 + b2) / 2] * h

The solution should appear in the format:
Trapezoid area: area_value square meters

If input is
3
4
5

Then the expected output is
Trapezoid area: 17.5 square meters
"""

def trapezoid_area(b1, b2, h):
    calculated_area = ((b1 + b2) / 2) * h
    return calculated_area

__name__ == "__main__"
user_b1 = float(input())
user_b2 = float(input())
user_h = float(input())

area = trapezoid_area(user_b1, user_b2, user_h)

print(f"Trapezoid area: {area:.1f} square meters")