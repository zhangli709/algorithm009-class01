


# 解数独
"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def getLocs(board):#初始化，获取需要填充的位置，记录为一个栈
            locs = []
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        locs.append((row, col))
            return locs

        def getMaps(board):#定义三个字典，跟踪9行、9列和9块的已填充数字，采用数据结构为defaultdict
            from collections import defaultdict as dd
            rowMap = [dd(int) for _ in range(9)]
            colMap = [dd(int) for _ in range(9)]
            blockMap = [dd(int) for _ in range(9)]
            for row in range(9):
                for col in range(9):
                    if board[row][col] != '.':
                        num = int(board[row][col])
                        rowMap[row][num] += 1
                        colMap[col][num] += 1
                        bolckIndex = int(row/3)*3+int(col/3)
                        blockMap[bolckIndex][num] += 1
            return rowMap, colMap, blockMap

        def fillBoard(board, locs):#递归填充剩余的数独空位置
            if not locs:
                return True
            row, col = locs.pop()#弹出一个待填充位置
            bolckIndex = int(row/3)*3+int(col/3)
            found = False
            for num in range(1, 10):
                if found:
                        break
                if not rowMap[row][num] and not colMap[col][num] and not blockMap[bolckIndex][num]:
                    ##如果当前行、当前列和当前块均不存在该数字，则将数字更新到相应行、列、块，并尝试填充
                    rowMap[row][num] = 1
                    colMap[col][num] = 1
                    blockMap[bolckIndex][num] = 1
                    board[row][col] = str(num)
                    found = fillBoard(board, locs)#递归到下一层填充
                    rowMap[row][num] = 0##状态回溯，将填充的位置清空
                    colMap[col][num] = 0
                    blockMap[bolckIndex][num] = 0
            if not found:##如果本轮都无法求解，则回溯到初始状态，继续从前面再填充
                locs.append((row, col))
                board[row][col] = '.'
            return found

        rowMap, colMap, blockMap = getMaps(board)
        locs = getLocs(board)
        fillBoard(board, locs)

