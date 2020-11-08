
def main():
    file = open("input.txt", r)
    print(file.read())



class graph_factory:

    def create_graph(self, file):
        algo = ""
        row_start = 0
        col_start = 0
        row_goal = 0
        col_goal = 0
        size = 0
        costs = []
        lines = file.readLines()
        num_line = 0
        for line in lines:
            if num_line == 0:
                algo = line
            elif num_line == 1:
                str_loc = line.split(",")
                row_start = int(str_loc[0])
                col_start = int(str_loc[1])
            elif num_line == 2:
                str_loc = line.split(",")
                row_goal = int(str_loc[0])
                col_goal = int(str_loc[1])
            elif num_line == 3:
                size = int(line)
            else:
                str_loc = line.split(",")
                for l in str_loc:
                    costs.append[int(l)]

            num_line += 1
        start = size * row_start + col_start
        goal = size * row_goal + col_goal
        return graph(start, goal, size, costs, algo)




class graph:

    def __init__(self, start_loc, goal_loc, size, costs, algorithm):
        col = 0
        row = 0
        self.nodes = []
        while row < size:
           while col < size:
               location = row*size+col
               cost = costs[location]
               self.nodes.append(node(location, cost))
               col+=1
           ++row

        for n in self.nodes:
            self.addNeighbors(self, n, size, nodes)
        self.start = self.nodes[start_loc]
        self.goal = self.nodes[goal_loc]
        self.algorithm = algorithm


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