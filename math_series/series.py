
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

def fibonacci(n: int) -> int:
    '''
    The Fibonacci Series is a numeric series starting with the integers 0 and 1.
        In this series, the next integer is determined by summing the previous two integers.
        This gives us: (n)=6, (nth_value)=[0, 1, 1, 2, 3, 5, 8, 13, ...]
    the fibonacci function have one parameter (n).
        so will return the nth value in the fibonacci series after checking that the parameter (n),
        greater than or equal to zero.
    '''
    if n <= 0:
        return 0
    fibonacci_sequence = [0, 1]
    for i in range(n):
        nth_value = fibonacci_sequence[i] + fibonacci_sequence[i+1]
        fibonacci_sequence.append(nth_value)
    nth = fibonacci_sequence[len(fibonacci_sequence)-1]
    return nth


def lucas(n: int) -> int:
    '''
    The Lucas Numbers are a related series of integers,
        that start with the values 2 and 1 rather than 0 and 1.
        In this series, the next integer is determined by summing the previous two integers.
        This gives us: (n)=6, (nth_value)=[2, 1, 3, 4, 7, 11, 18, 29, ...]
    the Lucas function have one parameter (n).
        so will return the nth value in the Lucas series after checking that the parameter (n),
        greater than or equal to zero.
    '''
    if n <= 0:
        return 2
    lucas_numbers = [2, 1]
    for i in range(n):
        nth_value = lucas_numbers[i] + lucas_numbers[i+1]
        lucas_numbers.append(nth_value)
    nth = lucas_numbers[len(lucas_numbers)-1]
    return nth


def sum_series(n: int, x=0, y=1):
    series = [x, y]
    if n <= 0 and x == 0 and y == 1:
        return 0
    for i in range(n):
        nth_value = series[i] + series[i+1]
        series.append(nth_value)
    nth = series[len(series)-1]
    return nth
