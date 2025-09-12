# Multilevel Inheritance

class Grandparent:
    def show_gp(self):
        print("This is the Grandparent class")

class Parent(Grandparent):
    def show_parent(self):
        print("This is the Parent class")

class Child(Parent):
    def show_child(self):
        print("This is the Child class")

obj = Child()
obj.show_gp()
obj.show_parent()
obj.show_child()
