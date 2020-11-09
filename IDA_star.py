from Huristic_functions import *


def ida_star(graph):
    h = h_distance(graph, graph.start)
    path = [graph.start]
    graph.start.g = graph.start.cost
    isFound = false
    while True:
        f, path, isFound = search(graph, h, graph.start, path, isFound)
        if path is not None:
            return path
    return None


def search(graph, h, node, path):
    f = node.g + h(node)
    min_f = float('inf')
    if f > h:
        return f, path, False
    if node == graph.goal:
        return f, path, True
    for neighbor in node.neighbors:
        res_f, res_path, res_found = search(graph, h, neighbor, path + [neighbor])
        if res_found:
            return res_path, res_found
        elif res_f < min:
            min_f = res_f
    return min_f, path, False
