# Simple Calculator Project

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers. Handles division by zero."""
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def calculator():
    print("===== Simple Calculator =====")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")

        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice! Please select a valid option.")
            continue

        # Get user input for numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform the selected operation
        if choice == "1":
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")


# Run the calculator
if __name__ == "__main__":
    calculator()
