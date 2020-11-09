from PriorityQueue import *

def ucs(graph):
    visited = []
    q = PriorityQueue()
    start = graph.start
    q.put((start.cost, start, [start]))

    while not q.is_empty():
        cumulative_cost, node, path = q.get()
        visited.append(node)

        if node == graph.goal:
            return path
        else:
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    cur_cumulative_cost = cumulative_cost + neighbor.cost
                    temp_path = path + [neighbor]
                    q.put((cur_cumulative_cost, neighbor, temp_path))
    return None
