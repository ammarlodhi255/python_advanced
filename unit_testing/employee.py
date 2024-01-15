class Employee():

    raise_amt = 1.05 

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.fname, self.lname)
    
    @property 
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    def apply_raise(self):
        if self.pay < 10000:
            raise ValueError('There is no employee in this company with such a pay')
        
        self.pay = int(self.pay * self.raise_amt)
