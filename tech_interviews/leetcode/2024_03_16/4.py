from typing import List


class Solution:
    """
    def minStartValue(self, nums: List[int]) -> int:

        min_value = 1
        prefix = [min_value]

        for i in range(0, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        print(prefix, min(prefix))

        if min(prefix) > 0:
            return min_value
        else: min_value += 1

        return min_value
    """

    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        total = 0

        for num in nums:
            total += num
            min_val = min(min_val, total)
            print(min_val, total)
        return -min_val + 1


if __name__ == "__main__":
    s1 = Solution()
    print(s1.minStartValue([-3, 2, -3, 4, 2]))
    # print(s1.minStartValue([1, 2]))
    # print(s1.minStartValue([1, -2, -3]))
    # print(s1.minStartValue([1, 2, 3]))
