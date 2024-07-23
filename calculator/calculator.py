def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b
def divide(a, b):
    """Returns the quotient of dividing the first number by the second (non-zero) number."""
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero!"
if __name__ == "__main__":
    # Sample inputs
    num1 = 10
    num2 = 5
    print(f"Sum: {add(num1, num2)}")
    print(f"Difference: {subtract(num1, num2)}")
    print(f"Product: {multiply(num1, num2)}")
    print(f"Quotient: {divide(num1, num2)}")
