from typing import List

from test_framework import generic_test

import collections

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    row = collections.defaultdict(set)
    col = collections.defaultdict(set)
    square = collections.defaultdict(set)

    for r in range(9):
        for c in range(9):
            if partial_assignment[r][c] == 0:
                continue
            if (
                partial_assignment[r][c] in row[r]
                or partial_assignment[r][c] in col[c]
                or partial_assignment[r][c] in square[(r // 3, c // 3)]
            ):
                return False
            row[r].add(partial_assignment[r][c])
            col[c].add(partial_assignment[r][c])
            square[(r // 3, c // 3)].add(partial_assignment[r][c])

    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_sudoku.py", "is_valid_sudoku.tsv", is_valid_sudoku
        )
    )
