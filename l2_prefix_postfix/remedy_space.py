import re


def add_spaces_around_operators_regex(s):
    """
    # Example usage
    input_str = "3+ 4* 5"
    result = add_spaces_around_operators_regex(input_str)
    print(result)  # "3 + 4 * 5"
    """
    # Insert spaces around any +, -, *, /, ^
    s = re.sub(r"([+\-*/^])", r" \1 ", s)
    # Collapse multiple spaces into one
    s = re.sub(r"\s+", " ", s)
    return s.strip()
