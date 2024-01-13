employee_dict = {'name': 'John', 'age': 25, 'department': "Computer Science"}

print(employee_dict.get('phone', 'Not Found'))
employee_dict['phone'] = '555-555-99'

print(employee_dict)