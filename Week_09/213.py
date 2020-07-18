

# 213 打家劫舍II

"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
"""


class Solution:
    def rob(self, nums: List[int]) -> int:

        def foo(nums):
            n = len(nums)
            if not nums: return 0
            if n == 1: return nums[0]
            # 1. 定义状态转移公式
            dp = [0] * n

            # 2. 定义边界条件
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            # 3. 定义转移方程
            for i in range(2, n):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[n - 1]

        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(foo(nums[:-1]), foo(nums[1:]))
