"""Merge two sorted lists into a single sorted list.

Complete `merge(x, y)` below and run `pytest` to check your solution.
"""


def merge(x: list[int], y: list[int]) -> list[int]:
    """Return a new sorted list containing all elements from sorted lists x and y."""
    pass


def test_basic_interleaved():
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]


def test_different_lengths():
    assert merge([1, 5], [2, 3, 4, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert merge([1, 2, 3, 6, 7], [4, 5]) == [1, 2, 3, 4, 5, 6, 7]


def test_non_overlapping():
    assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]


def test_empty_lists():
    assert merge([], []) == []
    assert merge([], [1, 2, 3]) == [1, 2, 3]
    assert merge([1, 2, 3], []) == [1, 2, 3]


def test_single_elements():
    assert merge([1], [2]) == [1, 2]
    assert merge([2], [1]) == [1, 2]
    assert merge([5], [5]) == [5, 5]


def test_duplicates():
    assert merge([1, 2, 2, 5], [2, 3, 5, 5]) == [1, 2, 2, 2, 3, 5, 5, 5]
    assert merge([0, 0, 0], [0, 0]) == [0, 0, 0, 0, 0]


def test_negative_numbers_and_zero():
    assert merge([-10, -3, 0, 4], [-5, -3, 1, 2]) == [-10, -5, -3, -3, 0, 1, 2, 4]
    assert merge([-100, -10, -1], [-90, -2, 0]) == [-100, -90, -10, -2, -1, 0]
