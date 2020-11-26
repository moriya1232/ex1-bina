from graph import *
from IDS import *
from UCS import *
from A_star import *
from IDA_star import *
import math


def main():
    # open the file
    file = open("input.txt", "r")
    # create the graph by graph_factory
    graph = GraphFactory().create_graph(file)
    # find the solution
    graph, num_nodes = find_solution(graph)
    output_file = open("output.txt", "w+")
    # write the solution
    output_file.write(write_solution(graph, num_nodes))
    # remove it
    print(write_solution(graph, num_nodes))
    # close the files
    file.close()
    output_file.close()


def find_solution(graph):
    def chebyshev(node):
        loc_goal = graph.goal.location
        row_goal = math.floor(loc_goal / graph.size)
        col_goal = loc_goal % graph.size
        loc_cur = node.location
        row_cur = math.floor(loc_cur / graph.size)
        col_cur = loc_cur % graph.size
        dx = abs(col_goal - col_cur)
        dy = abs(row_goal - row_cur)
        return (dx + dy) - min(dx, dy)
    # check which algorithm to use.
    if (graph.start == graph.goal):
        return [graph.start, ""], 0
    if graph.algorithm == "IDS":
        return ids(graph)
    elif graph.algorithm == "UCS":
        return ucs(graph)
    elif graph.algorithm == "ASTAR":
        return a_star(graph, chebyshev)
    elif graph.algorithm == "IDASTAR":
        return ida_star(graph, chebyshev)
    else:
        return None, None


if __name__ == "__main__":
    main()
