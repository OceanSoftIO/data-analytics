class CalculatorError(Exception):
    """Custom exception for errors in the Calculator."""
    pass


class InvalidOperationError(CalculatorError):
    """Raised when an invalid operation is attempted."""
    pass


class InputValidationError(CalculatorError):
    """Raised when input validation fails."""
    pass
