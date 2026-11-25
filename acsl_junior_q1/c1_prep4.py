"""
ACSL Contest 1 - Warmup 4: Character Counting & Multipliers
===========================================================

GOAL:
Learn how to count specific characters in a string and calculate values quickly.

PROBLEM:
In many ACSL problems, instead of checking character-by-character, you can count
how many times a letter appears and multiply by its point value.

For example, in "AABBOOGG":
  - 'B' appears 2 times. If each 'B' is worth 6 points:
      points = 2 * 6 = 12

TASK:
Write a function `count_and_score(text, target, points_per_item)` that:
  1. Counts how many times `target` appears in `text`.
  2. Multiplies that count by `points_per_item`.
  3. Returns the total points as an integer.

EXAMPLES:
  count_and_score("AABBOOGG", "B", 6) -> 12    # 2 * 6 = 12
  count_and_score("BRAG", "A", 1)      -> 1     # 1 * 1 = 1
  count_and_score("BBBBBB", "B", 6)    -> 36    # 6 * 6 = 36
  count_and_score("ROBR", "G", 3)      -> 0     # 0 * 3 = 0

HINTS:
  Python strings have a super handy `.count()` method:
      occurrences = text.count(target)
      return occurrences * points_per_item

  (Or you can use a loop with a counter variable!)

HOW TO TEST:
  Run in terminal:
      python3 c1_prep4.py
  or
      pytest c1_prep4.py
"""

import pytest

def count_and_score(text: str, target: str, points_per_item: int) -> int:
    # TODO: Write your code here! Replace `pass` with your solution.
    pass


# ==============================================================================
# TESTS
# ==============================================================================
test_cases = [
    ("AABBOOGG", "B", 6, 12),
    ("BRAG", "A", 1, 1),
    ("BBBBBB", "B", 6, 36),
    ("ROBR", "G", 3, 0),
    ("AAAAA", "A", 1, 5),
    ("OOGG", "O", 3, 6),
    ("", "B", 6, 0),
]


@pytest.mark.parametrize("text,target,points_per_item,expected", test_cases)
def test_count_and_score(text, target, points_per_item, expected):
    assert count_and_score(text, target, points_per_item) == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Testing c1_prep4.py (count_and_score)...")
    print("=" * 60)
    passed = 0
    for text, target, pts, expected in test_cases:
        try:
            res = count_and_score(text, target, pts)
            if res == expected:
                print(f"  [PASS] ('{text}', '{target}', {pts}) -> {res}")
                passed += 1
            else:
                print(f"  [FAIL] ('{text}', '{target}', {pts}) -> got {res}, expected {expected}")
        except Exception as e:
            print(f"  [NOT YET] ('{text}', '{target}', {pts}) -> expected {expected} ({type(e).__name__})")

    print("\n" + "=" * 60)
    if passed == len(test_cases):
        print(f"🎉 GREAT WORK! All {passed}/{len(test_cases)} tests passed! Ready for c1_prep5.py!")
    else:
        print(f"Score: {passed}/{len(test_cases)} tests passed. Keep working on it!")
    print("=" * 60)
