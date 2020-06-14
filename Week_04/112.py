


# 122 买卖股票的最佳时机

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            temp = prices[i] - prices[i-1]
            if temp > 0:
                res += temp
        return res