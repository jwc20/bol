def find_max(nums, k):

    _max = 0

    for i in range(len(nums) - k + 1):
        _sum = 0
        for j in range(i, i + k):
            _sum += nums[j]
        _max = max(_max, _sum)

    return _max


print(find_max([2, 1, 5, 1, 3, 2], 3))
