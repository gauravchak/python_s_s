# Contents of tests/test_prime.py

import pytest
from src.prime import is_prime


def test_prime_positive():
    assert is_prime(2)
    assert is_prime(3)
    assert is_prime(5)
    assert is_prime(7)
    assert is_prime(11)
    assert is_prime(13)
    assert is_prime(17)
    assert is_prime(19)
    assert is_prime(23)
    assert is_prime(29)
    assert is_prime(97)


def test_prime_negative():
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(6)
    assert not is_prime(8)
    assert not is_prime(9)
    assert not is_prime(10)
    assert not is_prime(12)
    assert not is_prime(14)
    assert not is_prime(15)
    assert not is_prime(16)
    assert not is_prime(25)
    assert not is_prime(100)


def test_prime_zero_and_negative():
    assert not is_prime(0)
    assert not is_prime(-1)
    assert not is_prime(-2)
    assert not is_prime(-10)


def test_large_prime():
    assert is_prime(7919)
    assert is_prime(104729)
    assert not is_prime(7920)
