class Employee():
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last 
        self.pay = pay 
    

    def __str__(self):
        return f'Name: {self.first} {self.last}, Email: {self.email}, Salary: {self.pay}'

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    '''
        A property decorator, allows us to define a method but we can access it like an attribute.
        Note that with the property decorator, you can only access an attribute, not change it. 
        For changing the value of an attribute by accessing it and assigning it a new value, we 
        can implement setters.
    '''

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first, self.last = first, last 
    

    '''
        A deleter is what gets executed when we use the 'del' operator.
    '''

    @fullname.deleter
    def fullname(self):
        self.first, self.last = None, None 


if __name__ == '__main__':

    emp = Employee('John', 'Connor', 12000)
    print(emp)
    print(emp.fullname)

    emp.fullname = 'Sarah Hives'

    print(emp)
    print(emp.fullname)

    del emp.fullname
    print(emp)
    print(emp.fullname)