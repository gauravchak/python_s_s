"""Merge two sorted lists into a single sorted list.

Complete `merge(x, y)` below and run `pytest` to check your solution.
"""
from typing import List


def merge(x: List[int], y: List[int]) -> List[int]:
    """Return a new list containing all elements from lists x and y."""
    a = 0
    b = 0
    F = []
    while a < len(x) and b < len(y):
        if x[a] < y[b]:
            F.append(x[a])
            a = a + 1
        else:
            F.append(y[b])
            b = b + 1
    for i in range(a, len(x)):
        F.append(x[i])
    for i in range(b, len(y)):
        F.append(y[i])
    return F

def test_equal_length():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]


def test_different_lengths():
    assert merge([1, 5], [2, 3, 4, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert merge([1, 2, 3, 6, 7], [4, 5]) == [1, 2, 3, 4, 5, 6, 7]


def test_empty_lists():
    assert merge([], []) == []
    assert merge([], [1, 2, 3]) == [1, 2, 3]
    assert merge([1, 2, 3], []) == [1, 2, 3]


def test_single_elements():
    assert merge([1], [2]) == [1, 2]
    assert merge([2], [1]) == [1, 2]
    assert merge([5], [5]) == [5, 5]


