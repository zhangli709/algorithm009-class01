
# 746 使用最小花费爬楼梯


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if not cost:return 0
        if len(cost)==1:return cost[0]
        # 1.
        dp = [0] * n

        # 2.
        dp[0] = 0
        dp[1] = min(cost[0], cost[1])

        # 3.
        for i in range(2, n):
            dp[i] = min(dp[i-1]+cost[i], dp[i-2]+cost[i-1])
        return dp[-1]