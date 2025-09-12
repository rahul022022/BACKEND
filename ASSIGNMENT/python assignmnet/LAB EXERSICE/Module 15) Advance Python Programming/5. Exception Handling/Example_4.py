# Program: Custom exception example

class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    print("You entered:", num)

except NegativeNumberError as e:
    print("Custom Exception:", e)
    