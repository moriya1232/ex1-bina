from PriorityQueue import *


def best_first_search(graph, function):
    q = PriorityQueue(function)
    start = graph.start
    closed = []
    q.put(start)
    num_nodes = 0
    while not q.is_empty():
        node = q.get()
        if node == graph.goal:
            return graph, num_nodes
        else:
            num_nodes += 1
            closed.append(node)
            for neighbor in node.neighbors:
                if neighbor not in closed and neighbor not in q.queue:
                    neighbor.father = node
                    closed.append(neighbor)
                    neighbor.g = node.g + neighbor.cost
                    q.put(neighbor)
                elif neighbor in q.queue and neighbor.g < q.get_by_loc(neighbor.location).g:
                    q.queue.remove(neighbor)
                    neighbor.father = node
                    q.put(neighbor)
    return None, None