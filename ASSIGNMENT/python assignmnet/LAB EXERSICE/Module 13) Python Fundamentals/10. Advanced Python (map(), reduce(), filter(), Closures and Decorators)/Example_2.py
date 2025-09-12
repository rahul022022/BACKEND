# Using reduce() to find the product of a list of numbers

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# reduce(function, iterable)
product = reduce(lambda x, y: x * y, numbers)

print("Numbers:", numbers)
print("Product of numbers:", product)
