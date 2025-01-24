from typing import Union
from runbooks.exceptions import CalculatorError
from runbooks.config import DEFAULT_CONFIG


class Calculator:
    """Calculator class supporting arithmetic operations with configurable precision."""

    def __init__(self, precision: int = DEFAULT_CONFIG['precision']):
        """Initialize calculator with configurable precision."""
        self.precision = precision

    def _format_result(self, result: Union[int, float]) -> Union[int, float]:
        """Format result based on precision."""
        return round(result, self.precision)

    def add(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        """Adds two numbers."""
        return self._format_result(x + y)

    def subtract(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        """Subtracts second number from first."""
        return self._format_result(x - y)

    def multiply(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        """Multiplies two numbers."""
        return self._format_result(x * y)

    def divide(self, x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
        """Divides first number by second."""
        if y == 0:
            raise CalculatorError("Division by zero is not allowed.")
        return self._format_result(x / y)
