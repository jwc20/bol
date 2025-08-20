
from typing import List
"""
https://leetcode.com/problems/sort-array-by-increasing-frequency/description/?envType=daily-question&envId=2024-07-23

1636. Sort Array by Increasing Frequency
Easy


Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:
p
Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""
from collections import deque

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        """
        we use hashmap to store the items in nums as key and the 'freq' frequency of the items as value.
        we can return the list keys in the hashmap 'freq' times sorted.

        this will take O(n) space and O(n log(n)) time when n is the length of nums.
        """

        d = {}

        result = deque()

        ## iterate through nums and get the freq.
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1

        last_key = nums[0]
        last_value = d[nums[0]]
        print(last_key, last_value)
        
        for k, v in sorted(d.items(), key=lambda x:x[1], reverse=False):
            
            if last_key < k and last_value == v:
                for _ in range(v):
                    result.appendleft(k)
   
            for _ in range(v):
                result.append(k)
                
            last_key = k
            last_value = v
    
        return result

print(Solution().frequencySort([1,1,2,2,2,3]))
print(Solution().frequencySort([2,3,1,3,2]))
print(Solution().frequencySort([-1,1,-6,4,5,-6,1,4,1]))
