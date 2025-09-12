# Lab Task - Variables and Data Types in Python

# Example 1: Creating variables with different data types
age = 20
height = 5.6
name = "Rahul"
is_student = True
fruits = ["Apple", "Banana", "Mango"]
coordinates = (10, 20)
student = {"name": "Rahul", "age": 20, "course": "Python"}

print("---- Example 1: Different Data Types ----")
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))
print("Fruits:", fruits, "| Type:", type(fruits))
print("Coordinates:", coordinates, "| Type:", type(coordinates))
print("Student Dictionary:", student, "| Type:", type(student))
print()

# Example 2: Python code structure
print("---- Example 2: Code Structure ----")
def greet(name):
    if name:
        print("Hello,", name)
    else:
        print("Hello, Guest")

greet("Rahul")
greet("")
print()

# Example 3: Creating variables
print("---- Example 3: Creating Variables ----")
x = 10
y = 3.14
z = "Hello"
a, b, c = 1, 2, 3
print(x, y, z)
print("a:", a, "b:", b, "c:", c)
print()

# Example 4: Taking user input
print("---- Example 4: User Input ----")
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
print("Welcome", user_name, "You are", user_age, "years old.")
print()

# Example 5: Checking variable type
print("---- Example 5: Checking Types ----")
print("Type of user_name:", type(user_name))
print("Type of user_age:", type(user_age))
