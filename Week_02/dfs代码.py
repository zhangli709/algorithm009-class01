

# DFS代码 - 递归写法

visited = set() # 和树中的DFS最大区别

def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)

    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)