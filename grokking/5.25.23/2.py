def contains_duplicates(nums):
    h = {}

    for i in range(len(nums)):
        if nums[i] not in h:
            h[nums[i]] = 1

        else:
            return True
    return False


print(contains_duplicates([1, 2, 3, 4]))
print(contains_duplicates([1, 2, 3, 1]))
