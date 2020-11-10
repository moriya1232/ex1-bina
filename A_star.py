from PriorityQueue import *
from Huristic_functions import *


def a_star(graph):
    graph.start.g = graph.start.cost
    closed = []
    q = PriorityQueue()
    q.put((graph.start.g + h_distance(graph, graph.start), graph.start, [[graph.start, ""]]))
    num_nodes = 1
    while not q.is_empty():
        f, node, path = q.get()
        if node == graph.goal:
            return path, num_nodes
        closed.append(node)
        for neighbor in node.neighbors:
            if neighbor not in closed:
                neighbor[0].g = node.g + neighbor[0].cost
                f_neighbor = neighbor[0].g + h_distance(graph, neighbor[0])
                path_neighbor = path + [neighbor]
                num_nodes += 1
                q.put((f_neighbor, neighbor[0], path_neighbor))
    return None
