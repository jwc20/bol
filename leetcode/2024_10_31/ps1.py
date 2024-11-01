








from collections import namedtuples

class Solution:
    def firstUniqChar(self, s: str) -> int:

        """
        input: a string 
        output: integer, the position of the first non-repeating character, if it doesnt exists, return -1.


        Example 1:
            Input: s = "leetcode"
            Output: 0
        
        Example 2:
            Input: s = "loveleetcode"
            Output: 2
        
        Example 3:
            Input: s = "aabb"
            Output: -1


        - the order of the string matters, so we cannot presort the string to check for repeating characters.

        The most naive approach would be to use multiple loops over the string and check for each character a repeating character exists.


        Although this will take O(n^2) Time (where n is the length of the input string),it will take O(1) space.

        Another approach that will use O(n) time and space, would be to use a hashmap to get the count for each character.
        When we are done iterating though the string, we can check the hashmap (dictionary) and get the first item that has the value of 1.



        Another approach would be to use a stack. (maybe)

        [l]         push l
        [lo]        push l, its not the same as o
        [l]         pop o

        (this will not work, and it doenst make sense and im also dumb)


        The interviewer will probably not like the O(n^2) appraoach, so use the hashmap approach.




        """

        d = {}
        for i in range(len(s)):

            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1

        for item in d.values():
            return item[0] 

        return -1

        
        # maybe use a namedtuple?

#         HashMap = namedtuples('HashMap', ('index','value', 'count'))  


#         for i in range(len(s)):
#             if s[i] not in HashMap:
#                 HashMap(i, s[i], 1)
#             else:



        return 0 
