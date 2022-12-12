
from typing import List

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:

    shift = ((0, 1), (1, 0), (0, -1), (-1, 0))          # (up, right, down, left)
    # shift = [[0, 1], [1, 0], [0, -1], [-1, 0]]          # (up, right, down, left)
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix) ** 2):
        spiral_ordering.append(square_matrix[x][y])     # append element at given position to the result
        square_matrix[x][y] = 0                         # set to 0 if visited

        # It goes shifts +1 or -1 in one direction (horizontally or vertically)
        next_x = x + shift[direction][0]
        next_y = y + shift[direction][1]

        # We want to change directions if...
        if (
            next_x not in range(len(square_matrix))     # out of bound in x direction
            or next_y not in range(len(square_matrix))  # out of bound in y direction
            or square_matrix[next_x][next_y] == 0       # visited before
        ):

            # change direction
            direction = (direction + 1) & 3             # Why 3? Since there are 4 shifts set above (up, right, down, left), we are choosing among 0-3.
            next_x = x + shift[direction][0]
            next_y = y + shift[direction][1]

        x, y = next_x, next_y

    return spiral_ordering


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(matrix_in_spiral_order(matrix))

