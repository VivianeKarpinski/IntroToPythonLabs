"""
Write a program to calculate the total price for car wash services. A base car wash is $10. A dictionary with each additional service and the corresponding cost has been provided. Two additional services can be selected. A '-' signifies an additional service was not selected. Output all selected services, according to the input order, along with the corresponding costs and then the total price for all car wash services.

Ex if the input is
Tire shine
Wax

The output is:
ZyCar Wash
Base car wash -- $10
Tire shine -- $2
Wax -- $3
----
Total price: $15



If the input is:
Rain repellent
-

The output is:
ZyCar Wash
Base car wash -- $10
Rain repellent -- $2
----
Total price: $12

"""
services = { 'Air freshener' : 1 , 'Rain repellent': 2, 'Tire shine' : 2, 'Wax' : 3, 'Vacuum' : 5 }
base_wash = 10
total = 0

service_choice1 = input()
service_choice2 = input()

#choice 1

if service_choice1 == 'Air freshener':
    service1cost = services.get(service_choice1)
    
elif service_choice1 == 'Rain repellent':
   service1cost = services.get(service_choice1)

elif service_choice1 == 'Tire shine':
    service1cost = services.get(service_choice1)

elif service_choice1 == 'Wax':
    service1cost = services.get(service_choice1)

elif service_choice1 == 'Vacuum':
    service1cost = services.get(service_choice1)

elif service_choice1 == "-":
    service1cost = 0

#choice 2
if service_choice2 == 'Air freshener':
    service2cost = services.get(service_choice2)

elif service_choice2 == 'Rain repellent':
    service2cost = services.get(service_choice2)

elif service_choice2 == 'Tire shine':
    service2cost = services.get(service_choice2)

elif service_choice2 == 'Wax':
    service2cost = services.get(service_choice2)

elif service_choice2 == 'Vacuum':
    service2cost = services.get(service_choice2)

elif service_choice2 == "-":
    service2cost = 0

total = base_wash + service1cost + service2cost

print(f'ZyCar Wash\nBase car wash -- ${base_wash}')
if service1cost > 0:
    print(f'{service_choice1} -- ${service1cost}')
if service2cost > 0:
    print(f'{service_choice2} -- ${service2cost}')
print('----')
print(f'Total price: ${total}')