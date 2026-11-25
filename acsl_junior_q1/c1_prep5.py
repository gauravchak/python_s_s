"""
ACSL Contest 1 - Warmup 5: Digit Hunting from the Right
=======================================================

GOAL:
Learn how to pick a digit from a number counting from the RIGHT side.
(This is an essential skill for ACSL Contest 1 problems like Number Transformation).

PROBLEM:
In ACSL, questions often ask for the "P-th digit from the right" of a number N.
In the number 124987:
  - 1st digit from the right: 7 (the units place)
  - 2nd digit from the right: 8 (the tens place)
  - 3rd digit from the right: 9 (the hundreds place)
  - 4th digit from the right: 4
  - 5th digit from the right: 2
  - 6th digit from the right: 1

TASK:
Write a function `get_digit_from_right(number, p)` that returns the P-th digit
from the right as an integer.

EXAMPLES:
  get_digit_from_right(124987, 2)  -> 8
  get_digit_from_right(540670, 3)  -> 6
  get_digit_from_right(7145042, 1) -> 2
  get_digit_from_right(4386709, 7) -> 4

HINTS:
  1. Convert the number to a string first:
         s = str(number)
  2. Python has a secret superpower: negative indexing!
         s[-1] is the 1st character from the right.
         s[-2] is the 2nd character from the right.
         s[-p] is the P-th character from the right!
  3. Convert the character back to an integer:
         return int(s[-p])

HOW TO TEST:
  Run in terminal:
      python3 c1_prep5.py
  or
      pytest c1_prep5.py
"""

import pytest

def get_digit_from_right(number: int, p: int) -> int:
    # TODO: Write your code here! Replace `pass` with your solution.
    pass


# ==============================================================================
# TESTS
# ==============================================================================
test_cases = [
    (124987, 1, 7),
    (124987, 2, 8),
    (124987, 3, 9),
    (124987, 4, 4),
    (124987, 5, 2),
    (124987, 6, 1),
    (540670, 3, 6),
    (7145042, 1, 2),
    (7145042, 2, 4),
    (4386709, 7, 4),
]


@pytest.mark.parametrize("number,p,expected", test_cases)
def test_get_digit_from_right(number, p, expected):
    assert get_digit_from_right(number, p) == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Testing c1_prep5.py (get_digit_from_right)...")
    print("=" * 60)
    passed = 0
    for num, p, expected in test_cases:
        try:
            res = get_digit_from_right(num, p)
            if res == expected:
                print(f"  [PASS] ({num}, p={p}) -> {res}")
                passed += 1
            else:
                print(f"  [FAIL] ({num}, p={p}) -> got {res}, expected {expected}")
        except Exception as e:
            print(f"  [NOT YET] ({num}, p={p}) -> expected {expected} ({type(e).__name__})")

    print("\n" + "=" * 60)
    if passed == len(test_cases):
        print(f"🎉 SUPERB! All {passed}/{len(test_cases)} tests passed! Ready for the final warmup: c1_prep6.py!")
    else:
        print(f"Score: {passed}/{len(test_cases)} tests passed. Keep working on it!")
    print("=" * 60)
