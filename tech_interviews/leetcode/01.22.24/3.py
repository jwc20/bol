"""
https://leetcode.com/problems/set-mismatch/?envType=daily-question&envId=2024-01-22
"""


from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        A naive approach would be to use double loop.

        We can use hashmap but this will take additional space.

        Another approach would be to use two pointers.
        Note that the problem didnt mention about the input being sorted.
            This could mean that we may have to sort beforehand => O(nlogn)


        We can start two pointers from the left side
        [1,2,2,4]
        l r          nums[l] != nums[r], l+=1, r+=1
          l r       nums[l] == nums[r], the numbers are the same. r+=1
          l    r       nums[l] != nums[r],  return [nums[l], nums[r]]


        After find that two numbers are equal, increment the right pointer, to see another duplicate.
        """

        if len(nums) == 2:
            return [nums[0], nums[0] + 1]

        l, r = 0, 1

        duplicate_number = 0
        # lossed_number = 0

        while r < len(nums) - 1:
            if nums[l] == nums[r]:
                duplicate_number = nums[l]
                r += 1

                if nums[l] != nums[r]:
                    return [duplicate_number, nums[r] - 1]

            else:
                l, r = l + 1, r + 1

        return []


if __name__ == "__main__":

    nums1 = [1, 2, 2, 4]
    nums2 = [1, 1]
    sol1 = Solution().findErrorNums(nums1)
    sol2 = Solution().findErrorNums(nums2)

    print(sol1, sol2)
