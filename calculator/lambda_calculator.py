add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b if b != 0 else "Error: Cannot divide by zero!"

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    print(f"Sum: {add(num1, num2)}")
    print(f"Difference: {subtract(num1, num2)}")
    print(f"Product: {multiply(num1, num2)}")
    print(f"Quotient: {divide(num1, num2)}")
