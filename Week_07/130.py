

# 被围绕的区域

"""
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp_i = i + x
                tmp_j = j + y
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == '0':
                    dfs(tmp_i, tmp_j)

        for j in range(col):
            # 第一行
            if board[0][j] == '0':
                dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "0":
                dfs(row - 1, j)

        for i in range(row):
            # 第一列
            if board[i][0] == '0':
                dfs(i, 0)
            # 最后一列
            if board[i][col - 1] == '0':
                dfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                # 0 --> X
                if board[i][j] == '0':
                    board[i][j] = 'X'

                # B --> 0
                if board[i][j] == 'B':
                    board[i][j] = '0'