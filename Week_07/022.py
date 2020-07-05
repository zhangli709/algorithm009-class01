


# 括号生成

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # res = []
        # cur = ''
        # def dfs(cur, left, right):
        #     if left ==0 and right ==0:
        #         res.append(cur)
        #         return
        #     if right < left:
        #         return
        #     if left > 0:
        #         dfs(cur+'(', left -1, right)
        #     if right > 0:
        #         dfs(cur+')', left, right -1 )

        # dfs(cur, n,n)
        # return res

        # 1. 深度优先遍历
        # res = []
        # cur_str = ''
        # def dfs(cur_str, left, right):
        #     """
        #     :param cur_str: 从根节点到叶子节点的路径字符串
        #     :param left: 左括号还可以使用的个数
        #     :param right 右括号还可以使用的个数
        #     :return
        #     """
        #     if left ==0 and right ==0:
        #         res.append(cur_str)
        #         return
        #     if right < left:
        #         return
        #     if left > 0:
        #         dfs(cur_str + '(', left-1, right)
        #     if right > 0:
        #         dfs(cur_str + ')', left, right-1)
        # dfs(cur_str, n,n)
        # return res

        # 2.  广度优先遍历

        # 3. 动态规划
        # if n ==0:return[]
        # dp = [None for _ in range(n+1)]
        # dp[0] = ['']
        # for i in range(1, n+1):
        #     cur = []
        #     for j in range(i):
        #         left = dp[j]
        #         right = dp[i-j-1]
        #         for s1 in left:
        #             for s2 in right:
        #                 cur.append('(' + s1 + ')'+s2)
        #     dp[i] = cur
        # return dp[n]

        # 4. 回溯法
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')

