# moriya leopold

# TODO: check if ids need to run for ever if there is no solution or stup when it pass over all the nodes


def ids(graph):
    i = 1
    while True:
        print(i)
        res, num_nodes = dfs(graph, i)
        if res is not None:
            print("Solution's size: " + str(i))
            return res, num_nodes
        i += 1


def dfs(graph, depth = float('inf')):
    res = []
    if depth <= 0:
        return None
    for neighbor1 in graph.start.neighbors:
        neighbor = neighbor1[0]
        path = [[graph.start, ""]]
        num_nodes = 1
        if neighbor not in path:
            num_nodes += 1
            res, i = recursive_dfs(graph, neighbor, depth - 1, num_nodes, path + [neighbor1])
            if res is not None:
                break
    return res, num_nodes


def recursive_dfs(graph, node, depth, num_nodes, path=[]):
    if node.location == graph.goal.location:
        return path, num_nodes
    if depth <= 0:
        return None, None
    for neighbor1 in node.neighbors:
        neighbor = neighbor1[0]
        if neighbor not in path:
            num_nodes += 1
            res, res_num_nodes = recursive_dfs(graph, neighbor, depth - 1, num_nodes, path+[neighbor1])
            if res is not None:
                return res, num_nodes
    return None, None
