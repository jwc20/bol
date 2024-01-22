"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Note that the input array is already sorted.

        A naive approach is to use double loop.
            Take a number from the start of the array and take the sum of next items'
            in the array. If the sum of two items equals the target value, then return
            the positions of the two items.

        A better approach would be to use two pointers starting from the left and right
        side of the array.
        We want to check if the sum for each pair is greater, lower, or equal.
        """

        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

            elif numbers[l] + numbers[r] > target:
                r -= 1

            else:
                l += 1
        return []


if __name__ == "__main__":
    n1, t1 = [2, 7, 11, 15], 9
    n2, t2 = [2, 3, 4], 6
    n3, t3 = [-1, 0], -1

    sol1 = Solution().twoSum(n1, t1)
    sol2 = Solution().twoSum(n2, t2)
    sol3 = Solution().twoSum(n3, t3)

    print(sol1, sol2, sol3)
