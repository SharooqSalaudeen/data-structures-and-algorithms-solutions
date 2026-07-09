from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = max(profit, prices[j] - prices[i])
        return profit
