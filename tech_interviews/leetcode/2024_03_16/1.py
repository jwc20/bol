def check(nums, queries, limit):
    prefix = [nums[0]]
    result = []

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    for x, y in queries:
        subarray_sum = prefix[y] - prefix[x] + nums[x]
        result.append(subarray_sum < limit)

    return result


if __name__ == "__main__":
    nums = [1, 2, 2, 4]
    queries = [(0, 1), (1, 2), (0, 3)]
    limit = 4
    check(nums, queries, limit)
    # => [True, False, False]

    print(check(nums, queries, limit))

    nums1 = [1, 6, 3, 2, 7, 2]
    queries1 = [(0, 3), (2, 5), (2, 4)]
    limit1 = 13
    check(nums1, queries1, limit1)
    # => [True, False, True]

    print(check(nums1, queries1, limit1))
