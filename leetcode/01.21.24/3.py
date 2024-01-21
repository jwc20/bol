"""
https://leetcode.com/problems/move-zeroes/
"""


from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        We use two pointers and start the pointers at each ends of the strings.
        if the character the left pointer is 0 then we swap places with the right pointer and
        increment, decrement the left and right pointer respectively.

        if the character at the lefte pointer is not 0 then just increment.
        """
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                continue
            nums[l] = nums[r]
            l += 1

        while l < len(nums):
            nums[l] = 0
            l += 1

        print(l, nums)


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    sol1 = Solution().moveZeroes(nums)
