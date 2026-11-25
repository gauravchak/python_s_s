"""Merge two lists into a single interleaved list.

Complete `merge(x, y)` below and run `pytest` to check your solution.
"""
from typing import List


def merge(x: List[int], y: List[int]) -> List[int]:
    """Return a new list containing all elements from lists x and y."""
    sll = 0  # smaller_list_len
    if len(x) < len(y):
        sll = len(x)
    else:
        sll = len(y)
    print('n = ',sll)
    F = []
    for i in range(sll):
        F.append(x[i])
        F.append(y[i])
    if len(x) > sll:
        for i in range(sll, len(x)):
            F.append(x[i])
    elif len(y) > sll:
        for i in range(sll, len(y)):
            F.append(y[i])
    return F

# x = merge([1, 2, 3, 6, 7], [4, 5, -1])
# print(x)

def test_basic_interleaved():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([2, 4, 6], [1, 3, 5]) == [2, 1, 4, 3, 6, 5]


def test_different_lengths():
    assert merge([1, 5], [2, 3, 4, 6, 7]) == [1, 2, 5, 3, 4, 6, 7]
    assert merge([1, 2, 3, 6, 7], [4, 5]) == [1, 4, 2, 5, 3, 6, 7]


def test_empty_lists():
    assert merge([], []) == []
    assert merge([], [1, 2, 3]) == [1, 2, 3]
    assert merge([1, 2, 3], []) == [1, 2, 3]


def test_single_elements():
    assert merge([1], [2]) == [1, 2]
    assert merge([2], [1]) == [2, 1]
    assert merge([5], [5]) == [5, 5]


