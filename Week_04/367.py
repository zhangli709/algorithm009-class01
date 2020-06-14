

# 367 有效的完全平方数

# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

# 说明：不要使用任何内置的库函数，如  sqrt。


# 1. 暴力破解法

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        i = 1
        while i ** 2 < num:
            i += 1
        return i ** 2 == num

# 2. 二分法

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r =0, num//2+1
        while l<r:
            mid = l+r+1 >> 1
            if mid**2 > num:
                r =mid- 1
            else:
                l = mid
        return l**2 == num

# 3. 牛顿法

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = num
        while i ** 2 > num:
            i = (i + num / i) // 2
        return i ** 2 == num



