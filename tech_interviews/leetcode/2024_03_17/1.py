"""
2090. K Radius Subarray Averages

https://leetcode.com/problems/k-radius-subarray-averages/description/
"""

from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        window_size = 2 * k + 1
        n = len(nums)
        averages = [-1] * n

        if window_size > n:
            return averages

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        print(f"prefix: {prefix}")

        for i in range(k, n - k):
            leftBound, rightBound = i - k, i + k
            print(f"leftBound: {leftBound}, rightBound: {rightBound}")
            subArraySum = prefix[rightBound + 1] - prefix[leftBound]
            print(f"subArraySum: {subArraySum}, prefix[rightBound + 1]: {prefix[rightBound + 1]}, prefix[leftBound]: {prefix[leftBound]}")
            average = subArraySum // window_size
            averages[i] = average

        return averages


if __name__ == "__main__":
    # s = Solution()
    # nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    # k = 2
    # print(s.getAverages(nums, k))
    # # => [-1, -1, 2, 2, 2, 3, 2, -1, -1]

    s1 = Solution()
    nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]
    k = 3
    print(s1.getAverages(nums, k))
    # => [-1, -1, -1, 5, 4, 4, -1, -1, -1]
