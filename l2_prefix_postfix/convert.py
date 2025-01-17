"""
A program that takes

- type of expression infix/prefix/postfix
- the expression limited to words and operators separated by space
- then it prints the converted expression to the other two types.
"""

from typing import List
from remedy_space import add_spaces_around_operators_regex
from infix_to_postfix import infix_to_postfix


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


#
# Build Tree Functions
#


def build_tree_from_prefix(tokens_iter):
    """
    Build an expression tree from a prefix expression, using an iterator
    over the list of tokens.

    Algorithm (recursive):
      1. Read next token.
      2. If it's an operator, create a node, then build its left subtree,
         then build its right subtree.
      3. If it's an operand, create a leaf node.
    """
    try:
        token = next(tokens_iter)
    except StopIteration:
        return None

    node = Node(token)

    # Include ^ in the set of operators
    if token in {"+", "-", "*", "/", "^"}:
        node.left = build_tree_from_prefix(tokens_iter)
        node.right = build_tree_from_prefix(tokens_iter)

    return node


def build_tree_from_postfix(tokens_iter):
    """
    Build an expression tree from a postfix expression. We'll process tokens
    from left to right, but we need to store them so that we can pop from
    the end easily. So we can just treat 'tokens_iter' as a stack.

    Algorithm (stack-based):
      1. For each token:
         - If operand, push a leaf node onto the stack.
         - If operator, pop top 2 nodes, make them children, push operator
           node back.
    """
    stack = []
    for token in tokens_iter:
        # Include ^ in the set of operators
        if token not in {"+", "-", "*", "/", "^"}:
            # operand
            stack.append(Node(token))
        else:
            # operator
            right_node = stack.pop()
            left_node = stack.pop()
            new_node = Node(token)
            new_node.left = left_node
            new_node.right = right_node
            stack.append(new_node)
    return stack.pop() if stack else None


def build_tree_from_infix(tokens: List[str]):
    """
    Build an expression tree from an infix expression.

    For simplicity, we:
      1. Convert the infix to postfix using a standard algorithm.
      2. Then build a tree from that postfix.

    This approach automatically handles operator precedence for {+,-,*,/,^}.
    If you need parentheses or other operators, you'll need to extend the logic
    """
    postfix_tokens = infix_to_postfix(tokens)
    # Now build a tree from the postfix tokens
    return build_tree_from_postfix(postfix_tokens)


#
# Tree -> String Functions
#


def tree_to_prefix(node):
    """
    Return the prefix representation (root-left-right) of the expression tree.
    """
    if not node:
        return ""
    return " ".join(
        filter(
            None,
            [
                str(node.data),
                tree_to_prefix(node.left),
                tree_to_prefix(node.right),
            ],
        )
    )


def tree_to_infix(node):
    """
    Return the infix representation (left-root-right) of the expression tree.
    We add parentheses to preserve order, but you can omit if not needed.
    """
    if not node:
        return ""
    if not node.left and not node.right:
        # leaf node
        return str(node.data)
    left_expr = tree_to_infix(node.left)
    right_expr = tree_to_infix(node.right)
    return f"( {left_expr} {node.data} {right_expr} )"


def tree_to_postfix(node):
    """
    Return the postfix representation (left-right-root) of the expression tree.
    """
    if not node:
        return ""
    return " ".join(
        filter(
            None,
            [
                tree_to_postfix(node.left),
                tree_to_postfix(node.right),
                str(node.data),
            ],
        )
    )


#
# Evaluate the Expression Tree
#


def evaluate_tree(node):
    """
    Evaluate the expression tree using a recursive algorithm.
    Leaves (no children) are treated as numeric operands (float).
    Operators are limited to +, -, *, /, ^.
    """
    if node is None:
        return 0.0

    # If this is a leaf node, assume it's a number
    if node.left is None and node.right is None:
        try:
            return float(node.data)
        except ValueError as e:
            raise ValueError(
                f"Cannot convert operand '{node.data}' to float."
            ) from e

    # Recursively evaluate subtrees
    left_val = evaluate_tree(node.left)
    right_val = evaluate_tree(node.right)

    # Apply the operator at the current node
    if node.data == "+":
        return left_val + right_val
    elif node.data == "-":
        return left_val - right_val
    elif node.data == "*":
        return left_val * right_val
    elif node.data == "/":
        if right_val == 0.0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return left_val / right_val
    elif node.data == "^":
        return left_val**right_val
    else:
        # If we get here, the operator is not recognized
        raise ValueError(f"Unknown operator '{node.data}'.")


def print_tree(node, level=0):
    """
    Print the binary tree in a sideways (horizontal) style.

    :param node:  Current node.
    :param level: Current depth level in the tree (used for indentation).
    """
    if node is None:
        return

    # First, print the right subtree (at a deeper level)
    print_tree(node.right, level + 1)

    # Print current node
    indent = "  " * level  # You can tweak spacing here
    print(f"{indent}{node.data}")

    # Finally, print the left subtree
    print_tree(node.left, level + 1)


#
# Main program entry
#


def main():
    """main"""
    expr_type = (
        input("Enter the type of expression (infix/prefix/postfix): ")
        .strip()
        .lower()
    )
    expression = input(
        "Enter the expression (tokens separated by spaces): "
    ).strip()
    # Add spaces around operators
    expression = add_spaces_around_operators_regex(expression)
    # get list of words, split by whitespace
    tokens = expression.split()

    # Build tree according to type
    if expr_type == "infix":
        root = build_tree_from_infix(tokens)
    elif expr_type == "prefix":
        root = build_tree_from_prefix(iter(tokens))
    elif expr_type == "postfix":
        root = build_tree_from_postfix(tokens)
    else:
        print("Invalid type of expression")
        return

    # Print the tree
    print("\nExpression Tree:")
    print_tree(root)

    # Now print the other two forms
    prefix_expr = tree_to_prefix(root)
    infix_expr = tree_to_infix(root)
    postfix_expr = tree_to_postfix(root)

    print("Prefix  :", prefix_expr)
    print("Infix   :", infix_expr)
    print("Postfix :", postfix_expr)

    # Evaluate
    print("Result  :", evaluate_tree(root))


if __name__ == "__main__":
    main()
