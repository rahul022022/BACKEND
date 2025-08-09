
# I will o demonstrate the creation of variables and different data types.

number = 10  # so Number is variable , And 10 Is a integer datatype.
print(number)
print(type(number))  

pi = 3.14   # so pi is variable , And 3.14 datatype is float.
print(pi)
print(type(pi))

Name = "Rahul Zapadiya" # so in this name is a variable , and Rahul Zapadiya string data type.
print(Name)
print(type(Name)) 

condition  = True   # so in this condition is a variable, and True boolean data type.
print(condition)
print(type(condition))

# List (mutable, ordered)
fruits = ["Apple", "Banana", "Cherry"]
print("Fruits:", fruits, "| Type:", type(fruits))

# Tuple (immutable, ordered)
coordinates = (10.5, 20.3)
print("Coordinates:", coordinates, "| Type:", type(coordinates))

# Dictionary (key-value pairs)
student_info = {"name": "Rahul", "age": 25, "course": "Python"}
print("Student Info:", student_info, "| Type:", type(student_info))

# Set (unordered, unique items)
unique_numbers = {1, 2, 3, 4}
print("Unique Numbers:", unique_numbers, "| Type:", type(unique_numbers))


# Now how to take user input and how check variable type using type().

user_name = input("Enter Your Name -> ") 
user_age = int(input("Enter Your Age -> "))

# So you might be think why you take int in one and not in another one because its very simple age will include numbers thats why we use int in that types of case.

print(user_name)
print(user_age)
