"""
- The naive approach would be to loop over the input list twice and calculate the sums to see if it 
matches the target value.
- This will give us O(n^2) time complexity which is not optimal

- Another approach would be to sort the input list and use two pointers.
- This will give us O(n log n) time

- A better approach would be to use hash map for this problem which will give us O(n) linear time and space.
- basically, we create a dictionary (hashmap) that keeps the position and the value of the elements in the array as key and value pairs.
- we iterate through the input list and check if the target value MINUS the current value is already in the hashmap.
    - true => return the positions
    - false => add the element to the hashmap and continue iterating through the list.
"""

from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash = defaultdict()

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash:
                return [hash[diff], i]
            hash[num] = i


if __name__ == "__main__":
    nums1 = [2, 7, 11, 15]
    target1 = 9
    sol1 = Solution().twoSum(nums1, target1)
    # => [0, 1]

    nums2 = [3, 2, 4]
    target2 = 6
    sol2 = Solution().twoSum(nums2, target2)
    # => [1, 2]

    nums3 = [3, 3]
    target3 = 6
    sol3 = Solution().twoSum(nums3, target3)
    # => [0, 1]

    print("sol1:", sol1)
    print("sol2:", sol2)
    print("sol3:", sol3)
