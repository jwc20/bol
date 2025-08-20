"""

input: 
    - nums1, nums2 arrays that are in increasing order
    - m, n integers

output: merged array that is sorted

** Note that we are storing the result to nums1


- The naive method would be to combine the two array by using in-built python function and sort afterwards. 
- ([1,2,3] + [6,7,1] in python gives us [1,2,3,6,7,1])
- The sorting will give us O(n log n) time


- A better approach would be to iterate backwards from both arrays from the m and n positions.
- we keep an position value for nums to insert from either nums1 or nums2 called 'last'

    - if the value from nums1 is greater, then insert nums1[last] = nums1[m] and m--
    - else, then insert to nums1[last] = nums2[n] and n--

- if either m or n is less than or equal to 0, then we break the loop.

[1 2 3 0 0 0]; [2 5 6]
     m              n             m < n => [1 2 3 0 0 6], n-- ; last=5
     m            n               m < n => [1 2 3 0 5 6], n-- ; last=4
     m          n                 m > n => [1 2 3 3 5 6], m-- ; last=3
   m            n                 m = n => [1 2 2 3 5 6], m-- ; last=2
 m              n                 m < n => [1 2 2 3 5 6], n-- ; last=1

since the smallest element in nums1 is smaller than the smallest element in nums2, we dont have to do anything. 

-----------------------------

- now there could be cases where one or more element for nums2 are smaller than the smallest element in nums1.

[2 2 3 0 0 0]; [1 5 6]
     m              n             m < n => [2 2 3 0 0 6], n-- ; last=5 
     m            n               m < n => [2 2 3 0 5 6], n-- ; last=4
     m          n                 m > n => [2 2 3 3 5 6], m-- ; last=3
   m            n                 m > n => [2 2 2 3 5 6], m-- ; last=2
 m              n                 m > n => [2 2 2 3 5 6], m-- ; last=1, and break loop

- since the remaining value for nums2 is less than the smallest element in nums1, we add the remaining the elements of nums2 to nums1.

=> [1 2 2 3 5 6]

"""


from typing import List
import unittest


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1

            last -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            n, last = n - 1, last - 1


class TestMergeFunction(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_example_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_example_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_nums2_smaller_than_nums1(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_nums1_empty(self):
        nums1 = [0, 0, 0]
        m = 0
        nums2 = [1, 2, 3]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])

    def test_nums2_empty(self):
        nums1 = [1, 2, 3]
        m = 3
        nums2 = []
        n = 0
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])

    def test_all_elements_same(self):
        nums1 = [1, 1, 1, 0, 0, 0]
        m = 3
        nums2 = [1, 1, 1]
        n = 3
        self.solution.merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 1, 1, 1, 1, 1])


if __name__ == "__main__":
    unittest.main()
