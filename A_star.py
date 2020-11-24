from PriorityQueue import *
from Huristic_functions import *

# a_star algorithm


def a_star(graph):
    graph.start.g = graph.start.cost
    closed = []
    q = PriorityQueue()
    # use calculate of huristic function
    q.put((graph.start.g + h_distance(graph, graph.start), graph.start, [[graph.start, ""]]))
    num_nodes = 1
    # evalute by the queue but if its will come to the goal node it will stop (return)
    while not q.is_empty():
        f, node, path = q.get()
        if node == graph.goal:
            return path, num_nodes
        closed.append(node)
        for neighbor1 in node.neighbors:
            neighbor = neighbor1[0]
            if neighbor not in closed:
                neighbor.g = node.g + neighbor.cost
                # calculate by huristic function
                f_neighbor = neighbor.g + h_distance(graph, neighbor)
                path_neighbor = path + [neighbor1]
                num_nodes += 1
                q.put((f_neighbor, neighbor, path_neighbor))
    return None
