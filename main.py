from graph import *
from IDS import *
from UCS import *
from A_star import *
from IDA_star import *

def main():
    file = open("input.txt", "r")
    graph = GraphFactory().create_graph(file)
    res = find_solution(graph)
    write_solution(res)


def find_solution(graph):
    if graph.algorithm == "IDS":
        return ids(graph)
    elif graph.algorithm == "UCS":
        return ucs(graph)
    elif graph.algorithm == "A*":
        return a_star(graph)
    elif graph.algorithm == "IDA*":
        return ida_star(graph)
    else:
        return None

if __name__ == "__main__":
    main()

