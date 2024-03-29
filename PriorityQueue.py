# priority queue, this diffrent a little form the regular priority queue
# it use huristic function


class PriorityQueue(object):
    def __init__(self, huristic_function):
        self.queue = []
        self.h = huristic_function

    # get True or False if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # insert elemnet to queue
    def put(self, data):
        self.queue.append(data)

    # pop the element
    def get(self):
        if self.is_empty():
            return None
        min = self.queue[0]
        for i in self.queue:
            # check by the huristic function
            if i.g + self.h(i) < min.g + self.h(min):
                min = i
        self.queue.remove(min)
        return min

    # get the node from the priority
    def get_by_loc(self, location):
        for i in self.queue:
            if i.location == location:
                return i

