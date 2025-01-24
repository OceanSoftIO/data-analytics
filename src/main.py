"""
Main Application: CLI for Calculator and Toolkit Operations.

This script provides a CLI interface for performing arithmetic operations
using both Calculator (object-oriented) and Toolkit (functional) approaches.

Features:
- Supports addition, subtraction, multiplication, and division.
- Handles edge cases like invalid inputs, division by zero, and unsupported operations.
- Provides error logging and debugging through configurations.

Author: Python Developer
"""

import logging

from runbooks.calculator import Calculator
from runbooks.config import DEFAULT_CONFIG
from runbooks.exceptions import InputValidationError, InvalidOperationError
from runbooks.toolkit import add, divide, multiply, subtract
from runbooks.file_manager import validate_input

# Configure logging
logging.basicConfig(
    filename=DEFAULT_CONFIG["log_file"],
    level=logging.DEBUG if DEFAULT_CONFIG["debug"] else logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def calculator_cli():
    """CLI interface for Calculator (object-oriented)."""
    try:
        calc = Calculator(precision=DEFAULT_CONFIG['precision'])
        operations = {
            '+': calc.add,
            '-': calc.subtract,
            '*': calc.multiply,
            '/': calc.divide,
        }

        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation not in operations:
            raise InvalidOperationError(f"Invalid operation '{operation}'. Choose from +, -, *, /.")

        x = validate_input(input("Enter first number: "))
        y = validate_input(input("Enter second number: "))

        result = operations[operation](x, y)
        print(f"Result: {result}")

    except (InvalidOperationError, InputValidationError) as e:
        logging.error(e)
        print(f"Error: {e}")
    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        print(f"Critical Error: {e}")


def toolkit_cli():
    """CLI interface for Toolkit (functional approach)."""
    try:
        operations = {
            '+': add,
            '-': subtract,
            '*': multiply,
            '/': divide,
        }

        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation not in operations:
            raise InvalidOperationError(f"Invalid operation '{operation}'. Choose from +, -, *, /.")

        x = validate_input(input("Enter first number: "))
        y = validate_input(input("Enter second number: "))

        # Perform the operation
        result = operations[operation](x, y)
        print(f"Result: {result}")

    except (InvalidOperationError, InputValidationError, ZeroDivisionError) as e:
        logging.error(e)
        print(f"Error: {e}")
    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        print(f"Critical Error: {e}")


def main():
    """Main CLI interface to select between Calculator and Toolkit."""
    print("Welcome to Runbooks CLI!")
    print("Select mode: ")
    print("1. Calculator (Object-Oriented)")
    print("2. Toolkit (Functional Approach)")

    try:
        choice = input("Choose 1 or 2: ").strip()
        if choice == "1":
            calculator_cli()
        elif choice == "2":
            toolkit_cli()
        else:
            raise ValueError("Invalid choice. Please select 1 or 2.")

    except Exception as e:
        logging.critical(f"Unexpected error in CLI: {e}")
        print(f"Critical Error: {e}")


if __name__ == "__main__":
    main()
