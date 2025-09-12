numbers = [5, 2, 9, 1, 7]

# Using sort() -> modifies the original list
numbers.sort()
print("List after sort():", numbers)

# Using sorted() -> returns a new sorted list without changing original
numbers2 = [5, 2, 9, 1, 7]
sorted_list = sorted(numbers2)
print("List after sorted():", sorted_list)
print("Original list remains unchanged:", numbers2)
