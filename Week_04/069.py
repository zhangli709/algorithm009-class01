


# x 的 平方根

"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

"""

#  1. 内置函数法
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)


# 2. 二分查找法
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x // 2 + 1
        while l < r:
            mid = l + r + 1 >> 1
            tmp = mid ** 2
            if tmp > x:
                r = mid - 1
            else:
                l = mid
        return l

# 3.牛顿法
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        # 起始的时候在 1 ，这可以比较随意设置
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)


