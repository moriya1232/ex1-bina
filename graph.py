
class graph:

    def __init__(self, start, goal, size, costs):
        col = 0
        row = 0
        nodes = []
        while row < size:
           while col < size:
               location = row*size+col
               cost = costs[location]
               nodes.append(node(location, cost))
               col+=1
           ++row

        for n in nodes:
            self.addNeighbors(self, n, size, nodes)



    def addNeighbors(self, node, size, nodes):
        location = node.location
        up_n = location - size
        down_n = location + size
        right_n = location + 1
        left_n = location - 1
        source_neighbors = [up_n - 1, up_n, up_n + 1, location - 1, right_n, left_n, down_n - 1, down_n, down_n + 1]
        up = [up_n - 1, up_n, up_n + 1]
        down = [down_n - 1, down_n, down_n + 1]
        left = [up_n - 1, left_n, down_n - 1]
        right = [up + 1, right_n, down_n + 1]

        # first column
        if location % size == 0:
            for l in left:
                source_neighbors.remove(l)
        # latest column
        elif location % size == size - 1:
            for r in right:
                source_neighbors.remove(r)
        for n in source_neighbors:
            if n<0 and n>=size*size:
                source_neighbors.remove(n)

        # check if up is -1
        if (nodes[up_n].cost == -1):
            for u in up:
                source_neighbors.remove(u)
        # check if down is -1
        if (nodes[down_n].cost == -1):
            for d in down_n:
                source_neighbors.remove(d)
        # check if left is -1
        if (nodes[left_n].cost == -1):
            for l in left:
                source_neighbors.remove(l)
        # check if right is -1
        if (nodes[right_n].cost == -1):
            for r in right:
                source_neighbors.remove(r)
        # create neighbors
        for n in source_neighbors:
            node.addNeighbor(nodes[n])


class node:

    def __init__(self, location, cost):
        self.location= location
        self.cost = cost
        self.neighbors = []

    def addNeighbor(self, node):
        self.neighbors.append(node)