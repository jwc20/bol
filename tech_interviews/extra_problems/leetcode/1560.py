import bisect 
from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        first, last = rounds[0], rounds[-1]

        if last >= first:
            return [i for i in range(first, last + 1)]

        else:
            res = []
            for i in range(n):
                if last >= i+1 or first <= i+1:
                    if res: 
                        bisect.insort(res, i+1)
                    else:
                        res.append(i+1)

        return res


# Input: n = 2, rounds = [2,1,2,1,2,1,2,1,2]
# Output: [2]
# Example 3:
# 
# Input: n = 7, rounds = [1,3,5,7]
# Output: [1,2,3,4,5,6,7]

print(Solution().mostVisited(4, [1,3,1,2]))
print(Solution().mostVisited(7, [1,3,5,7]))
print(Solution().mostVisited(2, [2,1,2,1,2,1,2,1,2]))
print(Solution().mostVisited(3, [3,2,1,2,1,3,2,1,2,1,3,2,3,1]))
