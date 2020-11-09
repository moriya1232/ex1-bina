# moriya leopold

# TODO: check if ids need to run for ever if there is no solution or stup when it pass over all the nodes


def ids(graph):
    i = 1
    while True:
        res = dfs(graph, i)
        if res is not None:
            print("Solution's size: " + str(i))
            return res
        i += 1


def dfs(graph, depth = float('inf')):
    if depth <= 0:
        return None
    for neighbor in graph.start.neighbors:
        visited = [graph.start]
        path = [graph.start]
        if neighbor not in path:
            path.append(neighbor)
            depth -= 1
            res = recursive_dfs(graph, neighbor, depth, visited, path)
            if res is not None:
                break
    return res


def recursive_dfs(graph, node, depth, visited=[], path=[]):
    if node.location == graph.goal.location:
        return path
    if depth <= 0:
        return None
    if node not in visited:
        visited.append(node)
        for neighbor in node.neighbors:
            if neighbor not in path:
                path.append(neighbor)
                depth -= 1
                return recursive_dfs(graph, neighbor, depth, visited, path)
