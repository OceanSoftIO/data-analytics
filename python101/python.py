from typing import Union

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the subtraction of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a: A number representing the first addend in the subtraction.
        b: A number representing the second addend in the subtraction.

    Returns:
        A number representing the arithmetic subtraction of `a` and `b`.
    """
    return float(a - b)

def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """Compute and return the multiply of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a: A number representing the first addend in the multiply.
        b: A number representing the second addend in the multiply.

    Returns:
        A number representing the arithmetic multiply of `a` and `b`.
    """
    return float(a * b)

def divide(a: Union[float, int], b: Union[float, int]) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)