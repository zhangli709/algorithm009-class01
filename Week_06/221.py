

# 221. 最大正方形

# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。


# 1. 暴力求解


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 暴力求解法
        # 思路，遍历，每次碰到1， 就以次数开始往下和往右一行是否为零。
        # if len(matrix) == 0 or len(matrix[0]) == 0:
        #     return 0

        # maxSide = 0
        # rows, columns = len(matrix), len(matrix[0])
        # for i in range(rows):
        #     for j in range(columns):
        #         if matrix[i][j] == '1':
        #             # 遇到一个 1 作为正方形的左上角
        #             maxSide = max(maxSide, 1)
        #             # 计算可能的最大正方形边长
        #             currentMaxSide = min(rows - i, columns - j)
        #             for k in range(1, currentMaxSide):
        #                 # 判断新增的一行一列是否均为 1
        #                 flag = True
        #                 if matrix[i + k][j + k] == '0':
        #                     break
        #                 for m in range(k):
        #                     if matrix[i + k][j + m] == '0' or matrix[i + m][j + k] == '0':
        #                         flag = False
        #                         break
        #                 if flag:
        #                     maxSide = max(maxSide, k + 1)
        #                 else:
        #                     break

        # maxSquare = maxSide * maxSide
        # return maxSquare

        # 动态规划
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare

