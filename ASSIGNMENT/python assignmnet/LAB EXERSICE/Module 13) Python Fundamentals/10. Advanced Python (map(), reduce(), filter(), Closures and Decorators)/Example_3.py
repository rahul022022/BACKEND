# Using filter() to get even numbers from list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(function, iterable)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original list:", numbers)
print("Even numbers:", even_numbers)
