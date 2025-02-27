"""Module with functions that divides array and count result"""

import multiprocessing as mp
import os
from typing import List


def divide_array(arr_to_divide: List) -> List:
    """Splits the array into chunks based on the number of CPU cores."""
    parts = os.cpu_count() or 2  # Ensure at least 2 parts
    arr_len = len(arr_to_divide)
    part_len = arr_len // parts  # Integer division
    divided_arrays = []

    for i in range(parts):
        start = i * part_len
        stop = (
                       i + 1) * part_len if i != parts - 1 else arr_len
        # Last chunk gets remainder
        divided_arrays.append(arr_to_divide[start:stop])

    return divided_arrays


def get_sum_array(array_inp: List) -> int:
    """Computes the sum of an array and puts the result in a queue."""
    return sum(array_inp)


def get_count_arrays_parts(array_inp: List) -> int:
    """Computes the number of arrays divided by the number of CPU cores."""
    arrays = divide_array(array_inp)
    with mp.Pool() as pool:
        results = pool.map(get_sum_array, arrays)

    for res in results:
        print(res)

    return sum(results)


if __name__ == '__main__':
    arr = list(range(1011000))

    result = get_count_arrays_parts(arr)
    print(f"Sum of array: {result}")
