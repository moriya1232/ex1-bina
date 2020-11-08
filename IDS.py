#moriya leopold





def dfs(graph, node, depth):
    #if depth<=0:

    visited = []
    if node not in visited:
        visited.append(node)
        for n in node.neighberhood():
            dfs(graph, n, --depth