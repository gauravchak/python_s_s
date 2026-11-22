"""
ACSL Contest 1 - Warmup 6: Digit Transformation (Modulo & Abs)
==============================================================

GOAL:
Master conditional branching, the modulo operator (%), absolute value, and string slicing.
This is the core math logic used in ACSL 2019-2020 Contest 1!

PROBLEM:
Given a single `digit` (from 0 through 9) and a number `d`:
  - Rule 1: If `digit` is between 0 and 4:
      Add `d` to `digit`, and keep only the UNITS (last) digit.
      Example: digit=2, d=3  -> 2 + 3 = 5 (units digit is 5)
      Example: digit=4, d=8  -> 4 + 8 = 12 (units digit is 2)

  - Rule 2: If `digit` is between 5 and 9:
      Find the absolute difference |digit - d|, and keep only the LEFTMOST (first) digit.
      Example: digit=8, d=3   -> |8 - 3| = 5 (leftmost digit is 5)
      Example: digit=7, d=8   -> |7 - 8| = 1 (leftmost digit is 1)
      Example: digit=9, d=523 -> |9 - 523| = 514 (leftmost digit is 5)

TASK:
Write a function `transform_digit(digit, d)` that returns the new single digit
as an integer.

HINTS:
  - Check which rule applies:
        if 0 <= digit <= 4:
            # Rule 1
            return (digit + d) % 10
        else:
            # Rule 2
            diff = abs(digit - d)
            # To get the leftmost digit: convert to str, take index 0, convert to int!
            return int(str(diff)[0])

HOW TO TEST:
  Run in terminal:
      python3 c1_prep6.py
  or
      pytest c1_prep6.py
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


def transform_digit(digit: int, d: int) -> int:
    # TODO: Write your code here! Replace `pass` with your solution.
    pass


# ==============================================================================
# TESTS
# ==============================================================================
test_cases = [
    (2, 3, 5),          # 2 + 3 = 5
    (4, 8, 2),          # 4 + 8 = 12 -> 2
    (0, 9, 9),          # 0 + 9 = 9
    (8, 3, 5),          # |8 - 3| = 5
    (9, 2, 7),          # |9 - 2| = 7
    (7, 8, 1),          # |7 - 8| = 1
    (9, 523, 5),        # |9 - 523| = 514 -> leftmost digit is 5
    (5, 15, 1),         # |5 - 15| = 10 -> leftmost digit is 1
]


@pytest.mark.parametrize("digit,d,expected", test_cases)
def test_transform_digit(digit, d, expected):
    assert transform_digit(digit, d) == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Testing c1_prep6.py (transform_digit)...")
    print("=" * 60)
    passed = 0
    for digit, d, expected in test_cases:
        try:
            res = transform_digit(digit, d)
            if res == expected:
                print(f"  [PASS] (digit={digit}, d={d}) -> {res}")
                passed += 1
            else:
                print(f"  [FAIL] (digit={digit}, d={d}) -> got {res}, expected {expected}")
        except Exception as e:
            print(f"  [NOT YET] (digit={digit}, d={d}) -> expected {expected} ({type(e).__name__})")

    print("\n" + "=" * 60)
    if passed == len(test_cases):
        print(f"🏆 INCREDIBLE! All {passed}/{len(test_cases)} tests passed!")
        print("You have mastered all the core ACSL Contest 1 concepts!")
        print("Now you are ready to conquer the real contest: c1_2024_2025.py!")
    else:
        print(f"Score: {passed}/{len(test_cases)} tests passed. Keep working on it!")
    print("=" * 60)
