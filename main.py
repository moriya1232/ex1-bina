from graph import *
from IDS import *
from UCS import *

def main():
    file = open("input2.txt", "r")
    graph = GraphFactory().create_graph(file)
    res = ucs(graph)
    if res is not None:
        for node in res:
            print(node.location)
    else:
        print("No Solution")


if __name__ == "__main__":
    main()
