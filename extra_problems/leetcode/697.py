class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        degree is maximum frequency of one element.
        return the smallest length of array with the max frequency.

        Naive Approach is to use hashmap to use the values in the array list as key and count as value.
        After finding the max frequency, append to the list the value with max frequency and other keys with degree of one. and return the length.
        This will have O(n) time and space.

        6 min
        """
