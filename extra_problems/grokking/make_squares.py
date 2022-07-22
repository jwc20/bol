# first solution
def make_squares(A):
    l, r = 0, len(A) - 1

    if all(n < 0 for n in A):
        return [A[i] ** 2 for i in reversed(range(len(A)))]

    while l < r:
        print(A[l], A[r], A)
        # if A[l] == 0 and A[r] == 0:
        if A[l] == 0:
            l += 1
        # if (A[l] ** 2) > (A[r] ** 2):
        elif abs(A[l]) > abs(A[r]):
            A[l], A[r] = A[r], A[l] ** 2
            r -= 1
        elif (A[l] ** 2) <= (A[r] ** 2):
            A[r] = A[r] ** 2
            r -= 1
    return A


def make_squares1(A):
    # print(all(n<0 for n in A))
    start = 0
    if all(n < 0 for n in A):
        return [A[i] ** 2 for i in reversed(range(len(A)))]
    for i in reversed(range(len(A))):
        # print(A)
        # print(i, A[i], A[start], A)
        if A[start] == 0 and A[i] == 0:
            start += 1
        elif A[i] ** 2 < A[start] ** 2:
            A[start], A[i] = A[i], A[start] ** 2
        elif (A[start] ** 2) <= (A[i] ** 2):
            A[i] = A[i] ** 2
    return A


# Solution from leetcode
def make_squares2(A):
    result = [None for _ in A]
    left, right = 0, len(A) - 1
    for index in reversed(range(len(A))):
        if abs(A[left]) > abs(A[right]):
            result[index] = A[left] ** 2
            left += 1
        else:
            result[index] = A[right] ** 2
            right -= 1
    return result


# print(make_squares2([-2, -1, 0, 2, 3]))
# print(make_squares2([-3, -1, 0, 1, 2]))
# print(make_squares2([-5,-4,-3,-2,-1]))
# print(make_squares2([-7,-3,2,3,11]))
print(make_squares2([-10000, -9999, -7, -5, 0, 0, 10000]))
