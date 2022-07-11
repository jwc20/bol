
from typing import List

def fun(prices: List[float]) -> float:

    min_price = float('inf')
    max_profit = 0.0

    for price in prices:
        min_price = min(min_price, price)
        temp = price - min_price
        max_profit = max(max_profit, temp)
    return max_profit

print(fun([310,315,275, 260, 290, 255]))

