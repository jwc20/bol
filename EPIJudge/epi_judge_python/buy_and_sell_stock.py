from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:

    # c = 0
    # n = 1
    # diff = []
    # while n < len(prices) - 1:
    #     print(c, n)
    #     if prices[c] - prices[n] < 0:
    #         c += 1
    #         n += 1
    #     if prices[c] - prices[n] ==  0:
    #         n = c + 1
    #     else:
    #         diff.append(prices[c] - prices[n])
    #         n += 1
    # return max(diff)

    # Brute Force O(n^2)
    # res = []
    # for i in range(len(prices) - 1):
    #     for j in range(1, len(prices)):
    #         if prices[i] < prices[j]:
    #             print(prices[i], prices[j])
    #             res.append(prices[j] - prices[i])
    #         # else:
    #         #     res.append(abs(prices[j] - prices[i]))
    # if len(res) == 0:
    #     return 0
    # return max(res)

    ####
    left = 0
    right = 1
    current_profit = float("inf")
    max_profit = 0.0
    while right < len(prices):
        current_profit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            max_profit = max(current_profit, max_profit)
        else:
            left = right
        right += 1

    return max_profit


# print(buy_and_sell_stock_once([310,315,275,295,260,270,290, 230, 255, 250]))
# print(buy_and_sell_stock_once([0.3, 0.3, 0.1]))
# print(buy_and_sell_stock_once([0.3, 0.2, 0.3]))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once
        )
    )
