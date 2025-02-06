"""Module with actions with matrix. Run tests with this command:
python test_matrix_8.py"""

from typing import List
import doctest


def matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> \
        List[List[int]]:
    """
    Multiply two matrices.

    Matrix multiplication is only possible if the number of columns in the
    first matrix
    is equal to the number of rows in the second matrix.

    Example:
    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]

    A more complex example:
    >>> matrix_multiply([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]])
    [[14, 32], [32, 77]]

    Raises:
    ValueError: If the number of columns in the first matrix does not equal
    the number of rows in the second matrix.
    """
    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "The number of columns in the first matrix must equal the number "
            "of rows in the second matrix.")

    # Matrix multiplication logic
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)]
              for row in matrix1]
    return result


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Transpose a matrix.

    Transposition means converting rows of the matrix into columns.

    Example:
    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]

    A more complex case:
    >>> transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    # Transpose using zip and list conversion
    return list(map(list, zip(*matrix)))


def run_doctests():
    """
    Run doctest to validate the examples in the function docstrings.
    """
    result = doctest.testmod()
    if result.failed == 0:
        print("All tests passed successfully!")
    else:
        print(f"{result.failed} test(s) failed.")


if __name__ == "__main__":
    run_doctests()
