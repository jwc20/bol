from typing import List


def fun(n: int) -> List[List[int]]:
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


print(fun(3))
print(fun(4))
print(fun(5))
print(fun(-1))
print(fun(1))
print(fun(2))
