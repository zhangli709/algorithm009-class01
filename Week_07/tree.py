



# 前序

def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)


# 中序
def inorder(self, root):
    if root:

        self.preorder(root.left)
        self.traverse_path.append(root.val)
        self.preorder(root.right)


# 后序
def postorder(self, root):
    if root:

        self.preorder(root.left)
        self.preorder(root.right)
        self.traverse_path.append(root.val)