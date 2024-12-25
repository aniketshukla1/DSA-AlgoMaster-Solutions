from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying_price = prices[0]

        for idx in range(1, len(prices)):
            if buying_price > prices[idx]:
                buying_price = prices[idx]
            elif prices[idx] - buying_price > max_profit:
                max_profit = prices[idx] - buying_price

        return max_profit
