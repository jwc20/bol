def sq_sorted(arr):
    h = len(arr) - 1
    l, r = 0, len(arr) - 1 
    s = [0 for x in range(len(arr))]

    while l <= r:
        l_sq = arr[l] * arr[l]
        r_sq = arr[r] * arr[r]

        if l_sq < r_sq:
            s[h] = r_sq
            r -= 1
        else:
            s[h] = l_sq
            l += 1 
        h -= 1

    return s


print(sq_sorted([-2, -1, 0, 2, 3]))
print(sq_sorted([-3, -1, 0, 1, 2]))
