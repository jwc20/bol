def triplet_with_smaller_sum(A, t):
    count = 0
    A.sort()

    for i in range(len(A)):
        l, r = i + 1, len(A) - 1
        while l < r:
            curr_sum = A[i] + A[l] + A[r]

            if curr_sum < t:
                count, l = count + r - l, l + 1
            else:
                r -= 1

    return count


print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))
print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
