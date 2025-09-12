# Create file and write something
with open("myfile.txt", "w") as f:
    f.write("This is my first file content.\n")
    f.write("Hello, World!\n")

# Now read the file
with open("myfile.txt", "r") as f:
    data = f.read()
    print("File contents:")
    print(data)
