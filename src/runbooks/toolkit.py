"""
Toolkit Module: Implements basic arithmetic operations.

This module provides functions to perform addition, subtraction,
multiplication, and division with detailed input validation.

Features:
- Handles edge cases like NaN, Infinity, and division by zero.
- Supports logging for better traceability.
- Enforces type checks for input safety.

Author: Python Developer
"""

from typing import Union
from loguru import logger

# Define a type alias for supported numeric types
Number = Union[int, float]

# Configure loguru logger to simplify logs for testing
logger.remove()
logger.add(lambda msg: print(msg, end=""), format="{message}", level="DEBUG")


def _validate_inputs(a: Number, b: Number, allow_zero: bool = True) -> None:
    """
    Validates numeric inputs and checks edge cases.

    Args:
        a (Number): The first input value.
        b (Number): The second input value.
        allow_zero (bool): Whether zero is allowed as a value for `b`. Default is True.

    Raises:
        TypeError: If inputs are not integers or floats.
        ValueError: If inputs are NaN or Infinity.
        ZeroDivisionError: If `b` is zero and `allow_zero` is False.
    """
    # Type check
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Inputs must be numbers. Received: {type(a)} and {type(b)}")

    # Edge cases: NaN or Infinity
    for value in [a, b]:
        if value != value or value in [float('inf'), float('-inf')]:
            raise ValueError(f"Invalid input {value}. Must be a finite number.")

    # Zero Division Check
    if not allow_zero and b == 0:
        raise ZeroDivisionError("division by zero")


def add(a: Number, b: Number) -> float:
    """
    Adds two numbers and returns the result.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a (Number): The first number.
        b (Number): The second number.

    Returns:
        float: The sum of `a` and `b`.

    Raises:
        TypeError: If inputs are not numbers.
    """
    _validate_inputs(a, b)
    logger.debug(f"Adding {a} + {b}")
    return float(a + b)


def subtract(a: Number, b: Number) -> float:
    """
    Subtracts the second number from the first.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a (Number): The first number.
        b (Number): The second number.

    Returns:
        float: The result of `a - b`.

    Raises:
        TypeError: If inputs are not numbers.
    """
    _validate_inputs(a, b)
    logger.debug(f"Subtracting {a} - {b}")
    return float(a - b)


def multiply(a: Number, b: Number) -> float:
    """
    Multiplies two numbers and returns the result.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a (Number): The first number.
        b (Number): The second number.

    Returns:
        float: The result of `a * b`.

    Raises:
        TypeError: If inputs are not numbers.
    """
    _validate_inputs(a, b)
    logger.debug(f"Multiplying {a} * {b}")
    return float(a * b)


def divide(a: Number, b: Number) -> float:
    """
    Divides the first number by the second.

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0

    Args:
        a (Number): The numerator.
        b (Number): The denominator.

    Returns:
        float: The result of `a / b`.

    Raises:
        TypeError: If inputs are not numbers.
        ZeroDivisionError: If `b` is zero.
    """
    _validate_inputs(a, b, allow_zero=False)
    logger.debug(f"Dividing {a} / {b}")
    return float(a / b)
