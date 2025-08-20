"""
- The brute force is to use multiple loops and check each items with all others

- This will take O(n^2) time and O(1) space
    - summation of i to n where n is the number of items in the list 

I am assuming that the input list is not sorted.
being sorted make things easier. 

sorting the list => O(n log n) time and O(1) space.

- Another appraoch would be to use a hashmap, where we iterate through the list and keep count for each items. 
- after iterating we can check the values in the hashmap if there are values that are greater than 1.
- This approach will take O(n) time and space.


- Another approach would be to use two pointers and check if the items at the pointers are the same, if yes, then we return False.
=> O(n) time and O(1) space

        1,2,3,1
        l r             l!=r
        l   r             l!=r
        l     r             l=r



        1,2,3,4
        l r             l!=r
        l   r             l!=r
        l     r             l!=r            oh no!


We have to sort the list before iterating since the above demonstration requires a double loop to implement => O(n^2)

"""

from typing import List

from collections import defaultdict


class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     nums.sort()

    #     for i in range(len(nums) - 1):
    #         if nums[i] == nums[i+1]:
    #             return True
    #     return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict()

        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                return True

        return False


input1 = [1, 2, 3, 1]
input2 = [1, 2, 3, 4]


print(Solution().containsDuplicate(input1))
print(Solution().containsDuplicate(input2))
