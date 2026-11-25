"""
ACSL Elementary Contest 1 - Warmup 3: Octal (Base 8) to Decimal
===============================================================

GOAL:
Learn how base-8 (octal) numbers work, using digits 0 through 7.

PROBLEM:
Convert an octal (base-8) string like "14" or "72" into a decimal (base-10) integer.

HOW OCTAL WORKS:
Each digit from right to left represents a power of 8: 1, 8, 64, 512...
For "14" (base 8):
  1*8 + 4*1 = 12
For "72" (base 8):
  7*8 + 2*1 = 58

EXAMPLES:
  octal_to_decimal("7")   -> 7
  octal_to_decimal("14")  -> 12
  octal_to_decimal("72")  -> 58
  octal_to_decimal("100") -> 64

HINTS:
  Method 1 (Loop from left to right — just like binary, but multiply by 8!):
      total = 0
      for digit in octal_str:
          total = total * 8 + int(digit)
      return total

  Method 2 (Built-in shortcut):
      return int(octal_str, 8)

HOW TO TEST:
  python3 c1_elem_prep3.py
  or
  pytest c1_elem_prep3.py
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


def octal_to_decimal(octal_str: str) -> int:
    # TODO: Write your code here! Replace `pass` with your solution.
    pass


test_cases = [
    ("0", 0),
    ("7", 7),
    ("10", 8),
    ("14", 12),
    ("72", 58),
    ("100", 64),
    ("377", 255),
]


@pytest.mark.parametrize("octal_str,expected", test_cases)
def test_octal_to_decimal(octal_str, expected):
    assert octal_to_decimal(octal_str) == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Testing c1_elem_prep3.py (octal_to_decimal)...")
    print("=" * 60)
    passed = 0
    for oct_s, expected in test_cases:
        try:
            res = octal_to_decimal(oct_s)
            if res == expected:
                print(f"  [PASS] '{oct_s}' (base 8) -> {res}")
                passed += 1
            else:
                print(f"  [FAIL] '{oct_s}' (base 8) -> got {res}, expected {expected}")
        except Exception as e:
            print(f"  [NOT YET] '{oct_s}' -> expected {expected} ({type(e).__name__})")

    print("\n" + "=" * 60)
    if passed == len(test_cases):
        print(f"🎉 AWESOME! All {passed}/{len(test_cases)} tests passed! Ready for c1_elem_prep4.py!")
    else:
        print(f"Score: {passed}/{len(test_cases)} tests passed. Keep working on it!")
    print("=" * 60)
