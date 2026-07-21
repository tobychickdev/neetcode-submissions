class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            profit = max(prices[i:]) - prices[i]
            max_profit = max(max_profit, profit)
        return max_profit

        