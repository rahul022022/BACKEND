# Program: Create a class and access properties using an object

class Student:
    def __init__(self, name, age):
        self.name = name    
        self.age = age      


s1 = Student("Rahul", 21)


print("Student Name:", s1.name)
print("Student Age:", s1.age)
