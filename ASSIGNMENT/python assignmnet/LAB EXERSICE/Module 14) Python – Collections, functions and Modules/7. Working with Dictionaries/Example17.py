# Two lists
keys = ["id", "name", "age"]
values = [101, "Rahul", 22]

# Empty dictionary
dictionary = {}

# Convert lists to dictionary using loop
for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

print("Converted dictionary:", dictionary)
