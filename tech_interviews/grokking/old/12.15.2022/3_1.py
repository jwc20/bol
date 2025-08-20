from typing import List


def countIslandsDFS(matrix: List[List[int]]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    total_islands = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                total_islands += 1
                visitIslandDFS(matrix, i, j)

    return total_islands


def visitIslandDFS(matrix: List[List[int]], x: int, y: int) -> None:
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return  # not a valid cell
    if matrix[x][y] == 0:
        return  # it's a water cell

    matrix[x][y] = 0

    # recursively visit all neighboring cells
    visitIslandDFS(matrix, x + 1, y)  # lower cell
    visitIslandDFS(matrix, x - 1, y)  # upper cell
    visitIslandDFS(matrix, x, y + 1)  # right cell
    visitIslandDFS(matrix, x, y - 1)  # left cell


print(
    countIslandsDFS(
        [
            [0, 1, 1, 1, 0],
            [0, 0, 0, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )
)  # => 1
print(
    countIslandsDFS(
        [
            [1, 1, 1, 0, 0],
            [0, 1, 0, 0, 1],
            [0, 0, 1, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ]
    )
)  # => 3
