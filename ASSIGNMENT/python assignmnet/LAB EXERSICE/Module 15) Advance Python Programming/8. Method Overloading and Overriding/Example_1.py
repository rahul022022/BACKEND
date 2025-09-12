# Method Overloading using default arguments

class Calculator:
    def add(self, a=0, b=0, c=0):
        return a + b + c

calc = Calculator()
print("add() with 2 args:", calc.add(10, 20))
print("add() with 3 args:", calc.add(10, 20, 30))
print("add() with 1 arg :", calc.add(50))
