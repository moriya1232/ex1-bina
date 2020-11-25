class PriorityQueue(object):     # priority queue, this diffrent a little form the regular priority queue
    def __init__(self, huristic_function):
        self.queue = []
        self.h = huristic_function

    def is_empty(self):
        return len(self.queue) == 0

    def put(self, data):
        self.queue.append(data)

    def get(self):
        if self.is_empty():
            return None
        min = self.queue[0]
        for i in self.queue:
            if i.g + self.h(i) < min.g + self.h(min):
                min = i
        self.queue.remove(min)
        return min

    def get_by_loc(self, location):
        for i in self.queue:
            if i.location == location:
                return i

