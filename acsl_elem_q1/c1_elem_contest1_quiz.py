"""
ACSL Elementary Division - Contest 1 Practice Quiz (Computer Number Systems)
===========================================================================

In the real ACSL Elementary Division Contest 1, students take a 30-minute,
5-question test on Computer Number Systems (no coding required on test day!).

Here are 5 classic Elementary Contest 1 problems turned into quick Python
functions so you can practice the math and check your answers automatically!

HOW TO TEST:
  python3 c1_elem_contest1_quiz.py
  or
  pytest c1_elem_contest1_quiz.py
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


# Question 1: Binary to Decimal
# What is the decimal value of the binary string `b`?
# Example: "10101" -> 21
def q1_binary_to_decimal(b: str) -> int:
    # TODO: Replace `pass` with your code
    pass


# Question 2: Binary Addition
# Given two binary strings `b1` and `b2`, add them together and return the
# result as a binary string!
# Example: "1011", "110" -> "10001"  (11 + 6 = 17, which is 10001 in binary)
def q2_add_binary(b1: str, b2: str) -> str:
    # TODO: Replace `pass` with your code
    pass


# Question 3: Hexadecimal Color / Byte Value
# A pixel uses an 8-bit binary string like "00110101".
# Return its decimal value (0 to 255).
# Example: "00110101" -> 53
def q3_pixel_byte(byte_str: str) -> int:
    # TODO: Replace `pass` with your code
    pass


# Question 4: Octal + Hex Addition (in Decimal)
# Given an octal string `oct_str` and a hex string `hex_str`,
# return their sum in decimal (base 10).
# Example: oct_str="14" (12), hex_str="1A" (26) -> 38
def q4_oct_plus_hex(oct_str: str, hex_str: str) -> int:
    # TODO: Replace `pass` with your code
    pass


# Question 5: Count the 1s in Binary
# Given a decimal number `n`, convert it to binary and count how many '1' bits it has.
# Example: n=45 -> binary is "101101" -> has 4 ones -> return 4
def q5_count_ones_in_binary(n: int) -> int:
    # TODO: Replace `pass` with your code
    pass


# ==============================================================================
# TESTS
# ==============================================================================
def test_q1():
    assert q1_binary_to_decimal("10101") == 21
    assert q1_binary_to_decimal("1110") == 14


def test_q2():
    assert q2_add_binary("1011", "110") == "10001"
    assert q2_add_binary("111", "1") == "1000"


def test_q3():
    assert q3_pixel_byte("00110101") == 53
    assert q3_pixel_byte("11111111") == 255


def test_q4():
    assert q4_oct_plus_hex("14", "1A") == 38
    assert q4_oct_plus_hex("10", "A") == 18


def test_q5():
    assert q5_count_ones_in_binary(45) == 4
    assert q5_count_ones_in_binary(15) == 4
    assert q5_count_ones_in_binary(16) == 1


if __name__ == "__main__":
    print("=" * 60)
    print("ACSL Elementary Contest 1 - 5-Question Practice Quiz")
    print("=" * 60)

    checks = [
        ("Q1 (Binary to Decimal)", test_q1),
        ("Q2 (Binary Addition)", test_q2),
        ("Q3 (8-bit Pixel Byte)", test_q3),
        ("Q4 (Octal + Hex)", test_q4),
        ("Q5 (Count 1s in Binary)", test_q5),
    ]

    passed = 0
    for name, fn in checks:
        try:
            fn()
            print(f"  [PASS] {name}")
            passed += 1
        except Exception as e:
            print(f"  [NOT YET] {name} ({type(e).__name__})")

    print("\n" + "=" * 60)
    print(f"Quiz Score: {passed}/5")
    if passed == 5:
        print("🏆 PERFECT 5/5! You are ready for ACSL Elementary Contest 1!")
    print("=" * 60)
