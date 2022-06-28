from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    '''
    res = [[1]]

    if n == 0:
        return []

    for i in range(n - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    return res
'''
    result = [[1], [1, 1]]

    if n == 1:
        return result[0:1]
    if n == 2:
        return result
    if n <= 0:
        return []

    index = 2

    while index < n:
        new_row = [1]
        print(len(result[-1]))
        for i in range(1, len(result[-1])):
            new_row.append(result[-1][i - 1] + result[-1][i])
        # print(new_row)
        new_row.append(1)
        result.append(new_row)
        index += 1
    return result





if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "pascal_triangle.py", "pascal_triangle.tsv", generate_pascal_triangle
        )
    )
