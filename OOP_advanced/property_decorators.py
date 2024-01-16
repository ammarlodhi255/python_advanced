class Employee():
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
    

    def __str__(self):
        return f'Name: {self.first} {self.last}, Email: {self.email}, Salary: {self.pay}'
    
    '''
        A property decorator, allows us to define a method but we can access it like an attribute.
        Note that with the property decorator, you can only access an attribute, not change it.
    '''

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    

if __name__ == '__main__':

    emp = Employee('John', 'Connor', 12000)
    print(emp)
    print(emp.email)
    print(emp.fullname)

    emp.first = 'Sarah'
    emp.last = 'Hives'

    print(emp)
    print(emp.email)
    print(emp.fullname)