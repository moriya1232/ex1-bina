from PriorityQueue import *
from Huristic_functions import *


def a_star(graph):
    graph.start.g = graph.start.cost
    closed = []
    q = PriorityQueue()
    q.put((graph.start.g + h_distance(graph, graph.start), graph.start, [[graph.start, ""]]))

    while not q.is_empty():
        f, node, path = q.get()
        if node == graph.goal:
            return path
        closed.append(node)
        for neighbor in node.neighbors:
            if neighbor not in closed:
                neighbor[0].g = node.g + neighbor[0].cost
                f_neighbor = neighbor[0].g + h_distance(graph, neighbor[0])
                path_neighbor = path + [neighbor]
                q.put((f_neighbor, neighbor[0], path_neighbor))
    return None
