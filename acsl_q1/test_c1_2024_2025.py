"""
Pytest Test Suite for ACSL 2024-2025 Contest 1: Rings (Junior Division)
========================================================================

Run these tests with:
    pytest test_c1_2024_2025.py
or
    python3 test_c1_2024_2025.py
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
from c1_2024_2025 import calculate_score, solve_rings, solve_from_input_str


# ==============================================================================
# Helper Function Tests: Individual Player Scoring
# ==============================================================================
player_score_test_cases = [
    ("BRAG", 11),                   # B(6) + R(1) + A(1) + G(3) = 11
    ("BOB", 15),                    # B(6) + O(3) + B(6) = 15
    ("AABBOOGG", 26),               # 1+1+6+6+3+3+3+3 = 26
    ("BAROBA", 18),                 # 6+1+1+3+6+1 = 18
    ("GBORABORBA", 32),
    ("BAAAAOORGGGB", 31),
    ("OORRRGRBBRRAAABB", 35),
    ("AAAAGRRRRGRRRBBOO", 42),
    ("BARROGGBBGO", 36),
    ("BBAAAARRRGGGOOOO", 40),
]


@pytest.mark.parametrize("tosses,expected_score", player_score_test_cases)
def test_calculate_score(tosses, expected_score):
    """Verifies that individual player scores are correctly computed."""
    assert calculate_score(tosses) == expected_score


# ==============================================================================
# Official Sample Inputs & Outputs (from page 2 of the ACSL Contest Packet)
# ==============================================================================
sample_cases = [
    ("BRAG", "BOB", "15 11"),
    ("AABBOOGG", "BAROBA", "26 18"),
    ("GBORABORBA", "BAAAAOORGGGB", "32 31"),
    ("OORRRGRBBRRAAABB", "AAAAGRRRRGRRRBBOO", "42 35"),
    ("BARROGGBBGO", "BBAAAARRRGGGOOOO", "40 36"),
    ("AAAABBBOOGGGRRR", "RRBBOOOGGGAAAA", "40 36"),
]


@pytest.mark.parametrize("player1,player2,expected", sample_cases)
def test_sample_inputs(player1, player2, expected):
    """Tests the official ACSL Sample Inputs 1 through 6."""
    assert solve_rings(player1, player2) == expected


# ==============================================================================
# Official Test Data & Outputs (from page 3 of the ACSL Contest Packet)
# ==============================================================================
official_test_data = [
    ("AROBG", "BRAGGROG", "21 14"),
    ("BOBBRAGROB", "BARBAGGRAB", "36 29"),
    ("BBBAAAOOOGGGRRR", "BBBBBAAAAGGGOOR", "50 42"),
    ("RRRRRRBBBBGGGGGGAAAO", "AAAAAAOOOOOORRRBBBBB", "57 54"),
    ("BABAGORBABAGORBABAGORBABAGOR", "GORBAGORBAGORBAGORBAGORBAGORBA", "84 84"),
    ("RRRGGGGBBBBAAOOOBBBAAARRBB", "BBBBAAAAOOOOBBBGGGRRRGOAGOAGO", "90 85"),
]


@pytest.mark.parametrize("player1,player2,expected", official_test_data)
def test_official_contest_data(player1, player2, expected):
    """Tests the official ACSL Test Data 1 through 6."""
    assert solve_rings(player1, player2) == expected


# ==============================================================================
# Single-String Input Parser Test (HackerRank / Contest Harness style)
# ==============================================================================
@pytest.mark.parametrize("player1,player2,expected", sample_cases)
def test_solve_from_input_str(player1, player2, expected):
    """Tests that the newline- or space-separated input string parser works."""
    assert solve_from_input_str(f"{player1}\n{player2}") == expected
    assert solve_from_input_str(f"{player1} {player2}") == expected


if __name__ == "__main__":
    print("=" * 60)
    print("Running tests for c1_2024_2025.py...")
    print("=" * 60)

    passed = 0
    total = len(sample_cases) + len(official_test_data)

    for p1, p2, exp in sample_cases + official_test_data:
        try:
            res = solve_rings(p1, p2)
            if res == exp:
                print(f"  [PASS] ({p1}, {p2}) -> {res}")
                passed += 1
            else:
                print(f"  [FAIL] ({p1}, {p2}) -> got '{res}', expected '{exp}'")
        except Exception as e:
            print(f"  [NOT YET] ({p1}, {p2}) -> expected '{exp}' ({type(e).__name__})")

    print(f"\nScore: {passed}/{total} tests passed.")
    if passed == total:
        print("🎉 Congratulations! All 2024-2025 ACSL Contest 1 tests passed!")
    else:
        print("Keep working on solve_rings() in c1_2024_2025.py!")
