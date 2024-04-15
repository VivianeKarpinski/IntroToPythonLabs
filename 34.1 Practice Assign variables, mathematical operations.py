"""
34.1 PRACTICE: Assign variables, mathematical operations.

INTRUCTIONS:
Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown
in the sample(s) below, including capitalization and whitespace.

TASK:
Create a solution that accepts three integer representing the number of times an employee travels to a job site. Output the
total distance traveled to two decimal places given the following miles per employee commute to the job site. Output the total
distance traveled to the job site. Output the total distance traveled to two decimal places given the following miles per employee
commute to the job site:

- Employee A: 15.62 miles
- Employee B: 41.85 miles
- Employee C: 32.67

The solution output should be in the format:
Distance: total_miles_traveled miles

Sample Input: 
1
2
3

Then the expected output is:
Distance: 197.33 miles

"""

#Employee A: 15.62 miles
#Employee B: 41.85 miles
#Employee C: 32.67 miles
#Solution accepts three integer inputs representing the number of tunes an employee travels to the job site
#Solution outputs "Distance: " followed by the total value to two decimal places.

#Creating variables for information given
employee_a = 15.62
employee_b = 41.85
employee_c = 32.67

#Taking in 3 inputs:
travel_1 = float(input())
travel_2 = float(input())
travel_3 = float(input())

#Performing Calculations
total_miles_traveled = ((travel_1 * employee_a) + (travel_2 * employee_b) + (travel_3 * employee_c))

#Correctly outputting results
print(f'Distance: {total_miles_traveled:.2f} miles')