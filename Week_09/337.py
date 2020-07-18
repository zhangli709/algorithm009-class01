
# 337 打家劫舍

"""
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。


"""


class Solution:
    def rob(self, root: TreeNode) -> int:
        return self.helper(root)[1]

    # helper函数返回一个节点为根的最大值 = [当前节点不参与计算的最大收益，当前节点的最大收益(参与/不参与)]
    def helper(self, root):
        if root is None:
            return [0, 0]
        left_amount = self.helper(root.left)
        right_amount = self.helper(root.right)
        withoutRoot = left_amount[1] + right_amount[1]
        withRoot = root.val + left_amount[0] + right_amount[0]
        return [withoutRoot, max(withRoot, withoutRoot)]