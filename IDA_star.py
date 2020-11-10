from Huristic_functions import *


def ida_star(graph):
    threshold = h_distance(graph, graph.start)
    path = [[graph.start, ""]]
    graph.start.g = graph.start.cost
    while True:
        path, is_done = search(graph, threshold, graph.start, path, graph.start.cost)
        if is_done:
            return path
        threshold += 1
    return None


def search(graph, threshold, node, path, cost):
    f = cost + h_distance(graph, node)
    if f > threshold:
        return path, False
    if node == graph.goal:
        return path, True
    # min_f = float('inf')
    for neighbor1 in node.neighbors:
        neighbor = neighbor1[0]
        res_path, res_found = search(graph, threshold, neighbor, path + [neighbor1], cost+neighbor.cost)
        if res_found:
            return res_path, True
    return path, False
