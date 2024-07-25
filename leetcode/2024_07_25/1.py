"""
https://leetcode.com/problems/sort-an-array/description/?envType=daily-question&envId=2024-07-25


912. Sort an Array
Medium

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""


import math
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        create a variable for max elem in nums.
        use two pointers.
        => O(n), O(1)
        """
        l, r = 0, len(nums)-1
        _max = -math.inf

        while l < r:
            if nums[l] > nums[r] and nums[r] > _max :
                nums[l], nums[r] = nums[r], nums[l]
                _max = nums[r]
                r -= 1

            elif nums[l] > nums[r] and nums[r] <= _max :
                nums[l], nums[r] = nums[r], nums[l]

            l += 1


        return nums
        
print(Solution().sortArray([5,1,1,2,0,0]))
print(Solution().sortArray([5,2,3,1]))
print(Solution().sortArray([-2,3,-5]))
