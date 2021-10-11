
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring


def fibonacci(n: int):
    fibonacci_sequence = [0, 1]
    for i in range(n):
        nth_value = fibonacci_sequence[i] + fibonacci_sequence[i+1]
        fibonacci_sequence.append(nth_value)
    nth = fibonacci_sequence[len(fibonacci_sequence)-1]
    return nth
