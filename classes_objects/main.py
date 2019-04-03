from person import Person
from datetime import datetime


class Employee(Person):
    empCount = 0

    def __init__(self, name, age, salary, address):
        Person.__init__(self, name, age, address)
        self.salary = salary
        self.date_employed = datetime.now().date()

    def __len__(self):
        return (datetime.now().date() - self.date_employed).days

    def __add__(self, other):
        return self.salary + other.salary

    def __repr__(self):
        return 'Employee({!r}, {!r}, {!r})'.format(
            self.name, self.age, self.salary)

    def display_count(self):
        print("Total Employee %d" % Employee.empCount)

    def display_person(self):
        print(
            "Name : ",
            self.name,
            ", Age : ",
            self.age,
            ", Salary: ",
            self.salary)

    def get_salary(self):
        return self.salary


emp1 = Employee('first employee', 21, 9999999, 'panacan')
emp2 = Employee('second employee', 24, 345234, 'matina')

print(repr(emp1))
print(repr(emp2))

emp1.display_person()
emp2.display_person()

print('days employed', len(emp1))
print('add salary', emp1 + emp2)

print('get_name', emp1.get_name())
print('get_age', emp2.get_age())
print('get_salary', emp1.get_salary())
print('get_address', emp2.get_address())
