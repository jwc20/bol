from typing import List


def func(A: List[float]) -> float:

    """
    - Use sliding window
    - keep track of current profit, max profit, and minimum price.
    - set max_profit = 0, min_price = inf
    - have the right pointer iterating using for loop
    - when current profit is less than the max_profit, then shift the left pointer to right pointer position

    [4,2,1,4,7] => 6

    [4,2,1,4,7]
     ^ ^
       ^ ^
         ^ ^   -> max_profit = 3
         ^   ^ -> max_profit = 6
    """

    max_profit = 0.0
    min_price = float("inf")

    for price in A:
        curr_profit = price - min_price
        max_profit = max(curr_profit, max_profit)
        min_price = min(min_price, price)

    return max_profit


prices0 = [4, 2, 1, 4, 7]

print(func(prices0))
