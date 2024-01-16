class Student():

    # Init is a common dunder/magic/special method
    def __init__(self, fname, lname):
        self.fname = fname 
        self. lname = lname

    '''
        The __repr__ method is mainly meant for developers. As an example, you can return 
        a string inside of the __repr__ method that could be copied by the developers to 
        recreate the object.  Whereas __str__ is a displayable format of the object meant 
        to be used for end-users.
    '''

    def __repr__(self):
        return 'Student({}, {})'.format(self.fname, self.lname) 


    def __str__(self):
        return 'First Name: {}. Last Name: {}'.format(self.fname, self.lname)
    

class Calc():
    def __init__(self, num):
        self.num = num


    def __add__(self, other):
        return self.num + other.num 
    

    def __mul__(self, other):
        return self.num * other.num  
    

    def __sub__(self, other):
        return self.num - other.num  
    

    def __mod__(self, other):
        return self.num % other.num


if __name__ == '__main__':
    std1 = Student('John', 'Connor')
    print(std1)
    print(repr(std1))
    print(str(std1))

    a = Calc(4)
    b = Calc(10)

    print(a + b)
    print(a * b)
    print(a - b)
    print(a % b)