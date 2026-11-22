"""
ACSL Contest 1 - Warmup 3: Mini-Rings Game
==========================================

GOAL:
Combine the functions you wrote in Prep 1 and Prep 2 to solve a full 2-player game!
This shows how real programmers solve big problems by combining smaller building blocks.

PROBLEM:
Two players play the ACSL Rings game:
  - Aqua  ('A') or Red   ('R') = 1 point
  - Orange('O') or Green ('G') = 3 points
  - Black ('B')                = 6 points

TASK:
Write a function `mini_rings(player1, player2)` that:
  1. Calculates Player 1's score.
  2. Calculates Player 2's score.
  3. Returns a string with the higher score first, separated by a space.

EXAMPLES:
  mini_rings("BRAG", "BOB") -> "15 11"
    Player 1 ("BRAG"): 6 + 1 + 1 + 3 = 11
    Player 2 ("BOB"):  6 + 3 + 6 = 15
    Larger first: "15 11"

  mini_rings("AABBOOGG", "BAROBA") -> "26 18"
    Player 1: 1+1+6+6+3+3+3+3 = 26
    Player 2: 6+1+1+3+6+1 = 18
    Larger first: "26 18"

HINTS:
  - You can write a helper function to calculate the score for one player
    (just like you did in c1_prep1.py!).
  - Then use `max()` and `min()` (like in c1_prep2.py!) to format the result!

HOW TO TEST:
  Run in terminal:
      python3 c1_prep3.py
  or
      pytest c1_prep3.py
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


def mini_rings(player1: str, player2: str) -> str:
    # TODO: Write your code here! Replace `pass` with your solution.
    pass


# ==============================================================================
# TESTS
# ==============================================================================
test_cases = [
    ("BRAG", "BOB", "15 11"),
    ("AABBOOGG", "BAROBA", "26 18"),
    ("GBORABORBA", "BAAAAOORGGGB", "32 31"),
    ("AAAA", "BBBB", "24 4"),
    ("OG", "OG", "6 6"),
]


@pytest.mark.parametrize("player1,player2,expected", test_cases)
def test_mini_rings(player1, player2, expected):
    assert mini_rings(player1, player2) == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Testing c1_prep3.py (mini_rings)...")
    print("=" * 60)
    passed = 0
    for p1, p2, expected in test_cases:
        try:
            res = mini_rings(p1, p2)
            if res == expected:
                print(f"  [PASS] ('{p1}', '{p2}') -> '{res}'")
                passed += 1
            else:
                print(f"  [FAIL] ('{p1}', '{p2}') -> got '{res}', expected '{expected}'")
        except Exception as e:
            print(f"  [NOT YET] ('{p1}', '{p2}') -> expected '{expected}' ({type(e).__name__})")

    print("\n" + "=" * 60)
    if passed == len(test_cases):
        print(f"🎉 FANTASTIC! All {passed}/{len(test_cases)} tests passed! You can already solve ACSL Rings!")
        print("Ready for c1_prep4.py to learn string counting tricks!")
    else:
        print(f"Score: {passed}/{len(test_cases)} tests passed. Keep working on it!")
    print("=" * 60)
