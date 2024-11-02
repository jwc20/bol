"""

- The naive approach would be to take each item and get the sum of that item and all other items in the list

- O(n^2) time and O(1) space



Q: is the input list sorted?
-> no



- two pointers

- sort the list => O(n log n) time

- l, r = 0, length(nums)  -1



while l < r
- check if the nums[l] + nums[r] == target
- if the nums[l] + nums[r] sum is greated decrement the right pointer 
- if lesser, then increment the left point


O(n log n) tiem and O(1) space

Input: nums = [2,7,11,15], target = 9

"""


from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = defaultdict()

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in d:
                return [i, d[complement]]

            d[nums[i]] = i

        return []
