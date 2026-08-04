class Parent:
    def show(self):
        print("This is parent class")
class Child(Parent):
    def show(self):
        print("This is child class")
obj = Child()
obj.show()