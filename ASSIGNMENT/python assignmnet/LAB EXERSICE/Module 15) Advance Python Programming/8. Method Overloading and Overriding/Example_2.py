# Method Overriding

class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def show(self):   # overrides Parent's method
        print("This is Child class method")

obj1 = Parent()
obj1.show()   # calls Parent version

obj2 = Child()
obj2.show()   # calls Child version
