class Solution:
  def isAnagram(self, s, t):
    if len(s) != len(t): return False

    hash = {} 

    for c in s:
        if c not in hash:
            hash[c] = 1 
        else:
            hash[c] += 1

    # print(hash)

    for c in t:
        if c in hash: 
            hash[c] -= 1
        if c not in hash:
            return False

    for c in hash:
        if hash[c] != 0:
            return False

    return True



print(Solution().is_anagram("cat", "tac"))
print(Solution().is_anagram("catasdasd", "asdastac"))
