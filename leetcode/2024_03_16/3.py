from typing import List


class Solution:
    def runningSum1(self, nums: List[int]) -> List[int]:  # O(n) time and O(n) space
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])

        return prefix

    def runningSum(self, nums: List[int]) -> List[int]:  # O(n) time and O(1) space
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.runningSum([1, 2, 3, 4]))
    print(s.runningSum([1, 1, 1, 1, 1]))
    print(s.runningSum([3, 1, 2, 10, 1]))

    s1 = Solution()
    print(s1.runningSum1([1, 2, 3, 4]))
    print(s1.runningSum1([1, 1, 1, 1, 1]))
    print(s1.runningSum1([3, 1, 2, 10, 1]))
