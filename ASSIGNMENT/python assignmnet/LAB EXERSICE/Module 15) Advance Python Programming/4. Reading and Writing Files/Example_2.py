# Program to write multiple strings into a file

with open("multilines.txt", "w") as f:
    f.write("Python is powerful.\n")
    f.write("File handling is easy.\n")
    f.write("We are writing multiple lines into a file.\n")

print("Data written successfully to multilines.txt")
