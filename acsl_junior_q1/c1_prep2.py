"""
ACSL Contest 1 - Warmup 2: High to Low Formatter
================================================

GOAL:
Learn how to compare two numbers and format them into a single string.

PROBLEM:
In ACSL games like ACSL Rings, after calculating two players' scores, you must
output them in order from LARGEST to SMALLEST, separated by a single space.
If both scores are equal, either order is fine (e.g. "50 50").

TASK:
Write a function `format_scores(score1, score2)` that takes two integer scores
and returns a string with the higher score first.

EXAMPLES:
  format_scores(11, 15) -> "15 11"
  format_scores(26, 18) -> "26 18"
  format_scores(50, 50) -> "50 50"
  format_scores(0, 12)  -> "12 0"

HINTS:
  Method 1 (using max and min):
      higher = max(score1, score2)
      lower = min(score1, score2)
      return f"{higher} {lower}"

  Method 2 (using if/else):
      if score1 >= score2:
          return f"{score1} {score2}"
      else:
          return f"{score2} {score1}"

HOW TO TEST:
  Run in terminal:
      python3 c1_prep2.py
  or
      pytest c1_prep2.py
"""

import pytest

def format_scores(score1: int, score2: int) -> str:
    # TODO: Write your code here! Replace `pass` with your solution.
    pass


# ==============================================================================
# TESTS
# ==============================================================================
test_cases = [
    (11, 15, "15 11"),
    (26, 18, "26 18"),
    (31, 32, "32 31"),
    (42, 35, "42 35"),
    (40, 36, "40 36"),
    (50, 50, "50 50"),
    (0, 10, "10 0"),
    (100, 1, "100 1"),
]


@pytest.mark.parametrize("score1,score2,expected", test_cases)
def test_format_scores(score1, score2, expected):
    assert format_scores(score1, score2) == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Testing c1_prep2.py (format_scores)...")
    print("=" * 60)
    passed = 0
    for s1, s2, expected in test_cases:
        try:
            res = format_scores(s1, s2)
            if res == expected:
                print(f"  [PASS] ({s1}, {s2}) -> '{res}'")
                passed += 1
            else:
                print(f"  [FAIL] ({s1}, {s2}) -> got '{res}', expected '{expected}'")
        except Exception as e:
            print(f"  [NOT YET] ({s1}, {s2}) -> expected '{expected}' ({type(e).__name__})")

    print("\n" + "=" * 60)
    if passed == len(test_cases):
        print(f"🎉 AWESOME JOB! All {passed}/{len(test_cases)} tests passed! Ready for c1_prep3.py!")
    else:
        print(f"Score: {passed}/{len(test_cases)} tests passed. Keep working on it!")
    print("=" * 60)
