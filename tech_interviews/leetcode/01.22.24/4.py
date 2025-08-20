"""
https://leetcode.com/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        A naive approach would be to use triple loop => O(n^3).

        [-1,0,1,2,-1,-4]

        The trick of this problem would be to take the item from the left nums[i],
        and take the sum of all the numbers on the right using pointers. nums[l] + nums[r]

        One important step before doing this would be to sort the array. Doing so,
        we can use the two pointers to increment and decrement based on the conditional of the three sum.

        [-1,0,1,2,-1,-4] => O(nlogn)
        [-4,-1,-1,0,1,2]
         i  l         r          -4 + -1 + 2 = -3 < 0, since it is smaller than 0, we increment the left pointer.
         i      l     r
         i        l   r          -4 + 0 + 2 = -2 < 0
         i          l r          -1 < 0, the left pointer reached the right pointer, we move on to the i+1
                                set l = 0, r = len(nums) - 1
            i   l     r           append the the result array.

        after performing the algorithm, we will get:
        time: O(nlogn) + O(n) + O(n)
        space: O(n)
        """
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                _total = a + nums[l] + nums[r]

                if _total < 0:
                    l += 1
                elif _total > 0:
                    r -= 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l, r = l + 1, r - 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result


if __name__ == "__main__":

    nums1 = [-1, 0, 1, 2, -1, -4]
    sol1 = Solution().threeSum(nums1)
    print(sol1)
