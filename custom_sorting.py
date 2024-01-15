class Student():
    def __init__(self, name, cgpa, department):
                self.name = name
                self.cgpa = cgpa 
                self.department = department

    def __repr__(self):
            return 'Name: {}, CGPA: {}, Department: {}'.format(self.name, self.cgpa, self.department)

std1 = Student('John', 3.7, 'Computer Science')
std2 = Student('Connor', 3.45, 'Accounting')
std3 = Student('Sara', 3.5, 'Computer Engineering')
std4 = Student('Reese', 3.72, 'Robotics')

students = [std1, std2, std3, std4]

# I want to sort students based on their cgpa.

def std_sort(std):
        return std.cgpa 

sorted_students = sorted(students, key=std_sort, reverse=True)

print(f'Students: {students}')
print(f'Sorted Students: {sorted_students}')

# You also do the above with the following:
from operator import attrgetter

sorted2 = sorted(students, key=attrgetter('cgpa'), reverse=True)
print(f'Attrgetter Sorted: {sorted2}')