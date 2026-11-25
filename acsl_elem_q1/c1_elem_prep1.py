"""
ACSL Elementary Contest 1 - Warmup 1: Binary to Decimal
=======================================================

NOTE ON ELEMENTARY DIVISION:
In ACSL Elementary Division (Grades 3-6), Contest 1 is a 5-question
non-programming test on Computer Number Systems (binary, octal, hex, decimal).
These Python exercises help you practice the exact math and logic by coding it!

PROBLEM:
Convert a binary (base-2) string like "10101" into a decimal (base-10) integer.

HOW BINARY WORKS:
Each digit from right to left represents a power of 2: 1, 2, 4, 8, 16, 32...
For "10101":
  1*16 + 0*8 + 1*4 + 0*2 + 1*1 = 21

   0 - 0
   1 - 1
  10 - 2
  11 - 3
 100 - 4
 101 - 5
 110 - 6
 111 - 7
1000 - 8
EXAMPLES:
  binary_to_decimal("10101") -> 21
  binary_to_decimal("1100")  -> 12
  binary_to_decimal("1")     -> 1
  binary_to_decimal("0")     -> 0

HINTS:
  Method 1 (Loop from left to right):
      total = 0
      for bit in binary_str:
          total = total * 2 + int(bit)
      return total

  Method 2 (Built-in Python shortcut — try Method 1 first!):
      return int(binary_str, 2)

HOW TO TEST:
  python3 c1_elem_prep1.py
  or
  pytest c1_elem_prep1.py
"""

import pytest


def binary_to_decimal(binary_str: str) -> int:
    place_value = 1
    final_sum = 0
    for i in range(len(binary_str)):
        bit = binary_str[len(binary_str)-1 - i]
        if bit == '1':
            final_sum = final_sum + place_value
        place_value = place_value * 2
    return final_sum


test_cases = [
    ("0", 0),
    ("1", 1),
    ("101", 5),
    ("1100", 12),
    ("10101", 21),
    ("00110101", 53),
    ("11111111", 255),
]


@pytest.mark.parametrize("binary_str,expected", test_cases)
def test_binary_to_decimal(binary_str, expected):
    assert binary_to_decimal(binary_str) == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Testing c1_elem_prep1.py (binary_to_decimal)...")
    print("=" * 60)
    passed = 0
    for b, expected in test_cases:
        try:
            res = binary_to_decimal(b)
            if res == expected:
                print(f"  [PASS] '{b}' -> {res}")
                passed += 1
            else:
                print(f"  [FAIL] '{b}' -> got {res}, expected {expected}")
        except Exception as e:
            print(f"  [NOT YET] '{b}' -> expected {expected} ({type(e).__name__})")

    print("\n" + "=" * 60)
    if passed == len(test_cases):
        print(f"🎉 AWESOME! All {passed}/{len(test_cases)} tests passed! Ready for c1_elem_prep2.py!")
    else:
        print(f"Score: {passed}/{len(test_cases)} tests passed. Keep working on it!")
    print("=" * 60)
