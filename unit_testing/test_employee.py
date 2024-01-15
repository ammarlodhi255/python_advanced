import unittest 
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod 
    def tearDownClass(cls):
        print('All tests completed')

    def setUp(self):
        self.emp1 = Employee('John', 'Connor', 12000)
        self.emp2 = Employee('Sarah', 'Connor', 15000)

    def tearDown(self):
        print('Test completed')

    def test_email(self):
        self.assertEqual(self.emp1.email, '{}.{}@company.com'.format(self.emp1.fname, self.emp1.lname))
        self.assertEqual(self.emp2.email, '{}.{}@company.com'.format(self.emp2.fname, self.emp2.lname))

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, '{} {}'.format(self.emp1.fname, self.emp1.lname))
        self.assertEqual(self.emp2.fullname, '{} {}'.format(self.emp2.fname, self.emp2.lname))

    def test_pay(self):
        temp_emp = Employee('TempFName', 'TempLName', 9500)
        with self.assertRaises(ValueError):
            temp_emp.apply_raise()

if __name__ == '__main__':
    unittest.main()


