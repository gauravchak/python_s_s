"""Test driven development.

We will write the tests first, then implement the functions.
"""

def get_gcf(x:int, y:int) -> int:
    """Returns the greatest common factor of x and y"""
    assert x >= 0 and y >= 0, "Both x and y must be positive"
    if x == 0:
        return y
    if y == 0:
        return x
    if x == y:
        return x
    # Euclid's algorithm
    # If x > y, then the GCF of x and y is the same as the GCF of x-y and y
    # This is because if `a` divides x and y, then it also divides x-y and y
    # x = k * a, y = l * a, then x-y = k * a - l * a = (k-l) * a
    # Since k-l is an integer, x-y is an integer times a, 
    # hence (x-y) also divisible by a.
    # Hence any factor of x and y is also a factor of x-y and y.
    if x > y:
        return get_gcf(x-y, y)
    else:
        return get_gcf(x, y-x)

x: int = 36
y: int = 24
expected: int = 12
result: int = get_gcf(x, y)
assert result == expected, f"Result is {result}, we were expecting {expected}"

x: int = 70
y: int = 35
expected: int = 35
result: int = get_gcf(x, y)
assert result == expected, f"Result is {result}, we were expecting {expected}"