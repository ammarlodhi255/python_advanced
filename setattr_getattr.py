class Person():
    pass


person_dict = {
    'first': 'Ammar',
    'last': 'Ahmed',
    'age': 24
}

person = Person()

for key, val in person_dict.items():
    setattr(person, key, val)

print(person.first, person.last, person.age)

for key, val in person_dict.items():
    print(getattr(person, key))