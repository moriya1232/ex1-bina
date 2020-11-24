from graph import *
from IDS import *
from UCS import *
from A_star import *
from IDA_star import *


def main():
    # open the file
    file = open("input.txt", "r")
    # create the graph by graph_factory
    graph = GraphFactory().create_graph(file)
    # find the solution
    res, num_nodes = find_solution(graph)
    output_file = open("output.txt", "w+")
    # write the solution
    output_file.write(write_solution(res, num_nodes))

    # close the files
    file.close()
    output_file.close()


def find_solution(graph):
    # check which algorithm to use.
    if (graph.start == graph.goal):
        return [graph.start, ""], 0
    if graph.algorithm == "IDS":
        return ids(graph)
    elif graph.algorithm == "UCS":
        return ucs(graph)
    elif graph.algorithm == "ASTAR":
        return a_star(graph)
    elif graph.algorithm == "IDASTAR":
        return ida_star(graph)
    else:
        return None, None


if __name__ == "__main__":
    main()
