# A recursive function to compute the factorial of a number n.
def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Example usage:
# print(factorial(5))  # Output: 120


# Write a test on the factorial function.
def test_factorial():
    assert factorial(0) == 1, "Test case for 0 failed"
    assert factorial(1) == 1, "Test case for 1 failed"
    assert factorial(2) == 2, "Test case for 2 failed"
    assert factorial(3) == 6, "Test case for 3 failed"
    assert factorial(4) == 24, "Test case for 4 failed"
    assert factorial(5) == 120, "Test case for 5 failed"
    assert factorial(6) == 720, "Test case for 6 failed"
    print("All test cases passed!")


test_factorial()
# Output:
# All test cases passed!
