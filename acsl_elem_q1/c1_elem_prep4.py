"""
ACSL Elementary Contest 1 - Warmup 4: Hexadecimal (Base 16) to Decimal
======================================================================

GOAL:
Learn how hexadecimal (base-16) uses digits 0-9 AND letters A-F!

PROBLEM:
Convert a hexadecimal string (like "1A" or "FF") into a decimal integer.

HEX DIGITS:
  0-9 = 0 to 9
  A = 10, B = 11, C = 12, D = 13, E = 14, F = 15

Each position from right to left represents a power of 16: 1, 16, 256...
For "1A" (base 16):
  1*16 + 10*1 = 26

EXAMPLES:
  hex_to_decimal("C")  -> 12
  hex_to_decimal("1A") -> 26
  hex_to_decimal("2F") -> 47
  hex_to_decimal("FF") -> 255

HINTS:
  1. Make a dictionary for the hex letters (or all 16 digits):
         hex_map = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
  2. Loop through each character `ch` in `hex_str.upper()`:
         if ch in hex_map:
             val = hex_map[ch]
         else:
             val = int(ch)
         total = total * 16 + val
  (Built-in shortcut: `int(hex_str, 16)`)

HOW TO TEST:
  python3 c1_elem_prep4.py
  or
  pytest c1_elem_prep4.py
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


def hex_to_decimal(hex_str: str) -> int:
    # TODO: Write your code here! Replace `pass` with your solution.
    pass


test_cases = [
    ("0", 0),
    ("9", 9),
    ("A", 10),
    ("C", 12),
    ("1A", 26),
    ("2F", 47),
    ("FF", 255),
    ("100", 256),
]


@pytest.mark.parametrize("hex_str,expected", test_cases)
def test_hex_to_decimal(hex_str, expected):
    assert hex_to_decimal(hex_str) == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Testing c1_elem_prep4.py (hex_to_decimal)...")
    print("=" * 60)
    passed = 0
    for h, expected in test_cases:
        try:
            res = hex_to_decimal(h)
            if res == expected:
                print(f"  [PASS] '{h}' (base 16) -> {res}")
                passed += 1
            else:
                print(f"  [FAIL] '{h}' (base 16) -> got {res}, expected {expected}")
        except Exception as e:
            print(f"  [NOT YET] '{h}' -> expected {expected} ({type(e).__name__})")

    print("\n" + "=" * 60)
    if passed == len(test_cases):
        print(f"🎉 FANTASTIC! All {passed}/{len(test_cases)} tests passed! Ready for c1_elem_prep5.py!")
    else:
        print(f"Score: {passed}/{len(test_cases)} tests passed. Keep working on it!")
    print("=" * 60)
