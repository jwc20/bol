# Pangram (easy)


class Solution:
    def checkIfPangram(self, sentence):
        """
        Input: sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"
        Output: true
        Explanation: The sentence contains at least one occurrence of every letter of the English alphabet either in lower or upper case. 

        Input: sentence = "This is not a pangram"
        Output: false
        Explanation: The sentence doesn't contain at least one occurrence of every letter of the English alphabet.
        """

        # remove spaces in sentence and make them all lower case. 
        # then, use hashmap to keep count of the letters. 
        # the hashmap must have a-z letters set to 0.
        # each letter must have value of 1. 
        # at the end, check. 


        new_sentence = sentence.strip().lower()
        # print(new_sentence)

        alphabet = "abcdefghijklmnopqrstuvwxyz"

        d = {} 
        for c in alphabet: 
            d[c] = 0

        # print(d)

        i = 0

        for i in range(len(new_sentence)): 
            if new_sentence[i] in d: 
                d[new_sentence[i]] += 1


        print(d)
        for value in d.values(): 
            if value == 0: 
                return False

        return True



print(Solution().checkIfPangram("TheQuickBrownFoxJumpsOverTheLazyDog"))
print(Solution().checkIfPangram("This is not a pangram"))
