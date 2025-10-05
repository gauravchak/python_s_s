# I want to make a file that is a challenge for my daughter to complete.
# It should have a function to implement a gcd approach using Euclid's algorithm.
def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two numbers using Euclid's algorithm.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: The greatest common divisor of a and b
    """


# Let's write some tests for the gcd function.
def test_gcd():
    assert gcd(48, 18) == 6, "Test case for (48, 18) failed"
    assert gcd(56, 98) == 14, "Test case for (56, 98) failed"
    assert gcd(101, 10) == 1, "Test case for (101, 10) failed"
    assert gcd(0, 5) == 5, "Test case for (0, 5) failed"
    assert gcd(5, 0) == 5, "Test case for (5, 0) failed"
    assert gcd(0, 0) == 0, "Test case for (0, 0) failed"
    print("All test cases passed!")
