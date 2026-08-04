#Multiple Inheritence
class Father:
    def skills(self):
        print("Gardening, Driving")

class Mother:
    def skills(self):
        print("Cooking, painting")
class Child(Father, Mother):
    def Hobby(self):
        print("Child: Playing, Reading")
c1 = Child()
c1.Hobby()