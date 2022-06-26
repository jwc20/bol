from typing import List


def fun(A: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0.0
    for price in A:
        max_profit_sell_today = price - min_price 
        max_profit = max(max_profit_sell_today, max_profit)
        min_price = min(price, min_price)
    return max_profit

print(fun([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))
