# Create a file and write a string into it

with open("example.txt", "w") as f:
    f.write("This is a practical example of file handling.")

print("String written into example.txt successfully.")

# Read file and print contents

with open("example.txt", "r") as f:
    data = f.read()
    print("Data inside example.txt:")
    print(data)


# Check file cursor position using tell()

with open("example.txt", "r") as f:
    print("Initial cursor position:", f.tell())  # should be 0
    data = f.read(10)  # read first 10 characters
    print("After reading 10 chars, cursor position:", f.tell())
