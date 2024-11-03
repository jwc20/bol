import unittest
from typing import List


"""
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


["eat","tea","tan","ate","nat","bat"]
   l     r

result = []

anagrams = []

- check anagrams for strs[0] = "eat"
    - check "tea"
        - append to anagrams ["eat", "tea"]
        - remove "tea" from strs
    - move on to the next item in strs


    check "tan"
        - "tan" is not an anagram for eat
        - move to next item

    check "ate"
        - append to anagrams ["eat", "tea", "ate"]
        - remove "ate" from strs
    - move on to the next item in strs


anagrams = ["eat", "tea", "ate"]
strs = ["tan", "nat", "bat"]


result [["eat", "tea", "ate"]]



=> This approach wil take 
5 + 4 + 3 + 2 + 1  iterations which O( (n(n+1)) / 2 ) == O(n^2) Time



=> also considering the alg for check for anagrams it will take O(n^2 * s)

--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------

algorithm for checking anagrams

- use dictionary 
    => O( length of the strs[i] ) === O(s) time, where s is the length of the string in the list
    => O(s) space


--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------

["eat","tea","tan","ate","nat","bat"]
   l     r
         l     r  
         l           r  
                     l     r  
                     l           r  




# this approach will send to the back of strs if it IS an anagram

["eat","tea","tan","ate","nat","bat"]
   l     m                       r



["eat","bat","tan","ate","nat","tea"]
   l     m                 r
   l           m           r
   l                 m     r


["eat","bat","tan","nat","ate","tea"]
   l                 m     r               when m < r, then swap the items in l and m and set l=0 and m=0 and r -= 2



["nat","bat","tan","eat","ate","tea"]
   l     m     r

["bat","nat","tan","eat","ate","tea"]
   l     m     r




=> Not too sure on the space complexity 
could be something like O(n * s)

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        l, m, r = 0, 1, len(strs) - 1

        if len(strs) == 0: return results
        if len(strs) == 1: return [[strs[0]]]
        if len(strs) == 2 and self.isAnagrams(strs[0], strs[1]): 
            return [[strs[0], strs[1]]]

        if len(strs) == 2 and self.isAnagrams(strs[0], strs[1] == False): 
            return [[strs[0]], [strs[1]]]



        anagrams = []
        while l < r:
            if self.isAnagrams(strs[l], strs[m]) == True:
                anagrams.append(strs[m])
                strs[m], strs[r] = strs[r], strs[m]

                if r == m + 1:
                    anagrams.append(strs[l])
                    results.append(anagrams)
                    anagrams = []
                    strs[l], strs[m] = strs[m], strs[l]
                    m = l + 1
                    r -= 2
                    # print(strs, results, anagrams, l, m ,r)

                else:
                    print(strs, results, anagrams, l, m, r)
                    r -= 1

            if self.isAnagrams(strs[l], strs[m]) == False:
                if r == m + 1 and m == l + 1 and r == l + 2:
                    strs[l], strs[m] = strs[m], strs[l]

                    if self.isAnagrams(strs[m], strs[r]):
                        anagrams.append(strs[l])
                        results.append(anagrams)
                        anagrams = []

                        anagrams.append(strs[m])
                        anagrams.append(strs[r])
                        results.append(anagrams)
                        print(results, anagrams, l, m, r)
                        return results
                m += 1

        # print(results)
        # return results

    def isAnagrams(self, s1, s2):

        if len(s1) != len(s2):
            return False

        d = {}
        # d = defaultdict()

        for i in range(len(s1)):
            if s1[i] not in d:
                d[s1[i]] = 1
            else:
                d[s1[i]] += 1

        for c in s2:
            if c in d:
                d[c] -= 1
            else:
                return False

        return all(count == 0 for count in d.values())


# print(Solution().isAnagrams('abc', 'cba'))
# print(Solution().isAnagrams('abs', 'cba'))


## - Test Cases: --------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------
## ----------------------------------------------------------------------------------------------------------


def sort_nested_lists(result: List[List[str]]) -> List[List[str]]:
    """Helper function to sort nested lists for comparison"""
    return sorted([sorted(inner_list) for inner_list in result])


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertNestedListEqual(self, list1, list2):
        """Helper method to compare nested lists regardless of order"""
        self.assertEqual(sort_nested_lists(list1), sort_nested_lists(list2))

    def test_example1(self):
        """Test case 1: Basic example with multiple anagram groups
        Input: ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        """
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_example2(self):
        """Test case 2: Single empty string
        Input: [""]
        Output: [[""]]
        """
        strs = [""]
        expected = [[""]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_example3(self):
        """Test case 3: Single character
        Input: ["a"]
        Output: [["a"]]
        """
        strs = ["a"]
        expected = [["a"]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_empty_list(self):
        """Test case 4: Empty input list
        Input: []
        Output: []
        """
        strs = []
        expected = []
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_no_anagrams(self):
        """Test case 5: No anagrams in the list
        Input: ["cat", "dog", "pig"]
        Output: [["cat"], ["dog"], ["pig"]]
        """
        strs = ["cat", "dog", "pig"]
        expected = [["cat"], ["dog"], ["pig"]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_all_anagrams(self):
        """Test case 6: All strings are anagrams
        Input: ["abc", "bca", "cab", "acb"]
        Output: [["abc", "bca", "cab", "acb"]]
        """
        strs = ["abc", "bca", "cab", "acb"]
        expected = [["abc", "bca", "cab", "acb"]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_case_sensitive(self):
        """Test case 7: Case sensitive strings
        Input: ["Abc", "bca", "CAB"]
        Output: [["Abc"], ["bca"], ["CAB"]]
        """
        strs = ["Abc", "bca", "CAB"]
        expected = [["Abc"], ["bca"], ["CAB"]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_with_spaces(self):
        """Test case 8: Strings with spaces
        Input: ["a bc", "b ca", "cab "]
        Output: [["a bc"], ["b ca"], ["cab "]]
        """
        strs = ["a bc", "b ca", "cab "]
        expected = [["a bc"], ["b ca"], ["cab "]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_multiple_empty_strings(self):
        """Test case 9: Multiple empty strings
        Input: ["", "", ""]
        Output: [["", "", ""]]
        """
        strs = ["", "", ""]
        expected = [["", "", ""]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_repeated_words(self):
        """Test case 10: Repeated words
        Input: ["cat", "cat", "cat"]
        Output: [["cat", "cat", "cat"]]
        """
        strs = ["cat", "cat", "cat"]
        expected = [["cat", "cat", "cat"]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_mixed_lengths(self):
        """Test case 11: Strings of different lengths
        Input: ["a", "ab", "abc", "abcd"]
        Output: [["a"], ["ab"], ["abc"], ["abcd"]]
        """
        strs = ["a", "ab", "abc", "abcd"]
        expected = [["a"], ["ab"], ["abc"], ["abcd"]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_special_characters(self):
        """Test case 12: Special characters
        Input: ["!@#", "@#!", "#@!"]
        Output: [["!@#", "@#!", "#@!"]]
        """
        strs = ["!@#", "@#!", "#@!"]
        expected = [["!@#", "@#!", "#@!"]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_numbers(self):
        """Test case 13: Strings with numbers
        Input: ["1a2", "a12", "21a"]
        Output: [["1a2", "a12", "21a"]]
        """
        strs = ["1a2", "a12", "21a"]
        expected = [["1a2", "a12", "21a"]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)

    def test_large_groups(self):
        """Test case 14: Large anagram groups
        Input: ["abc", "bca", "cab", "def", "efd", "fed"]
        Output: [["abc", "bca", "cab"], ["def", "efd", "fed"]]
        """
        strs = ["abc", "bca", "cab", "def", "efd", "fed"]
        expected = [["abc", "bca", "cab"], ["def", "efd", "fed"]]
        self.assertNestedListEqual(self.solution.groupAnagrams(strs), expected)


if __name__ == "__main__":
    unittest.main()
