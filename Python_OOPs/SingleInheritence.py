class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
p1 = person("abc", 30)
p1.display()

class employee(person):
    def __init__(self, name, age, emp_id, salary):
        super().__init__(name, age)
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        super().display()
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)

e1 = employee("xyz", 25, 101, 50000)
e1.display()

