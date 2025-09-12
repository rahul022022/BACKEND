# Using map() to square a list of numbers

numbers = [1, 2, 3, 4, 5]

# map(function, iterable)
squared_numbers = list(map(lambda x: x**2, numbers))

print("Original list:", numbers)
print("Squared list:", squared_numbers)
