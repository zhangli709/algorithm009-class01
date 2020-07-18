

# 070 爬楼梯

class Solution:

    # 1. 递归法，使用缓存
    # @functools.lru_cache(100)
    # def climbStairs(self, n: int) -> int:
    #     if n < 3: return n
    #
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 2. 动态规划
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1],dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]