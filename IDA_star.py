from Huristic_functions import *


def ida_star(graph):
    threshold = h_distance(graph, graph.start)
    path = [[graph.start, ""]]
    graph.start.g = graph.start.cost
    num_nodes = 1
    while True:
        path, is_done, num_nodes = search(graph, threshold, graph.start, path, graph.start.cost, num_nodes)
        if is_done:
            return path, num_nodes
        threshold += 1
    return None


def search(graph, threshold, node, path, cost, num_nodes):
    f = cost + h_distance(graph, node)
    if f > threshold:
        return path, False, num_nodes
    if node == graph.goal:
        return path, True, num_nodes
    # min_f = float('inf')
    for neighbor1 in node.neighbors:
        neighbor = neighbor1[0]
        num_nodes += 1
        res_path, res_found = search(graph, threshold, neighbor, path + [neighbor1], cost+neighbor.cost)
        if res_found:
            return res_path, True, num_nodes
    return path, False, num_nodes
