# Important dictionary functions:

employee_dict = {'name': 'John', 'age': 25, 'department': "Computer Science"}

print(employee_dict.get('phone', 'Not Found'))
print(f'Dict Length: {len(employee_dict)}')

employee_dict['phone'] = '555-555-99'
print(employee_dict)

employee_dict.update({'name': "Jane", 'age': 26})
print(employee_dict)

del employee_dict['age']
# age = employee_dict.pop('age')
print(employee_dict)

print(employee_dict.keys())
print(employee_dict.values())
print(employee_dict.items())


for key, value in employee_dict.items():
    print(f'{key}: {value}')


employee2 = employee_dict
if employee2 is employee_dict:
    print(id(employee2), id(employee_dict)) # Print memory locations

employee2['name'] = 'Ammar'
print(employee_dict['name']) # Dictionaries are mutable objects