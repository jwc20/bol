from typing import List


def f(A: List[str], s: str) -> List[str]:
    # result = []

    # for item in A:
    #     if s in item:
    #         result.append(item)

    # return result

    left, curr = 0, 0
    while curr < len(A):
        if s in A[curr]:
            A[left], A[curr] = A[curr], A[left]
            left += 1
            curr += 1

        else:
            curr += 1

    return A[:left]


print(f(["dog", "dark", "cat", "door", "dodge"], "do"))
print(f(["aaab", "baaa", "a", "aa", "babab", "sfasdfasdf", "123", "aaaaaaaaaa"], "aaa"))
