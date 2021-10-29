import csv
import yaml
from pprint import pprint

employees = []
addresses = []
departments = []


while True:
    answer = input('What would you like to add?\n1) Department\n2) Address\n3) Employee\n0) Exit\n:')
    
    if answer == '1':
        # for department table
        department = {
            "id" : int(input("Enter department id: ")),
            "name" : input("Enter department name: "),
            "headquarters_address_id" : int(input("Enter headquarters address id: "))
        }
        departments.append(department)
        continue
        

    elif answer == '2':
        # for address table
        address = {
            "address_id" : int(input("Enter address id: ")),
            "street" : input("Enter street as number name: "),
            "city" : input("Enter city: "),
            "state" : input("Enter state: ")
        }

        addresses.append(address)
        continue

    elif answer == '3':
        # for employees table
        employee = {
            "id" : int(input("Enter your employee id: ")),
            "name" : input("Enter the employee's name: "),
            "age" : int(input("Enter your age: ")),
            "salary" : float(input("Enter your salary: ")),
            "department_id" : int(input("Enter department id: ")),
            "address_id" : int(input("Enter address id: ")),
            "manager_id" : int(input("If the employee is a manager, enter manager's id. If not, type 0: ")),
        }
        employees.append(employee)
        continue
    
        
    elif answer == '0':
        break
    else:
        print('Could not process selection.')



## Test Data
# # for employees table
# employees = [{
#         "id" : 1,
#         "name" : 'Jane',
#         "age" : 9,
#         "salary" : 9,
#         "department_id" : 100,
#         "address_id" : 10,
#         "manager_id" : 9,
#     }]

# # for address table
# addresses = [{
#         "id" : 10,
#         "street" : '123 A',
#         "city" : "BB",
#         "state" : "A"
#     },
#     {
#         "id" : 11,
#         "street" : '123 B',
#         "city" : "AA",
#         "state" : "A"
#     },
#     {
#         "id" : 12,
#         "street" : '123 C',
#         "city" : "AA",
#         "state" : "B"
#     },
#     {
#         "id" : 13,
#         "street" : '123 D',
#         "city" : "AA",
#         "state" : "B"
#     }
# ]

# # for department table
# departments = [{
#         "id" : 100,
#         "name" : 'd1',
#         "headquarters_address_id" : 9
#     },
#     {
#         "id" : 101,
#         "name" : 'd2',
#         "headquarters_address_id" : 8
#     }
# ]


pprint(departments)
pprint(addresses)
pprint(employees)

            
            
#   - Each Python Script should output data as CSV

with open('employees.csv', "w") as file:
    writer = csv.DictWriter(file, fieldnames=employees[0].keys())
    writer.writeheader()

    for i in range(len(employees)):
        writer.writerow(employees[i])

print('employees.csv data saved.')


with open('addresses.csv', "w") as file:
    writer = csv.DictWriter(file, fieldnames=addresses[0].keys())
    writer.writeheader()

    for i in range(len(addresses)):
        writer.writerow(addresses[i])

print('addresses.csv data saved.')

with open('departments.csv', "w") as file:
    writer = csv.DictWriter(file, fieldnames=departments[0].keys())
    writer.writeheader()

    for i in range(len(departments)):
        writer.writerow(departments[i])

print('departments.csv data saved.')

# # Export Departments as a YAML file
with open("departments.yml", "wt") as file:
    yaml.dump(departments, file)

print('departments.yml data saved.')

# #Export Addresses as a YAML file, grouped by state, and then grouped by city

grouped_addresses = {}
for a in addresses:
    if a['state'] not in grouped_addresses:
        grouped_addresses[a['state']] = {}

    if a['city'] not in grouped_addresses[a['state']]:
        grouped_addresses[a['state']][a['city']] = {}

    grouped_addresses[a['state']][a['city']][a['id']] = a['street']

with open("addresses.yml", "wt") as file:
    yaml.dump(grouped_addresses, file)

print('addresses.yml data saved.')


