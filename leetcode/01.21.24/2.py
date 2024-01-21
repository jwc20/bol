"""
https://leetcode.com/problems/merge-strings-alternately/
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        word1 = "abc", 
        word2 = "pqr"

        word1:  a   b   c
        word2:    p   q   r
        merged: a p b q c r

        A naive approach would be to use double loop O(n^2) and append to a new list.
        -> time, space: O(n^2), O(n) where n is the length of the greater input
        
        (alternating inputs from word1 then word2)

        Another approach would be to use two pointers starting from each word1,word2 
        then append to a result list. appending to a dynamic array will cost space, so 
        a better approach would be to create a static array with length already determined (len(word1) + len(word2)).

        We need to have a conditional checking to see first, which word is longer. since then 
        we can alternating appending, then append the rest of the longer word after the shorter word runs out of character.


        - get the length of the words, shorter s, longer l.
        - we will merge the two words by s.
            - then we will append the rest of the words from the longer word. 
        """

        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        return "".join(result)

        
if __name__ == '__main__': 
    word1 = "abc", 
    word2 = "pqr"
    sol1 = Solution().mergeAlternately(word1, word2)

    print(sol1)

