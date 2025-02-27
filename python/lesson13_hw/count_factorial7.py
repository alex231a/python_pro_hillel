"""Module with functions to count factorial"""
import multiprocessing
from functools import reduce
from typing import List, Tuple, Optional


def partial_factorial(start: int, end: int) -> int:
    """
    Computes the factorial of numbers in the given range [start, end].

    :param start: Starting number of the range.
    :param end: Ending number of the range (inclusive).
    :return: The product of numbers in the range.
    """
    res = 1
    for i in range(start, end + 1):
        res *= i
    return res


def parallel_factorial(num_c: int, num_processes: Optional[int] = None) -> int:
    """
    Computes the factorial of `n` using multiple processes.

    :param num_c: The number for which to compute the factorial.
    :param num_processes: The number of parallel processes (default: CPU
    count).
    :return: The factorial of `num`.
    """
    if num_c in (0, 1):
        return 1

    num_processes = num_processes or multiprocessing.cpu_count()
    step = num_c // num_processes
    ranges: List[Tuple[int, int]] = []

    for i in range(num_processes):
        start = i * step + 1
        end = (i + 1) * step if i < num_processes - 1 else num_c
        ranges.append((start, end))

    with multiprocessing.Pool(processes=num_processes) as pool:
        partial_results = pool.starmap(partial_factorial, ranges)

    return reduce(lambda x, y: x * y, partial_results)


if __name__ == "__main__":
    NUM = 100
    print(f"Computing factorial of {NUM} using multiprocessing...")

    result = parallel_factorial(NUM)

    print(f"Factorial of {NUM} has {len(str(result))} digits.")

    print(f"Factorial of {NUM}:\n{result}")
