
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring

def fibonacci(n: int) -> int:
    '''
    The Fibonacci Series is a numeric series starting with the integers 0 and 1.
    In this series, the next integer is determined by summing the previous two integers.
    The Fibonacci function has one parameter (n).
    so depends on this parameter the Fibonacci function will iterate the (n)loop,
    to create the series by summing the previous two integers and,
    appending the summation to the Fibonacci Series then
    return the (nth_value) from it.
    This gives us: (n)=6, (nth_value)=[0, 1, 1, 2, 3, 5, 8, 13, ...] the return nth=(8)
    '''
    fibonacci_sequence = [0, 1]
    for i in range(n):
        nth_value = fibonacci_sequence[i] + fibonacci_sequence[i+1]
        fibonacci_sequence.append(nth_value)
    nth = fibonacci_sequence[len(fibonacci_sequence) - 2]
    return  nth




def lucas(n: int) -> int:
    '''
    The Lucas Numbers are a related series of integers,
    that start with the values 2 and 1 rather than 0 and 1.
    In this series, the next integer is determined by summing the previous two integers.
    the Lucas function have one parameter (n).
    so depends on this parameter the Lucas function will iterate the (n)loop,
    to create the series by summing the previous two integers and,
    appending the summation to the Lucas Numbers then
    return the (nth_value) from it.
    so will return the nth value in the Lucas series.
    This gives us: (n)=6, (nth_value)=[2, 1, 3, 4, 7, 11, 18, 29, ...] the return nth=(18)
    '''
    lucas_numbers = [2, 1]
    for i in range(n):
        nth_value = lucas_numbers[i] + lucas_numbers[i+1]
        lucas_numbers.append(nth_value)
    nth = lucas_numbers[len(lucas_numbers) - 2]
    return nth


def sum_series(n: int, x=0, y=1):
    '''
    The sum_series is a function that generates a series
    starting with defulet two optional arguments integers 0 and 1.
    In this series, the next integer is determined by summing the previous two integers.
    The sum_series function has one parameter (n).
    so depends on this parameter the sum_series function will iterate the (n)loop,
    to create the series by summing the previous two integers and,
    appending the summation to the Series then
    return the (nth_value) from it same as the Fibonacci function
    but if you want to generate a different series you have to change the optional value,
    by-->passing the new value through the function call.
    sum_series(6)=> this gives us: (n)=6,
    (nth_value)=[0, 1, 1, 2, 3, 5, 8, 13, ...] the return nth=(8)
    sum_series(6, 2, 1)=> this gives us: (n)=6, (x)=2, (y)=1
    (nth_value)=[2, 1, 3, 4, 7, 11, 18, 29, ...] the return nth=(18)
    '''
    series = [x, y]
    for i in range(n):
        nth_value = series[i] + series[i+1]
        series.append(nth_value)
    nth = series[len(series)-2]
    return nth
