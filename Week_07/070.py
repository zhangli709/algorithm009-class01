

# 爬楼梯  五种解法


class Solution:
    # def climbStairs(self, n: int) -> int:
    #     f1 = 1
    #     f2 = 2
    #     res = 0
    #     for i in range(2, n):
    #         res = f1+f2
    #         f1 = f2
    #         f2 = res
    #     return max(res, n)

    # 1. 直接递归法 + 缓存
    # @functools.lru_cache(100)
    # def climbStairs(self, n:int) -> int:
    #     if n ==1:return 1
    #     if n ==2:return 2
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 2. 直接DP法， 新建一个字典或者数组来存储以前的变量，空间复杂度0（n)
    # def climbStairs(self, n:int) ->int:
    #     dp = {}
    #     dp[1] = 1
    #     dp[2] = 2
    #     for i in range(3, n+1):
    #         dp[i] = dp[i-1] + dp[i-2]
    #     return dp[n]

    # 3. DP , 只存储前两个元素，减少了空间复杂度，空间复杂度o(1)
    # def climbStairs(self, n:int) -> int:
    #     if n==1 or n==2: return n
    #     a,b,tmp = 1,2,0
    #     for i in range(3, n+1):
    #         tmp = a+b
    #         a = b
    #         b = tmp
    #     return tmp

    # 4. 直接斐波那契数列计算公式
    def climbStairs(self, n: int) -> int:
        import math
        sqrt5 = 5 ** 0.5
        fibin = math.pow((1 + sqrt5) / 2, n + 1) - math.pow((1 - sqrt5) / 2, n + 1)
        return int(fibin / sqrt5)

