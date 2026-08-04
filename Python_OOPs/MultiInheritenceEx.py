# Parent Class 1: Handles personal details
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Parent Class 2: Handles job details
class CompanyRole:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_role(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)

# Child Class: Inherits directly from BOTH Parent 1 and Parent 2
class Employee(Person, CompanyRole):
    def __init__(self, name, age, emp_id, salary, department):
        # Initialize both parent classes individually
        Person.__init__(self, name, age)
        CompanyRole.__init__(self, emp_id, salary)
        self.department = department

    def display(self):
        self.display_person()  # Call method from Person
        self.display_role()    # Call method from CompanyRole
        print("Department:", self.department)

# Testing the multiple inheritance structure
e1 = Employee("xyz", 25, 101, 50000, "HR")
e1.display()
