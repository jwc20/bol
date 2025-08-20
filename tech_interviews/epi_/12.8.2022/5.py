"""
    in: A list of lists containing integers. [[1,2,3],[4,5,6],[7,8,9]]
    out: A list of integer

    We have to take a list of list of integers and return a list with elements in spiral order.
    
    [[1,2,3],
     [4,5,6],
     [7,8,9]] => [1,2,3,6,9,8,7,4,5]

    Need to keep track of n.

     Explanation: 
        - Append all of first row (first array) until it reaches the end.
        - Append the last elements of the remaining rows until the last row.
        - Append the remaining elements in the last row in reversed order.
        - Append the remaining rows first elements before reaching the first row.
        - Append the remaing elements in the row before the end.
        - ... 

    Need to approach this recursively?

    Moving through the matrix:
        - n times to East

        - n-1 times to South 
        - n-1 times to West 

        - n-2 times to North
        - n-2 times to East

    
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10,11,12],
     [13,14,15,16]] => [1,2,3,4,8,12,15,14,13,9,5,6,7,11,10]

    Moving through the matrix:
        - n times to East

        - n-1 times to South 
        - n-1 times to West 

        - n-2 times to North
        - n-2 times to East

        - n-3 times to South
        - n-3 times to West

        - n-4 times to North
        - n-4 times to East

    This will take O(n) time and space.


    # Corrections
        - Above method lacks uniformity, it makes it hard to code.
        - First add n-1 elements in the first **row**.
        - Then add the first n-1 elements of the last **column**.
        - Then add the last n-1 elements of the last row in reversed order.
        - Finally add the last n-1 elements of the first column in reversed order.
        
        - The soluton traverses the matrix in right -> down -> left -> up -> right -> ... direction. 
        - Change directions if the array is out of bounds or visited before. 
"""

from typing import List


def func(square_matrix: List[List[int]]) -> List[int]:

    shift = ((0, 1), (1, 0), (0, -1), (-1, 0))          # (up, right, down, left)
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
            direction = (direction + 1) & 3             # Why 3? Since there are 4 shifts set above, we are choosing among 0-3.
            next_x = x + shift[direction][0]
            next_y = y + shift[direction][1]

        x, y = next_x, next_y

    return spiral_ordering


# def func(M: List[List[int]]) -> List[int]:
#     result = []
#     n = len(M)
#     # first row, East
#     for i in range(n):
#         result.append(M[0][i])
#     # South
#     for i in range(1, n):
#         result.append(M[i][n - 1])
#     # last row, West
#     for i in reversed(range(0, n - 1)):
#         result.append(M[n - 1][i])
#     return result


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(func(matrix))
