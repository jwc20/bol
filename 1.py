from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [i, d[complement]]
            d[nums[i]] = i
        return []



print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2,4], 6))
print(Solution().twoSum([3,3], 6))
print(Solution().twoSum([3,4], 6))
