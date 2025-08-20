"""

input: s and t strings
output: boolean value

- The naive approach would be to sort both strings and compare each values as we iterate through both strings
=> O(n log n) time and O(1) space


- Another approach would be use a hash map 

    - iterate through input s
        - have a dictionary for input s string and keep counts for each characters

    - iterate through input t
        - and check if the current character is in the dictionary
            - if the chracter is in the dictionary, then decrement the count

    => O(n) time and space. where n is the length of both inputs


s = abc
t = bca

- check the length of both inputs

"""


"""

Anagram ; nagaram





"""

import unittest

from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        # s_lower = s.lower()
        # t_lower = t.lower()

        d = defaultdict()

        # load s to dictionary and keep count

        for c in s:
            if c not in d:
                d[c] = 1

            else:
                d[c] += 1

        for c in t:
            if c in d:
                d[c] -= 1

            else:
                return False

        print(d)

        return all(count == 0 for count in d.values())


## - Test Cases: --------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------


class TestAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        """Test case 1: Basic anagram
        s = "anagram"
        t = "nagaram"
        Expected: True
        """
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))

    def test_example2(self):
        """Test case 2: Non-anagram
        s = "rat"
        t = "car"
        Expected: False
        """
        self.assertFalse(self.solution.isAnagram("rat", "car"))

    def test_empty_strings(self):
        """Test case 3: Empty strings
        s = ""
        t = ""
        Expected: True
        """
        self.assertTrue(self.solution.isAnagram("", ""))

    def test_different_lengths(self):
        """Test case 4: Different lengths
        s = "abc"
        t = "abcd"
        Expected: False
        """
        self.assertFalse(self.solution.isAnagram("abc", "abcd"))

    def test_same_characters_different_counts(self):
        """Test case 5: Same characters but different counts
        s = "aaab"
        t = "aaba"
        Expected: True
        """
        self.assertTrue(self.solution.isAnagram("aaab", "aaba"))

    def test_single_character(self):
        """Test case 6: Single character strings
        s = "a"
        t = "a"
        Expected: True
        """
        self.assertTrue(self.solution.isAnagram("a", "a"))

    def test_case_sensitive(self):
        """Test case 7: Case sensitivity
        s = "Anagram"
        t = "nagaram"
        Expected: False
        """
        self.assertFalse(self.solution.isAnagram("Anagram", "nagaram"))

    def test_spaces(self):
        """Test case 8: Strings with spaces
        s = "hello world"
        t = "world hello"
        Expected: True
        """
        self.assertTrue(self.solution.isAnagram("hello world", "world hello"))

    def test_numbers(self):
        """Test case 9: Strings with numbers
        s = "123abc"
        t = "abc123"
        Expected: True
        """
        self.assertTrue(self.solution.isAnagram("123abc", "abc123"))

    def test_special_characters(self):
        """Test case 10: Special characters
        s = "!@#$"
        t = "$#@!"
        Expected: True
        """
        self.assertTrue(self.solution.isAnagram("!@#$", "$#@!"))

    def test_repeated_characters(self):
        """Test case 11: Strings with repeated characters
        s = "aaaaabbbbb"
        t = "ababababab"
        Expected: True
        """
        self.assertTrue(self.solution.isAnagram("aaaaabbbbb", "ababababab"))

    def test_unicode_characters(self):
        """Test case 12: Unicode characters
        s = "über"
        t = "reüb"
        Expected: True
        """
        self.assertTrue(self.solution.isAnagram("über", "reüb"))

    def test_one_empty_string(self):
        """Test case 13: One empty string
        s = "abc"
        t = ""
        Expected: False
        """
        self.assertFalse(self.solution.isAnagram("abc", ""))

    def test_similar_but_different(self):
        """Test case 14: Similar but different strings
        s = "aabbcc"
        t = "aabccc"
        Expected: False
        """
        self.assertFalse(self.solution.isAnagram("aabbcc", "aabccc"))


if __name__ == "__main__":
    unittest.main()
