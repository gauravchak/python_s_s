"""
ACSL Elementary Contest 1 - Warmup 5: Comparing Different Bases
===============================================================

GOAL:
Solve a classic ACSL Elementary Contest 1 question: comparing numbers written
in different bases (binary, octal, decimal, hexadecimal) to find the largest!

PROBLEM:
You are given a list of `(number_str, base)` pairs, such as:
  [("10101", 2), ("24", 8), ("1A", 16)]

Find which pair has the LARGEST decimal value, and return its decimal value.

EXAMPLES:
  largest_value([("10101", 2), ("24", 8), ("1A", 16)]) -> 26
    Why?
      "10101" in base 2  = 21
      "24"    in base 8  = 20
      "1A"    in base 16 = 26
      Largest is 26!

  largest_value([("1100", 2), ("14", 8), ("C", 16)]) -> 12
    (All three equal 12!)

HINTS:
  1. You can convert any `num_str` in `base` to decimal with:
         value = int(num_str, base)
     (Or write a general loop using `base`!)
  2. Keep track of `best = 0` (or convert all of them into a list and use `max(...)`).

HOW TO TEST:
  python3 c1_elem_prep5.py
  or
  pytest c1_elem_prep5.py
"""

try:
    import pytest
except ImportError:
    class _DummyMark:
        @staticmethod
        def parametrize(*args, **kwargs):
            return lambda fn: fn

    class _DummyPytest:
        mark = _DummyMark()

    pytest = _DummyPytest()


def largest_value(items: list[tuple[str, int]]) -> int:
    # TODO: Write your code here! Replace `pass` with your solution.
    pass


test_cases = [
    ([("10101", 2), ("24", 8), ("1A", 16)], 26),
    ([("1100", 2), ("14", 8), ("C", 16)], 12),
    ([("1111", 2), ("17", 8), ("10", 16)], 16),
    ([("100000", 2), ("42", 8), ("21", 16)], 34),
    ([("101", 10), ("101", 8), ("101", 16)], 257),
]


@pytest.mark.parametrize("items,expected", test_cases)
def test_largest_value(items, expected):
    assert largest_value(items) == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Testing c1_elem_prep5.py (largest_value)...")
    print("=" * 60)
    passed = 0
    for items, expected in test_cases:
        try:
            res = largest_value(items)
            if res == expected:
                print(f"  [PASS] {items} -> {res}")
                passed += 1
            else:
                print(f"  [FAIL] {items} -> got {res}, expected {expected}")
        except Exception as e:
            print(f"  [NOT YET] {items} -> expected {expected} ({type(e).__name__})")

    print("\n" + "=" * 60)
    if passed == len(test_cases):
        print(f"🏆 CONGRATULATIONS! All {passed}/{len(test_cases)} tests passed!")
        print("You're ready for ACSL Elementary Contest 1: Computer Number Systems!")
    else:
        print(f"Score: {passed}/{len(test_cases)} tests passed. Keep working on it!")
    print("=" * 60)
