# Get user input
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a second number: "))

def add(num1, num2):
    """Add two numbers and return the result."""
    return num1 + num2

# Call the function and display the result
result = add(number1, number2)
print(f"The sum of {number1} and {number2} is {result}")
