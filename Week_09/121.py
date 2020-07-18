
# 121 买卖股票的最佳时机

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 两个变量，一个存放当前最小值，一个存放当前最大利润

        cur_min = float('inf')
        cur_max_money = 0
        for i in prices:
            cur_min = min(cur_min, i)
            cur_max_money = max(cur_max_money, i-cur_min)
        return cur_max_money