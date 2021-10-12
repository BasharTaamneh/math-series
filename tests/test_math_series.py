# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'


def test_it_return_nth_value_in_fibonacci_series():
    # Arrange
    num_fibonacci = 1
    expected_fibonacci = 1
    # Act
    actual_fibonacci = fibonacci(num_fibonacci)
    # Assert
    assert actual_fibonacci == expected_fibonacci


def test_it_return_nth_value_in_fibonacci_series_2():
    # Arrange
    num_fibonacci = 3
    expected_fibonacci = 3
    # Act
    actual_fibonacci = fibonacci(num_fibonacci)
    # Assert
    assert actual_fibonacci == expected_fibonacci


def test_it_return_nth_value_in_fibonacci_series_3():
    # Arrange
    num_fibonacci = 4
    expected_fibonacci = 5
    # Act
    actual_fibonacci = fibonacci(num_fibonacci)
    # Assert
    assert actual_fibonacci == expected_fibonacci


def test_it_return_nth_value_in_fibonacci_series_4():
    # Arrange
    num_fibonacci = 6
    expected_fibonacci = 13
    # Act
    actual_fibonacci = fibonacci(num_fibonacci)
    # Assert
    assert actual_fibonacci == expected_fibonacci


def test_it_return_nth_value_in_fibonacci_series_5():
    # Arrange
    num_fibonacci = 7
    expected_fibonacci = 21
    # Act
    actual_fibonacci = fibonacci(num_fibonacci)
    # Assert
    assert actual_fibonacci == expected_fibonacci


def test_it_return_nth_value_in_fibonacci_series_6():
    # Arrange
    num_fibonacci = 0
    expected_fibonacci = 0
    # Act
    actual_fibonacci = fibonacci(num_fibonacci)
    # Assert
    assert actual_fibonacci == expected_fibonacci


def test_it_return_nth_value_in_lucas_numbers():
    # Arrange
    num_lucas = 1
    expected_lucas = 3
    # Act
    actual_lucas = lucas(num_lucas)
    # Assert
    assert actual_lucas == expected_lucas


def test_it_return_nth_value_in_lucas_numbers_1():
    # Arrange
    num_lucas = 0
    expected_lucas = 2
    # Act
    actual_lucas = lucas(num_lucas)
    # Assert
    assert actual_lucas == expected_lucas


def test_it_return_nth_value_in_lucas_numbers_1():
    # Arrange
    num_lucas = 0
    expected_lucas = 2
    # Act
    actual_lucas = lucas(num_lucas)
    # Assert
    assert actual_lucas == expected_lucas
