# Parent Class 1 (Employment Hierarchy)
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


# Child Class (Single Inheritance from Employee)
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

    def display(self):
        Employee.display(self)
        print("Language:", self.programming_language)


# Parent Class 2 (A completely separate hierarchy for Office Infrastructure)
class Department:
    def __init__(self, dept_name, floor):
        self.dept_name = dept_name
        self.floor = floor

    def display_dept(self):
        print("Department:", self.dept_name)
        print("Office Floor:", self.floor)


# Hybrid Child Class (Combines Developer hierarchy AND Department hierarchy)
class HR(Developer, Department):
    def __init__(self, name, salary, programming_language, dept_name, floor, total_recruits):
        # Initialize the Employee/Developer side
        Developer.__init__(self, name, salary, programming_language)
        # Initialize the separate Department side
        Department.__init__(self, dept_name, floor)

        self.total_recruits = total_recruits

    def display(self):
        Developer.display(self)      # Displays Employee and Developer info
        Department.display_dept(self) # Displays Department info
        print("Total Recruits:", self.total_recruits)

hr_dev = HR("ABC", 75000, "Python", "Talent Acquisition", 4, 25)

print("--- Displaying All Hybrid Details ---")
hr_dev.display()
