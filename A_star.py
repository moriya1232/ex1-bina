from PriorityQueue import *
import math


def h(graph, node):
    loc_goal = graph.goal.location
    row_goal = math.floor(loc_goal / graph.size)
    col_goal = loc_goal % graph.size
    loc_cur = node.location
    row_cur = math.floor(loc_cur / graph.size)
    col_cur = loc_cur % graph.size
    return math.ceil(abs(row_goal - row_cur) + abs(col_goal - col_cur) / 2)


def a_star(graph):
    graph.start.g = graph.start.cost
    closed = []
    q = PriorityQueue()
    q.put((graph.start.g + h(graph, graph.start), graph.start, [graph.start]))

    while not q.is_empty():
        f, node, path = q.get()
        if node == graph.goal:
            return path
        closed.append(node)
        for neighbor in node.neighbors:
            if neighbor not in closed:
                neighbor.g = node.g + neighbor.cost
                f_neighbor = neighbor.g + h(graph, neighbor)
                path_neighbor = path + [neighbor]
                q.put((f_neighbor, neighbor, path_neighbor))
    return None
