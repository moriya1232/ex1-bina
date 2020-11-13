# moriya leopold

# TODO: check if ids need to run for ever if there is no solution or stup when it pass over all the nodes
num_nodes = 0
this_iteration_nodes = []

def ids(graph):
    global this_iteration_nodes
    global num_nodes
    i = 1
    prev = 0
    while True:
        this_iteration_nodes = [graph.start]
        num_nodes += 1
        res = dfs(graph, i)
        if prev == len(this_iteration_nodes):
            return None, None
        if res is not None:
            return res, num_nodes

        i += 1
        prev = len(this_iteration_nodes)


def dfs(graph, depth=float('inf')):
    global num_nodes
    global this_iteration_nodes
    res = []
    if depth <= 0:
        return None
    for neighbor1 in graph.start.neighbors:
        neighbor = neighbor1[0]
        if neighbor not in this_iteration_nodes:
            this_iteration_nodes.append(neighbor)
        path = [[graph.start, ""]]
        num_nodes += 1
        res = recursive_dfs(graph, neighbor, depth - 1, path + [neighbor1])
        if res is not None:
            break
    return res


def recursive_dfs(graph, node, depth, path=[]):
    global this_iteration_nodes
    global num_nodes
    if node.location == graph.goal.location:
        return path
    if depth <= 0:
        return None
    # for i in path:
    #     path_nodes.append(i[0])
    for neighbor1 in node.neighbors:
        neighbor = neighbor1[0]
        if neighbor not in this_iteration_nodes:
            this_iteration_nodes.append(neighbor)
        num_nodes += 1
        res = recursive_dfs(graph, neighbor, depth - 1, path + [neighbor1])
        if res is not None:
            return res
    return None
