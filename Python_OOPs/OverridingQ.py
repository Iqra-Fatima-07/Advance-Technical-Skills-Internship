class Bird:
    def fly(self):
        print("Birds can fly")
class penguin(Bird):
    def fly(self):
        print("Penguin can't fly")

def flying_test(bird):
    Bird(fly)
    sparrow = bird()
    penguin = penguin()

    flying_test(sparrow)
    flying_test(penguin)