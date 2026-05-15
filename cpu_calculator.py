"""
Simple CPU Calculator
A calculator that displays your CPU model and performs basic arithmetic operations.
"""

import platform
import re


def get_cpu_model():
    """
    Retrieves the CPU model name from the system.
    Works on Windows, macOS, and Linux.
    
    Returns:
        str: The CPU model name, or "Unknown CPU" if detection fails.
    """
    try:
        if platform.system() == "Windows":
            import subprocess
            result = subprocess.check_output(
                "wmic cpu get name",
                shell=True,
                text=True
            ).strip()
            # Extract the actual CPU name (skip the header)
            lines = result.split('\n')
            return lines[1].strip() if len(lines) > 1 else "Unknown CPU"
        
        elif platform.system() == "Darwin":  # macOS
            import subprocess
            result = subprocess.check_output(
                "sysctl -n machdep.cpu.brand_string",
                shell=True,
                text=True
            ).strip()
            return result
        
        else:  # Linux
            with open("/proc/cpuinfo", "r") as f:
                for line in f:
                    if "model name" in line:
                        return line.split(":", 1)[1].strip()
            return "Unknown CPU"
    
    except Exception as e:
        return f"Unable to detect CPU: {str(e)}"


def display_cpu_info():
    """Displays the detected CPU model and system information."""
    print("\n" + "="*60)
    print("                    CPU CALCULATOR")
    print("="*60)
    cpu_model = get_cpu_model()
    print(f"CPU Model: {cpu_model}")
    print(f"System: {platform.system()} {platform.release()}")
    print("="*60 + "\n")


def add(a, b):
    """Addition operation."""
    return a + b


def subtract(a, b):
    """Subtraction operation."""
    return a - b


def multiply(a, b):
    """Multiplication operation."""
    return a * b


def divide(a, b):
    """Division operation with zero-check."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def power(a, b):
    """Power operation (a ** b)."""
    return a ** b


def calculator():
    """Main calculator loop that performs operations."""
    display_cpu_info()
    
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': power,
        'pow': power
    }
    
    print("Available operations: + (add), - (subtract), * (multiply), / (divide), ** or pow (power)")
    print("Type 'quit' or 'exit' to end the calculator\n")
    
    while True:
        try:
            user_input = input("Enter calculation (e.g., 5 + 3): ").strip().lower()
            
            if user_input in ['quit', 'exit']:
                print("\nThank you for using CPU Calculator!")
                break
            
            if not user_input:
                continue
            
            # Parse the input
            for op_symbol, operation in operations.items():
                if op_symbol in user_input:
                    parts = user_input.split(op_symbol)
                    if len(parts) == 2:
                        num1 = float(parts[0].strip())
                        num2 = float(parts[1].strip())
                        result = operation(num1, num2)
                        print(f"Result: {num1} {op_symbol} {num2} = {result}\n")
                        break
            else:
                print("Invalid input. Please use the format: number operator number\n")
        
        except ValueError:
            print("Error: Please enter valid numbers\n")
        except Exception as e:
            print(f"Error: {str(e)}\n")


if __name__ == "__main__":
    calculator()
