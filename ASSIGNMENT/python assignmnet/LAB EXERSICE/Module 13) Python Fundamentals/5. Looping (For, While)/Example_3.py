List1 = ['apple', 'banana', 'mango']
search_item = 'banana'

for fruit in List1:
    if fruit == search_item:
        print(f"{search_item} found in the list!")
        break
else:
    print(f"{search_item} not found in the list.")
    