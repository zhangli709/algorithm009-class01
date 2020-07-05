

# 岛屿数量

"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    grid[i][j] == '0'
                    my_list = collections.deque()
                    my_list.append([i,j])
                    while len(my_list)>0:
                        x,y = my_list.popleft()
                        for a,b in [[x-1,y],[x+1,y],[x, y-1],[x,y+1]]:
                            if 0<=a<len(grid) and 0 <=b<len(grid[0]) and grid[a][b] == '1':
                                my_list.append([a,b])
                                grid[a][b] = '0'
        return cnt