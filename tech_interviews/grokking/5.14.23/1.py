# Contains Duplicate (easy)

# Given an array of integers, find if the array contains any duplicates.


def contain_duplicate(nums):
    """
    Input: nums= [1, 2, 3, 4]
    Output: false
    Explanation: There are no duplicates in the given array.

    Input: nums= [1, 2, 3, 1]
    Output: true
    Explanation: '1' is repeating.
    """

    d = {}

    for i in range(len(nums)):
        if nums[i] not in d:
            d[nums[i]] = 1

        else:
            d[nums[i]] += 1

    for i in range(1, len(d)):
        if d[i] > 1:
            return False

    return True


if __name__ == "__main__":
    print(contain_duplicate([1, 2, 3, 4]))
    print(contain_duplicate([1, 2, 3, 1]))
