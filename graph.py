class TextCares(object):

    @staticmethod
    def remove_enters(lines):
        counter = 0
        for line in lines:
            if line[-1] == '\n':
                lines[counter] = line[:-1]

            counter += 1
        return lines


class GraphFactory(object):
    @staticmethod
    def create_graph(file):
        # graph factory need to be can create graph.
        algo = ""
        row_start = 0
        col_start = 0
        row_goal = 0
        col_goal = 0
        size = 0
        costs = []
        lines = file.readlines()
        lines = TextCares.remove_enters(lines)
        num_line = 0
        for line in lines:
            if num_line == 0:    # first line = algorithm
                algo = line
            elif num_line == 1:        # second line = start node
                str_loc = line.split(",")
                row_start = int(str_loc[0])
                col_start = int(str_loc[1])
            elif num_line == 2:           # third line = goal node
                str_loc = line.split(",")
                row_goal = int(str_loc[0])
                col_goal = int(str_loc[1])
            elif num_line == 3:          # forth line = size of the matrix
                size = int(line)
            else:                       # all the lines that left = the matrix of the problem
                str_loc = line.split(",")
                for l in str_loc:
                    costs.append(int(l.strip(" \n\t")))

            num_line += 1
        start = size * row_start + col_start
        goal = size * row_goal + col_goal
        return Graph(start, goal, size, costs, algo)       # create the graph and return it


def write_solution(graph, num_nodes):       # write the solution by the format that we asked for.
    if graph == None or graph.goal.father is None:
        return "no path"
    g = 0
    solution_str = ""
    solution_nodes_temp = []
    solution_nodes = []
    cur_node = graph.goal
    while cur_node != graph.start:
        solution_nodes_temp.append(cur_node)
        cur_node = cur_node.father
    solution_nodes_temp.append(cur_node)      # append the start node
    for i in solution_nodes_temp.__reversed__():
        solution_nodes.append(i)
    for i in range(len(solution_nodes)):
        if i == len(solution_nodes) - 1:     #came to goal
            break
        g += solution_nodes[i + 1].cost
        solution_str += check_where_to_go(graph, solution_nodes[i], solution_nodes[i + 1])
        solution_str += "-"
    solution_str = solution_str[0:-1]
    res = solution_str + " " + str(g) + " " + str(num_nodes)
    return res

def check_where_to_go(graph, node, next_node):
    size= graph.size
    location = node.location
    if location - size == next_node.location:
        return "U"
    elif location + 1 == next_node.location:
        return "R"
    elif location - 1 == next_node.location:
        return "L"
    elif location + size == next_node.location:
        return "D"
    elif location - size - 1 == next_node.location:
        return "LU"
    elif location - size + 1 == next_node.location:
        return "RU"
    elif location + size - 1 == next_node.location:
        return "LD"
    elif location + size + 1 == next_node.location:
        return "RD"


class Graph:             # can called problem too.
    def __init__(self, start_loc, goal_loc, size, costs, algorithm):
        self.size = size
        col = 0
        row = 0
        self.nodes = []
        while row < size:
            while col < size:
                location = row * size + col
                cost = costs[location]
                self.nodes.append(Node(location, cost))
                col += 1
            row += 1
            col = 0
        for n in self.nodes:
            self.add_neighbors(n, size, self.nodes)
        self.start = self.nodes[start_loc]
        self.goal = self.nodes[goal_loc]
        self.algorithm = algorithm

    def remove_fathers(self):
        for i in self.nodes:
            i.father = None

    def remove_depthes(self):
        for i in self.nodes:
            i.depth = None


    @staticmethod
    def add_neighbors(node, size, nodes):        # add the neighbors to any node
        location = node.location
        up_n = location - size
        down_n = location + size
        right_n = location + 1
        left_n = location - 1
        source_neighbors = [right_n, down_n + 1, down_n, down_n - 1, left_n,
                            up_n - 1, up_n, up_n + 1]
        up = [up_n - 1, up_n, up_n + 1]
        down = [down_n + 1, down_n, down_n - 1]
        left = [down_n - 1, left_n, up_n - 1]
        right = [right_n, down_n + 1, up_n + 1]

        # first column
        if location % size == 0:
            for l in left:
                source_neighbors.remove(l)
        # latest column
        elif location % size == size - 1:
            for r in right:
                source_neighbors.remove(r)
        temp_neighbors = source_neighbors.copy()
        for n in temp_neighbors:
            if n < 0 or n >= size * size:
                source_neighbors.remove(n)

        # check if up is -1
        if up_n - 1 in source_neighbors and nodes[up_n].cost == -1:
            for u in up:
                if u in source_neighbors:
                    source_neighbors.remove(u)
        # check if down is -1
        if down_n in source_neighbors and nodes[down_n].cost == -1:
            for d in down:
                if d in source_neighbors:
                    source_neighbors.remove(d)
        # check if left is -1
        if left_n in source_neighbors and nodes[left_n].cost == -1:
            for l in left:
                if l in source_neighbors:
                    source_neighbors.remove(l)
        # check if right is -1
        if right_n in source_neighbors and nodes[right_n].cost == -1:
            for r in right:
                if r in source_neighbors:
                    source_neighbors.remove(r)
        # create neighbors
        for n in source_neighbors:
            if nodes[n].cost != -1:
                node.add_neighbor(nodes[n])


class Node:
    def __init__(self, location, cost):
        self.location = location
        self.cost = cost
        self.neighbors = []
        self.g = 0
        self.father = None
        self.depth = None

    def add_neighbor(self, node):
        self.neighbors.append(node)
