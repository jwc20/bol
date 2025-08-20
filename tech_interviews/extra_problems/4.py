def partition(A, k):
    """
    0, 1, 2, 3, 2, 1
    l,c            g
       l,c         g (l++, c++)
          l,c      g (c++)

    0, 1, 2, 3, 2, 1
          l  c     g (A[c] swap A[g], g--)          

    0, 1, 2, 1, 2, 3
          l  c  g    (A[c] swap A[l], l++, c++)

    0, 1, 1, 2, 2, 3
             l  c,g

    """
    less,current, greater = 0, 0,  len(A)

    while current < greater:
        print(A)
        print(less, current, greater)
        if A[current] < k:
            A[current], A[less] = A[less], A[current]
            less, current = less + 1, current + 1

        elif A[current] > k:
            greater -= 1
            A[current], A[greater] = A[greater], A[current]

        else:  # A[current] = k
            current += 1

    return A


l1 = [0, 1, 2, 3, 2, 1, 3, 2, 1, 0, 1, 2, 2]
l2 = [0, 1, 2, 3, 0, 1]
k1 = 2

l3 = [0, 1, 2, 3, 4, 0, 1, 3, 2]
# print(partition(l1, k1))
# print(partition(l2, k1))
print(partition(l3, k1))

# => [0,0,1,1,1,1,2,2,2,2,3,3]
