
# N叉树的前序遍历
# 给定一个 N 叉树，返回其节点值的前序遍历。



class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def helper(root):
            if not root:
                return None
            result.append(root.val)
            children = root.children
            for child in children:
                helper(child)
        helper(root)
        return result