from graph import *
from IDS import *
from UCS import *
from A_star import *

def main():
    file = open("input5.txt", "r")
    graph = GraphFactory().create_graph(file)
    res = ids(graph)
    if res is not None:
        for node in res:
            print(node.location)
    else:
        print("no path")


if __name__ == "__main__":
    main()
