# Initial list
my_list = [10, 20, 30]

# Using append() -> adds element at the end
my_list.append(40)
print("After append:", my_list)

# Using insert() -> adds element at a specific index
my_list.insert(1, 15)  # Insert 15 at index 1
print("After insert:", my_list)


# Removing elements
print("Original list:", my_list)

# Using pop() -> removes element at a given index (default last element)
my_list.pop()  
print("After pop:", my_list)

# Using remove() -> removes first occurrence of a value
my_list.remove(15)
print("After remove:", my_list)


fruits = ["apple", "banana"]

# append() -> add at the end
fruits.append("mango")

# insert() -> add at specific index
fruits.insert(1, "orange")

print("Updated fruits list:", fruits)


numbers = [1, 2, 3, 4, 5]

# pop() -> removes element at index 2 (element = 3)
numbers.pop(2)

# remove() -> removes first occurrence of 5
numbers.remove(5)

print("Updated numbers list:", numbers)
