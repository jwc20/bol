def find_subsets(nums):
    subsets = []
    subsets.append([])
    #nums.sort(key=lambda x: x)
    list.sort(nums)


    for i in range(len(nums)):
        if nums[i] == nums[i-1]:
            continue

        for j in range(len(subsets)):
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)

    return subsets



s = [1, 3,3]
print(find_subsets(s))
