from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for idx in range(len(prices)-1):
            if prices[idx+1] > prices[idx]:
                max_profit += prices[idx+1] - prices[idx]
        return max_profit
