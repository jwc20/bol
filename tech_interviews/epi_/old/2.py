from typing import List


def fun(D: List[int]) -> List[int]:
    D[-1] += 1
    for i in reversed(range(1, len(D))):
        if D[i] != 10:
            break
        D[i] = 0
        D[i - 1] += 1
    else:
        if D[0] == 10:
            D[0] = 1
            D.append(0)
    return D


print(fun([1, 2, 9]))
print(fun([1, 1, 9, 9]))
print(fun([1, 3, 2, 9]))
print(fun([9, 9]))
print(fun([9, 9, 9]))
