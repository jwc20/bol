from typing import List
import math
from collections import defaultdict

"""

We can use hash map for this problem which will result in O(n^2) time and
O(n) space.

We will take the following approach: 
    - check to see if rows has duplicates,
    - check to see if columns has duplicates, and 
    - check to see if each 3x3 sections of the board has duplicates.

We can check the 3x3 sections by partitioning the 3x3 board as:
  0| 1| 2
0|
1|
2|

The key for the dictionary for the 3x3 section will be (0-2,0-2) and the 
values will be the elements in the matrix.
"""


def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    columns = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    for x in range(9):
        for y in range(9):
            if partial_assignment[x][y] == 0:
                continue
            if (
                partial_assignment[x][y] in rows[x]
                or partial_assignment[x][y] in columns[y]
                or partial_assignment[x][y] in squares[(x // 3, y // 3)]
            ):
                return False

            rows[x].add(partial_assignment[x][y])
            columns[y].add(partial_assignment[x][y])
            squares[(x // 3, y // 3)].add(partial_assignment[x][y])

    return True

    return


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
