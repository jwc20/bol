"""
    Buy and sell a stock once
    [310, 315, 275, 295, 260, 270, 290, 230, 255, 250] -> 30 
    
    A naive approach would be to calculate difference for each elements from left to right, append to new subarrays, and find the max profit.
    (So calculate for 310 with all other subsequent elements, then 315, then 275, ... )
    Since we need to iterate through list multiple times for each elements; by Guass summation rule, it will take O(n(n-1) / 2) ~ O(n^2) time and O(n) space.
    A better approach would be to iterate through the list once, use a sliding window to calculate the profit between the left and right side.
    We need to keep track of the minimum price(to calculate with max price), current profit, and max profit 
    When we hit the point where the current profit is less than the max_profit, make the left side of the window be the right side.
    For each step, we need to check if the difference (profit) is greater than the current profit.

    [310, 315, 275, 295, 260, 270, 290, 230, 255, 250] 
     ^l    ^r                                           min_price = -inf, profit = 5, max_profit = 0         
     ^l    ^r                                           min_price = 310, profit = 5, max_profit = 5
     ^l         ^r                                      min_price = 310, profit = -35, max_profit = 5 => shrink window
                ^l   ^r                                 min_price = 275, profit = 20, max_profit = 5
                ^l   ^r                                 min_price = 275, profit = 20, max_profit = 20 
                ^l        ^r                            min_price = 275, profit = -15, max_profit = 20 => shrink window 
                          ^l   ^r                       min_price = 260, profit = 10, max_profit = 20
                          ^l        ^r                  min_price = 260, profit = 30, max_profit = 30
                          ^l             ^r             min_price = 260, profit = -30, max_profit = 30 => shrink window
                                         ^l    ^r       min_price = 230, profit = 25, max_profit = 30
                                         ^l         ^r  min_price = 230, profit = 20, max_profit = 30
"""

from typing import List


def func1(A: List[float]) -> float:
    min_price, max_profit = float("inf"), 0.0
    # l, r = 0, 1
    # r = 1
    # while r < len(A):
    for price in A:
        current_profit = price - min_price
        max_profit = max(max_profit, current_profit)
        min_price = min(min_price, price)

    return max_profit


prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(func1(prices))
