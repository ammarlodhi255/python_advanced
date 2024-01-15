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


if __name__ == '__main__':
    emp1 = 'John,Connor,2500'
    emp2 = 'Sarah,Connor,5500'
    emp3 = 'Kyle,Reese,6000'

    emp1 = Employee.instantiate_from_string(emp1)
    emp2 = Employee.instantiate_from_string(emp2)
    emp3 = Employee.instantiate_from_string(emp3)

    print(emp1)
    print(emp2)
    print(emp3)