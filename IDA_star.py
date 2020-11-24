from Huristic_functions import *


def ida_star(graph):              #IDA* algorithm
    depth = 20
    threshold = h_distance(graph, graph.start)
    path = [[graph.start, ""]]
    graph.start.g = graph.start.cost
    num_nodes = 1      # count the nodes that evaluated
    while True:
        t, path, is_done, num_nodes = search(graph, threshold, graph.start, path, graph.start.cost, num_nodes, depth)
        if is_done:
            return path, num_nodes
        threshold = t
    return None


def search(graph, threshold, node, path, cost, num_nodes, depth):   # recursive algorithm od IDA*
    min_f = float('inf')
    f = cost + h_distance(graph, node)
    if depth <= 0:
        return f, path, False, num_nodes
    if f > threshold:
        return f, path, False, num_nodes
    if node == graph.goal:
        return f, path, True, num_nodes
    for neighbor1 in node.neighbors:
        neighbor = neighbor1[0]
        num_nodes += 1
        t, res_path, res_found, num_nodes = search(graph, threshold, neighbor, path + [neighbor1], cost+neighbor.cost, num_nodes, depth -1)
        if res_found:
            return min_f, res_path, True, num_nodes
        if t < min_f:
            min_f = t
    return min_f, path, False, num_nodes
