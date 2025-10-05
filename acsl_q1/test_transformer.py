import pytest
from transformer import transform

# List of test cases: (input_string, expected_output)
test_cases = [
    ("124987 2 3", "124950"),
    ("540670 3 9", "540300"),
    ("7145042 2 8", "7145020"),
    ("124987 2 523", "124950"),
    ("4386709 1 2", "4386707"),
]


@pytest.mark.parametrize("input_str,expected", test_cases)
def test_transform(input_str, expected):
    """
    Tests the transform function with various inputs.
    These tests will fail until the function is implemented.
    """
    assert transform(input_str) == expected
