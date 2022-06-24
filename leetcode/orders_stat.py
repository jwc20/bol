def order_stat(A: list) -> int:

    l = 0
    c = 0

    while c < len(A):
        print(l, A[l], "; ", c, A[c])
        if A[c] < A[l]:
            l = c
            c += 1
        if A[c] >= A[l]:
            c += 1

    return A[l]


A = [3, 2, 5, 0, 1, 2]

print(order_stat(A))
