# Two lists
keys = ["name", "age", "city"]
values = ["Rahul", 21, "Ahmedabad"]

# Empty dictionary
my_dict = {}

# Merge using loop
for i in range(len(keys)):
    my_dict[keys[i]] = values[i]

print("Merged dictionary:", my_dict)
