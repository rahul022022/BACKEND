# Program: Calculator with exception handling

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    choice = input("Enter operation (+, -, *, /): ")

    if choice == "+":
        print("Result:", a + b)
    elif choice == "-":
        print("Result:", a - b)
    elif choice == "*":
        print("Result:", a * b)
    elif choice == "/":
        print("Result:", a / b)
    else:
        print("Invalid operation!")

except ValueError:
    print("Error: Invalid input, please enter numbers only.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
