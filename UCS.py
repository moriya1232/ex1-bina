from PriorityQueue import *


def ucs(graph):
    q = PriorityQueue()
    start = graph.start
    visited = [start]
    q.put((start.cost, start, [[start, ""]]))
    num_nodes = 1
    while not q.is_empty():
        cumulative_cost, node, path = q.get()
        if node == graph.goal:
            return path, num_nodes
        else:
            for neighbor1 in node.neighbors:
                neighbor = neighbor1[0]
                if neighbor not in visited:
                    visited.append(neighbor)
                    cur_cumulative_cost = cumulative_cost + neighbor.cost
                    temp_path = path + [neighbor1]
                    num_nodes += 1
                    q.put((cur_cumulative_cost, neighbor, temp_path))
    return None
