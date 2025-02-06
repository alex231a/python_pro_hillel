"""Module with tests for class AgeVerifier"""

import pytest
from ageverifier import AgeVerifier


@pytest.mark.parametrize('age', [18, 30, 50, 60, 80, 100, 0, 120])
def test_is_adult(age):
    """Tests for is_adult"""
    if age <= 0:
        pytest.skip(f"Ege {age} is less or equal 0.")
    if age >= 120:
        pytest.skip(f"Ege {age} is more than 120.")
    assert AgeVerifier.is_adult(age)


@pytest.mark.parametrize('age', [17, 15, 10, 5, 3, 1, -5, 120])
def test_is_not_adult(age):
    """Tests for is_not_adult"""
    if age <= 0:
        pytest.skip(f"Ege {age} is less or equal 0.")
    if age >= 120:
        pytest.skip(f"Ege {age} is more than 120.")
    assert not AgeVerifier.is_adult(age)


if __name__ == "__main__":
    pytest.main()
