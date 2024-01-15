class Employee():
    def __init__(self, first, last, email, pay):
        self.first = first 
        self.last = last 
        self.email = email 
        self.pay = pay 
    

    def __repr__(self):
        return f'Name: {self.first} {self.last}, Email: {self.email}, Salary: {self.pay}'
    

    @classmethod
    def instantiate_from_string(cls, emp_str):
        first, last, pay = emp_str.split(',')
        pay = int(pay)
        email = f'{first}.{last}@company.com'
        return cls(first, last, email, pay)
    
    '''
        A static method has some logical connection to a class. It does not accept 'cls' or 'self'. 
        When a task can be completed without accessing either 'cls' or 'self' then that task should be 
        encapsulated inside of a static method.
    '''

    @staticmethod
    def is_work_day(day):
        if day == 6 or day == 7: return True