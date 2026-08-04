# write a program to create a program class employee with attribute name and salary 
# create another class developer that inherit the property of class employee again create another class of HR that will
#  inherit the property of class employee and developer display all the details

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

    def display(self):
        Employee.display(self)
        print("Language:", self.programming_language)


class HR(Developer, Employee):
    def __init__(self, name, salary, programming_language, total_recruits):
        Employee.__init__(self, name, salary)
        Developer.__init__(self, name, salary, programming_language)
        self.total_recruits = total_recruits

    def display(self):
        Developer.display(self)
        print("Total Recruits:", self.total_recruits)


hr_dev = HR("ABC", 75000, "Python", 25)

print("--- Displaying All Details ---")
hr_dev.display()
