"""
Convert infix expression to postfix expression using a stack.
"""

from typing import List


def precedence(op):
    """Return the precedence of the given operator."""
    if op in ("+", "-"):
        return 1
    if op in ("*", "/"):
        return 2
    if op == "^":
        return 3
    return 0


def is_right_associative(op):
    """
    Return True if operator is right-associative.
    For typical math usage, '^' is right-associative.
    """
    return op == "^"


def infix_to_postfix(tokens):
    """
    Convert infix tokens to postfix tokens using a standard stack-based algo:
      1. For operands, add to output.
      2. For '(', push to stack.
      3. For ')', pop from stack to output until '(' is found.
      4. For operators, pop from stack to output while top of stack has
         higher or (if left-associative) equal precedence.
    """
    stack = []
    output = []
    for token in tokens:
        # If token is operand (not operator or parentheses)
        if token not in {"+", "-", "*", "/", "^", "(", ")"}:
            output.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()  # remove '(' from stack
        else:
            # token is an operator: +, -, *, /, ^
            while stack and stack[-1] != "(":
                top_op = stack[-1]
                # Compare precedence of the top of stack with current operator
                top_precedence = precedence(top_op)
                current_precedence = precedence(token)

                # (A) If you want '^' to be left-associative (less common):
                # condition = (top_precedence >= current_precedence)

                # (B) If you want '^' to be right-associative (typical):
                # pop while top has strictly greater precedence,
                # or same precedence with left-associative
                if (top_precedence > current_precedence) or (
                    top_precedence == current_precedence
                    and not is_right_associative(token)
                ):
                    # The reason we output here is that the lower precedence
                    # operator indicates the sub expression should be evaluated
                    # first. So we pop it and add to the output.
                    # e.g. "3 * 4 + ..." -> output: "3 4 *" ; stack: "+"
                    output.append(stack.pop())
                else:
                    break

            stack.append(token)

    # pop all the operators from the stack
    while stack:
        output.append(stack.pop())
    return output


# Example usage
input_str: str = "3 + 4 * 5"
itokens: List[str] = input_str.split()
result: List[str] = infix_to_postfix(itokens)
print(" ".join(result))  # "3 4 5 * +"
