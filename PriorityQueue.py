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
