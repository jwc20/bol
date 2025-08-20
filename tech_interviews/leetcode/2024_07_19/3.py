"""
1002. Find Common Characters
Easy

Given a string array words, return an array of all characters that show up in all strings within the words 
(including duplicates). 
You may return the answer in any order.


Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
358.3K
Submissions
480.4K
Acceptance Rate
74.6%
"""

from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        we can use a hashmap, but this will take additional space. => O( length of the longest word )

        time : O (length of list * length of word)

        """

        d = {}
        # d = defaultdict()

        for w in words:
            for c in w:
                if c not in d:
                    d[c] = 0

                d[c] += 1
        return d



print(Solution().commonChars(["cool","lock","cook"]))

        
