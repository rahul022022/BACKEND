# Use of super() in Inheritance

class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent constructor called")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)   # call Parent constructor
        self.age = age
        print("Child constructor called")

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

obj = Child("Rahul", 21)
obj.show()
