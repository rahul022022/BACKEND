# Hybrid Inheritance

class A:
    def show_A(self):
        print("Class A")

class B(A):
    def show_B(self):
        print("Class B")

class C(A):
    def show_C(self):
        print("Class C")

class D(B, C):   # Multiple inheritance
    def show_D(self):
        print("Class D")

obj = D()
obj.show_A()
obj.show_B()
obj.show_C()
obj.show_D()
