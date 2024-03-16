from typing import List


def left_section_is_greater_than_right_section(nums):
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    ans = 0

    for j in range(len(prefix) - 1):
        left_section = prefix[j]
        right_section = prefix[-1] - prefix[j]

        if left_section > right_section:
            ans += 1

    return ans


def waysToSplitArray(nums: List[int]) -> int:
    ans = left_section = 0
    total = sum(nums)

    for i in range(len(nums) - 1):
        left_section += nums[i]
        right_section = total - left_section
        if left_section >= right_section:
            ans += 1

    return ans


if __name__ == "__main__":
    nums = [2, 3, 1, 5, 2, 1, 4]
    print(left_section_is_greater_than_right_section(nums))
    print(waysToSplitArray(nums))

    nums1 = [10, 4, -8, 7]
    print(left_section_is_greater_than_right_section(nums1))
    print(waysToSplitArray(nums1))
