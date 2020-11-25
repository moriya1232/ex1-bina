from Huristic_functions import *

num_nodes = 1


def ida_star(graph, function):              #IDA* algorithm
    global num_nodes
    depth = 20
    threshold = function(graph.start)
    path = [graph.start]
    graph.start.g = graph.start.cost
    while True:
        t, path, is_done = search(graph, function, threshold, graph.start, path, graph.start.cost, depth)
        if is_done:
            return graph, num_nodes
        if t == float('inf'):
            return None, None
        threshold = t
    return None, None


def search(graph, function, threshold, node, path, cost, depth):   # recursive algorithm od IDA*
    global num_nodes
    if depth <= 0:
        return float('inf'), None, True
    min_f = float('inf')
    f = cost + function(node)
    if node == graph.goal:
        return f, path, True
    if f > threshold:
        return f, path, False
    for neighbor in node.neighbors:
        neighbor.father = node
        t, res_path, res_found = search(graph, function, threshold, neighbor, path + [neighbor], cost+neighbor.cost,  depth -1)
        if res_found:
            return min_f, res_path, True
        num_nodes += 1
        if t < min_f:
            min_f = t
    return min_f, path, False
