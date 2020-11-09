import queue


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def put(self, data):
        self.queue.append(data)

    def get(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min][0]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()

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
