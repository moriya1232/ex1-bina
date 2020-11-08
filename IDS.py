#moriya leopold


def dfs(graph, node, visited=[], path=[]):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbor in node.neighbors:
            dfs(graph, neighbor, vidited, path.append(neighbor))
    return path