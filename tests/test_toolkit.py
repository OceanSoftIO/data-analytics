"""
Test Suite for Toolkit Module

Tests the arithmetic operations provided by the toolkit module, covering:
- Addition, subtraction, multiplication, and division.
- Edge cases such as invalid inputs, division by zero, NaN, and Infinity.
- Performance with large numbers and type safety checks.

Author: Python Developer
"""

import pytest
from runbooks.toolkit import add, subtract, multiply, divide


#################################################################################
# HELPER FIXTURES                                                               #
#################################################################################

@pytest.fixture
def large_number():
    """Provides a very large number for performance testing."""
    return 1e100


#################################################################################
# TEST CASES: ADDITION                                                          #
#################################################################################

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5.0),                # Integers
        (2.5, 3.5, 6.0),            # Floats
        (-1, 1, 0.0),               # Negative and positive
        (0, 0, 0.0),                # Zero
        (1e10, 1e10, 2e10),         # Large numbers
    ],
)
def test_add(a, b, expected):
    """Test add function with valid inputs."""
    assert add(a, b) == expected


def test_add_invalid_inputs():
    """Test add with invalid inputs."""
    with pytest.raises(TypeError):
        add("a", 1)  # Invalid type


#################################################################################
# TEST CASES: SUBTRACTION                                                       #
#################################################################################

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2.0),                # Integers
        (2.5, 1.5, 1.0),            # Floats
        (-1, -1, 0.0),              # Negative numbers
        (0, 0, 0.0),                # Zero
        (1e10, 1e5, 9.9999e9),      # Large numbers
    ],
)
def test_subtract(a, b, expected):
    """Test subtract function with valid inputs."""
    assert subtract(a, b) == expected


def test_subtract_invalid_inputs():
    """Test subtract with invalid inputs."""
    with pytest.raises(TypeError):
        subtract(None, 1)  # Invalid type


#################################################################################
# TEST CASES: MULTIPLICATION                                                    #
#################################################################################

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6.0),                # Integers
        (2.5, 4, 10.0),             # Floats
        (-2, 3, -6.0),              # Negative numbers
        (0, 5, 0.0),                # Zero
        (1e5, 1e5, 1e10),           # Large numbers
    ],
)
def test_multiply(a, b, expected):
    """Test multiply function with valid inputs."""
    assert multiply(a, b) == expected


def test_multiply_invalid_inputs():
    """Test multiply with invalid inputs."""
    with pytest.raises(TypeError):
        multiply(2, "b")  # Invalid type


#################################################################################
# TEST CASES: DIVISION                                                          #
#################################################################################

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),                # Integers
        (2.5, 0.5, 5.0),            # Floats
        (-6, 3, -2.0),              # Negative numbers
        (1e10, 1e5, 1e5),           # Large numbers
    ],
)
def test_divide(a, b, expected):
    """Test divide function with valid inputs."""
    assert divide(a, b) == expected


def test_divide_by_zero():
    """Test divide function raises ZeroDivisionError on zero divisor."""
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(10, 0)


def test_divide_invalid_inputs():
    """Test divide with invalid inputs."""
    with pytest.raises(TypeError):
        divide("a", 2)  # Invalid type


#################################################################################
# EDGE CASES: SPECIAL FLOATS (NaN, INF)                                         #
#################################################################################

@pytest.mark.parametrize(
    "func, a, b",
    [
        (add, float('nan'), 1),
        (subtract, float('inf'), 1),
        (multiply, 1, float('-inf')),
        (divide, float('nan'), 1),
    ],
)
def test_special_floats(func, a, b):
    """Test functions with NaN and Infinity inputs."""
    with pytest.raises(ValueError, match="Invalid input .* Must be a finite number."):
        func(a, b)


#################################################################################
# PERFORMANCE TEST CASES                                                        #
#################################################################################

def test_large_operations(large_number):
    """Test arithmetic operations with extremely large numbers."""
    assert add(large_number, large_number) == 2 * large_number
    assert subtract(large_number, large_number) == 0.0
    assert multiply(large_number, 2) == 2 * large_number
    assert divide(large_number, 1) == large_number


#################################################################################
# TEST CASES: RETURN TYPES                                                      #
#################################################################################

@pytest.mark.parametrize(
    "func, a, b",
    [
        (add, 1, 2),
        (subtract, 5, 3),
        (multiply, 2, 3),
        (divide, 6, 2),
    ],
)
def test_return_type(func, a, b):
    """Test if the return type of all functions is float."""
    assert isinstance(func(a, b), float)


#################################################################################
# LOGGING VALIDATION                                                            #
#################################################################################

@pytest.mark.parametrize(
    "func, a, b, log_message",
    [
        (add, 1, 2, "Adding 1 + 2"),
        (subtract, 3, 1, "Subtracting 3 - 1"),
        (multiply, 2, 3, "Multiplying 2 * 3"),
        (divide, 4, 2, "Dividing 4 / 2"),
    ],
)
def test_logging(func, a, b, log_message, capsys):
    """Test log messages for debugging."""
    func(a, b)
    captured = capsys.readouterr()
    assert log_message in captured.out


#################################################################################
# EDGE CASES: EXTENDED FLOATS AND SMALL VALUES                                  #
#################################################################################

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (0, 0.1, 0.0),                   # Small divisor
        (-0.0, 1.0, 0.0),                # Negative zero
        (-1e10, 2, -5e9),                # Large negative numbers
        (1, 3, 1 / 3),                   # Fractions
    ],
)
def test_extended_cases(a, b, expected):
    """Test extended cases including small divisors and fractions."""
    assert divide(a, b) == pytest.approx(expected)
