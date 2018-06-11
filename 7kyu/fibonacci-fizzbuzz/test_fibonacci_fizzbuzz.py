"""Fibonacci Fizz Buzz Test Cases."""
from fibonacci_fizzbuzz import fibs_fizz_buzz


def test_basic():
    """Basic test cases."""
    assert fibs_fizz_buzz(5) == [1, 1, 2, 'Fizz', 'Buzz']
    assert fibs_fizz_buzz(7) == [1, 1, 2, 'Fizz', 'Buzz', 8, 13]
    assert fibs_fizz_buzz(10) == [1, 1, 2, 'Fizz', 'Buzz', 8, 13, 'Fizz', 34,
                                  'Buzz']
    assert fibs_fizz_buzz(15) == [1, 1, 2, 'Fizz', 'Buzz', 8, 13, 'Fizz', 34,
                                  'Buzz', 89, 'Fizz', 233, 377, 'Buzz']
    assert fibs_fizz_buzz(20) == [1, 1, 2, "Fizz", "Buzz", 8, 13, "Fizz",
                                  34, "Buzz", 89, "Fizz", 233, 377, "Buzz",
                                  "Fizz", 1597, 2584, 4181, "FizzBuzz"]
