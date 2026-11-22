"""
ACSL Contest 1 - Warmup 1: Ring Toss Scoring
============================================

GOAL:
Learn how to loop through a string, check each character, and add up points.

PROBLEM:
In the ACSL Rings game, tossing a ball through a colored ring gives you points:
  - Aqua   ('A') : 1 point
  - Red    ('R') : 1 point
  - Orange ('O') : 3 points
  - Green  ('G') : 3 points
  - Black  ('B') : 6 points

TASK:
Write a function `score_ring_toss(tosses)` that takes a string of throws
(like "BRAG") and returns the total score as an integer.

EXAMPLES:
  score_ring_toss("BRAG")     -> 11   # B(6) + R(1) + A(1) + G(3) = 11
  score_ring_toss("BOB")      -> 15   # B(6) + O(3) + B(6) = 15
  score_ring_toss("AABBOOGG") -> 26   # 1+1+6+6+3+3+3+3 = 26
  score_ring_toss("")         -> 0

HINTS:
  1. Start with a variable: `total = 0`
  2. Use a `for` loop to look at each letter:
         for char in tosses:
  3. Use `if/elif/else` to add points to `total`:
         if char == 'A' or char == 'R':
             total += 1
         elif ...
     (Alternative: use a dictionary like `points = {'A': 1, 'R': 1, ...}`)
  4. Don't forget to `return total` at the end!

HOW TO TEST:
  Run in terminal:
      python3 c1_prep1.py
  or
      pytest c1_prep1.py
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


def score_ring_toss(tosses: str) -> int:
    # TODO: Write your code here! Replace `pass` with your solution.
    pass


# ==============================================================================
# TESTS
# ==============================================================================
test_cases = [
    ("BRAG", 11),
    ("BOB", 15),
    ("AABBOOGG", 26),
    ("BAROBA", 18),
    ("AAAA", 4),
    ("BBBB", 24),
    ("OG", 6),
    ("", 0),
]


@pytest.mark.parametrize("tosses,expected", test_cases)
def test_score_ring_toss(tosses, expected):
    assert score_ring_toss(tosses) == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Testing c1_prep1.py (score_ring_toss)...")
    print("=" * 60)
    passed = 0
    for tosses, expected in test_cases:
        try:
            res = score_ring_toss(tosses)
            if res == expected:
                print(f"  [PASS] '{tosses}' -> {res}")
                passed += 1
            else:
                print(f"  [FAIL] '{tosses}' -> got {res}, expected {expected}")
        except Exception as e:
            print(f"  [NOT YET] '{tosses}' -> expected {expected} ({type(e).__name__})")

    print("\n" + "=" * 60)
    if passed == len(test_cases):
        print(f"🎉 AMAZING! All {passed}/{len(test_cases)} tests passed! Ready for c1_prep2.py!")
    else:
        print(f"Score: {passed}/{len(test_cases)} tests passed. Keep working on it!")
    print("=" * 60)
