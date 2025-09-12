# Hierarchical Inheritance

class Parent:
    def property(self):
        print("Parent property shared")

class Child1(Parent):
    def child1_feature(self):
        print("Child1 feature")

class Child2(Parent):
    def child2_feature(self):
        print("Child2 feature")

obj1 = Child1()
obj2 = Child2()

obj1.property()
obj1.child1_feature()

obj2.property()
obj2.child2_feature()
