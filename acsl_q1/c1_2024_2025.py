"""
ACSL 2024-2025 | Contest 1: Rings (Junior Division)
===================================================

PROBLEM DESCRIPTION:
ACSL Rings is a 2-player game where the object is to score points by tossing a
ball through one of the 5 rings. Points are awarded as follows:

  - Through the aqua or red ring   (A or R) : 1 point
  - Through the orange or green ring (O or G) : 3 points
  - Through the black ring             (B)   : 6 points

We will use a single letter to represent each of the colors:
  aqua (A), red (R), orange (O), green (G), and black (B).

INPUT:
You will be given 2 strings representing each player's results for all tosses that
go through one of the rings. Each string will be no more than 100 characters.

OUTPUT:
Output a string containing each player's score with the larger score first,
separated by a single space (e.g. "15 11").
If both players have the same score, it doesn't matter which one appears first (e.g. "84 84").

EXAMPLE:
  Player 1: BRAG
  Player 2: BOB

  Player 1 tosses:
    B (6) + R (1) + A (1) + G (3) = 11 points
  Player 2 tosses:
    B (6) + O (3) + B (6) = 15 points

  Output: "15 11" (larger score first)
"""


def calculate_score(tosses: str) -> int:
    """
    Helper function to calculate the score for a single player's tosses.

    Point values:
      'A': 1, 'R': 1
      'O': 3, 'G': 3
      'B': 6

    Example:
      calculate_score("BRAG") -> 11
      calculate_score("BOB")  -> 15
    """
    # TODO for student: calculate and return the total points for `tosses`
    pass


def solve_rings(player1: str, player2: str) -> str:
    """
    Main function:
    Given two strings `player1` and `player2`, calculate each player's score
    and return the two scores formatted as a string with the larger score first,
    separated by a space.

    Example:
      solve_rings("BRAG", "BOB") -> "15 11"
    """
    # TODO for student:
    # 1. Calculate score for player 1
    # 2. Calculate score for player 2
    # 3. Determine which is higher
    # 4. Return as "HIGHER LOWER"
    pass


def solve_from_input_str(input_str: str) -> str:
    """
    Optional helper: parses a single input string that contains both players'
    tosses separated by whitespace or newlines (common in contest platforms).

    Example:
      solve_from_input_str("BRAG\\nBOB") -> "15 11"
      solve_from_input_str("BRAG BOB")   -> "15 11"
    """
    parts = input_str.strip().split()
    if len(parts) == 2:
        return solve_rings(parts[0], parts[1])
    return ""


if __name__ == "__main__":
    print("Testing solve_rings with the example from the problem:")
    result = solve_rings("BRAG", "BOB")
    print(f"Result: {result} (Expected: '15 11')")
