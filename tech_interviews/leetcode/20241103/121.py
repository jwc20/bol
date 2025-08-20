"""

Input: prices = [7,1,5,3,6,4]
Output: 5





[7,1,5,3,6,4]


# (positive values are losses and negative values are profits)
6
2
4
1 <- max profit
3


i = 1
-4 <- max profit
-2
-5
-3



- another approach would be to use sorting before using left and right pointers 
O(n log n) time 

- after sorting the max value will always be on the right side and the min value will always be on the left side
- wew calculate the difference of max and min, then we get the max profit.

=> O(n log n) time and O(1) space



i, j
prices[i] <= prices[j] where i, j are position indices of the prices list. i < j (or i+1 <= j)


[7,1,5,3,6,4]
 i 


"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float("inf")
        max_profit = 0

        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]

            if abs(min_price - prices[i]) > max_profit:
                max_profit = abs(min_price - prices[i])

        return max_profit


p1 = [7, 1, 5, 3, 6, 4]

print(Solution().maxProfit(p1))
