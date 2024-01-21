"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        a naive approach would be to split each word into a list of words 
        s = "let's take leetcode contest"

        => ["let's", "take", "leetcode", "contest"]
        
        now we would iterate over the list and reverse each strings using two pointers.
        using two pointers would reduce the time complexity to o(n).
        otherwise, we can use sorting function, which would have the time of o(nlogn)

        storing individual words into a list would additional memory. => o(s) where s is the length of the input s.

        after reversing each words, we join the sentence and return. 

        time: o(n); space: o(s)


        another approach would be to have conditional checking to check for spaces.
        not sure how to implement this.
        """

        result = [] 
        words = s.split()

        for word in words:
            wl = list(word)
            l, r = 0, len(wl) - 1
            while l < r:
                wl[l], wl[r] = wl[r], wl[l]
                l, r = l+1, r-1

            result.append("".join(wl))
            # print(" ".join(result))

        return " ".join(result)



    def reverseWords1(self, s: str) -> str:

        """ 
        This is approach builds from the above function and has a better space complexity.
        The trick is to use two pointers through out the whole string.
        """
        s = list(s)
        l = 0

        for r in range(len(s)):
            if s[r] == " " or r == len(s) - 1:
                temp_l, temp_r = l, r - 1

                if r == len(s) - 1:
                    temp_r = r 
                while temp_l < temp_r:
                    s[temp_l], s[temp_r] = s[temp_r], s[temp_l]
                    temp_l, temp_r = temp_l + 1, temp_r - 1
                l = r + 1
        return "".join(s)




if __name__ == '__main__': 
    s1 = "Let's take LeetCode contest"
    s2 = "Mr Ding" 

    sol1 = Solution().reverseWords1(s1)
    sol2 =  Solution().reverseWords1(s2)

    print(sol1)
    print(sol2)


