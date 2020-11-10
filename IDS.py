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
    res = []
    if depth <= 0:
        return None
    for neighbor1 in graph.start.neighbors:
        neighbor = neighbor1[0]
        path = [[graph.start, ""]]
        if neighbor not in path:
            res = recursive_dfs(graph, neighbor, depth - 1, path + [neighbor1])
            if res is not None:
                break
    return res


def recursive_dfs(graph, node, depth, path=[]):
    if node.location == graph.goal.location:
        return path
    if depth <= 0:
        return None
    for neighbor1 in node.neighbors:
        neighbor = neighbor1[0]
        if neighbor not in path:
            res = recursive_dfs(graph, neighbor, depth - 1, path+[neighbor1])
            if res is not None:
                return res
    return None
