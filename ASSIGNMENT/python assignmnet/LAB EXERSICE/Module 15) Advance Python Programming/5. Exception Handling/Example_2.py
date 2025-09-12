# Program: Handling multiple exceptions

try:
    num = int(input("Enter a number: "))
    result = 10 / num
   
    with open("testfile.txt", "w") as f:
        f.write("Hello! This file was just created.\n")

    with open("testfile.txt", "r") as f:
        data = f.read()
    print("File contents:", data)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Error: Invalid input, please enter a number.")
            