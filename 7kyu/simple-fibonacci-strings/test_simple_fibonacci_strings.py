"""Simple fibonacci strings test cases."""
from simple_fibonacci_strings import simple_fibonacci_strings


def test_case_three():
    """Test case when n is 2, 3, 4."""
    assert simple_fibonacci_strings(2) == '010'
    assert simple_fibonacci_strings(3) == '01001'
    assert simple_fibonacci_strings(4) == '01001010'
