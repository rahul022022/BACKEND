"""
This program demonstrates correct use of:
1. Indentation
2. Comments
3. Variable naming
Following PEP 8 style guidelines
"""

# Function to calculate the sum of two numbers
def add_numbers(num1, num2):
    """Return the sum of two numbers."""
    return num1 + num2


# Function to calculate the square of a number
def square_number(number):
    """Return the square of a number."""
    return number ** 2


# Main program execution
if __name__ == "__main__":
    # Variables (snake_case naming as per PEP 8)
    first_number = 10
    second_number = 5

    # Calculate sum
    sum_result = add_numbers(first_number, second_number)

    # Calculate square of the sum
    square_result = square_number(sum_result)

    # Output the results
    print(f"The sum of {first_number} and {second_number} is: {sum_result}")
    print(f"The square of {sum_result} is: {square_result}")
