


def BFS(graph, start,end):
    queue = []
    queue.append([start])

    visited = set() # 和数中的BFS的最大区别

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)