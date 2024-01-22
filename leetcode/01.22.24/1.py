"""
https://leetcode.com/problems/valid-palindrome/
"""

import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        use two pointers to check characters from each sides.
        check if they are the same. if yes increment the left pointer and decrement the right pointer.
        If the left and right pointers are next to each other, return true
        if the two characters are not the same, then return false.
        """

        if len(s) <= 1:
            return True
        s = s.lower()
        s = s.translate(str.maketrans("", "", string.punctuation)).replace(" ", "")

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True


if __name__ == "__main__":

    s1 = "race a car"
    sol1 = Solution().isPalindrome(s1)

    s2 = "A man, a plan, a canal: Panama"
    sol2 = Solution().isPalindrome(s2)

    s3 = " "
    sol3 = Solution().isPalindrome(s3)

    print(sol1, sol2, sol3)
