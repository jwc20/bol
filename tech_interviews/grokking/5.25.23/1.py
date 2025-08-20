def sq_sorted_array(nums):

    h = len(nums) - 1
    squared = [0 for x in range(len(nums))]
    l, r = 0, len(nums) - 1

    while l <= r:
        lsq = nums[l] * nums[l]
        rsq = nums[r] * nums[r]

        if lsq > rsq:
            squared[h] = lsq
            l += 1
        else:
            squared[h] = rsq
            r -= 1
        h -= 1

    return squared


print(sq_sorted_array([-2, -1, 0, 2, 3]))
print(sq_sorted_array([-3, -1, 0, 1, 2]))
