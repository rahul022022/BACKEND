# Generator function for first 10 even numbers
def generate_even_numbers():
    num = 2
    count = 0
    while count < 10:
        yield num
        num += 2
        count += 1

# Using the generator
for even in generate_even_numbers():
    print(even, end=" ")
