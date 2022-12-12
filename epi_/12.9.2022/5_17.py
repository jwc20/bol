from typing import List
import math

"""
- Check if sudoku is valid
- Check that no row, column, or 3x3 subarray contains duplicates

A naive approach would be to use loops to check rows and columns.
- We have to set x=y=0.
- Go row by row (and columns) and check if there exists a duplicate value.
    - if duplicates exists, return false

This approach will take O(n^2) time with no additional space.

Can we do this with O(n) time?
"""


def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_assignment)
    # Check row and column constraints.
    if any(
        has_duplicate([partial_assignment[i][j] for j in range(n)])
        or has_duplicate([partial_assignment[j][i] for j in range(n)])
        for i in range(n)
    ):
        return False

    # Check region constraints.
    region_size = int(math.sqrt(n))

    return all(
        not has_duplicate(
            [
                partial_assignment[a][b]
                for a in range(region_size * I, region_size * (I + 1))
                for b in range(region_size * J, region_size * (J + 1))
            ]
        )
        for I in range(region_size)
        for J in range(region_size)
    )


m1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0, 0],
    [0, 0, 0, 0, 6, 0, 4, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 5],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 3, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 3, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 0],
]


m2 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 5, 9, 8, 0, 2, 1],
    [0, 1, 0, 4, 0, 0, 9, 0, 3],
    [3, 0, 6, 7, 0, 0, 4, 0, 8],
    [8, 2, 0, 1, 5, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 8, 4, 3, 0, 7, 0, 5, 0],
    [6, 9, 0, 0, 0, 0, 2, 0, 0],
    [1, 3, 0, 0, 0, 2, 8, 0, 7],
]


print(is_valid_sudoku(m1))
print(is_valid_sudoku(m2))
