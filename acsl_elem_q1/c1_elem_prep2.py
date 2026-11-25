"""
ACSL Elementary Contest 1 - Warmup 2: Decimal to Binary
=======================================================

GOAL:
Learn how to convert a normal decimal (base-10) number into a binary (base-2) string.

PROBLEM:
Convert a non-negative decimal integer `n` into its binary string representation.

HOW IT WORKS (Repeated Division by 2):
For n = 45:
  45 / 2 = 22 remainder 1
  22 / 2 = 11 remainder 0
  11 / 2 = 5  remainder 1
   5 / 2 = 2  remainder 1
   2 / 2 = 1  remainder 0
   1 / 2 = 0  remainder 1
Read remainders from bottom to top: "101101"

EXAMPLES:
  decimal_to_binary(0)  -> "0"
  decimal_to_binary(5)  -> "101"
  decimal_to_binary(12) -> "1100"
  decimal_to_binary(45) -> "101101"

HINTS:
  1. Special case: if `n == 0`, return `"0"`.
  2. Use a `while n > 0:` loop:
       - Get remainder: `rem = n % 2`
       - Add `str(rem)` to the FRONT of your result string: `result = str(rem) + result`
       - Divide `n` by 2: `n = n // 2`
  (Built-in shortcut to check your work: `bin(n)[2:]`)

HOW TO TEST:
  python3 c1_elem_prep2.py
  or
  pytest c1_elem_prep2.py
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


def decimal_to_binary(n: int) -> str:
    # TODO: Write your code here! Replace `pass` with your solution.
    pass


test_cases = [
    (0, "0"),
    (1, "1"),
    (5, "101"),
    (12, "1100"),
    (21, "10101"),
    (45, "101101"),
    (255, "11111111"),
]


@pytest.mark.parametrize("n,expected", test_cases)
def test_decimal_to_binary(n, expected):
    assert decimal_to_binary(n) == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Testing c1_elem_prep2.py (decimal_to_binary)...")
    print("=" * 60)
    passed = 0
    for n, expected in test_cases:
        try:
            res = decimal_to_binary(n)
            if res == expected:
                print(f"  [PASS] {n} -> '{res}'")
                passed += 1
            else:
                print(f"  [FAIL] {n} -> got '{res}', expected '{expected}'")
        except Exception as e:
            print(f"  [NOT YET] {n} -> expected '{expected}' ({type(e).__name__})")

    print("\n" + "=" * 60)
    if passed == len(test_cases):
        print(f"🎉 GREAT JOB! All {passed}/{len(test_cases)} tests passed! Ready for c1_elem_prep3.py!")
    else:
        print(f"Score: {passed}/{len(test_cases)} tests passed. Keep working on it!")
    print("=" * 60)
