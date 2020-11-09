from graph import *
from IDS import *

def main():
    file = open("input4.txt", "r")
    graph = GraphFactory().create_graph(file)


    res = ids(graph)
    if res is not None:
        for node in res:
            print(node.location)
    else:
        print("No Solution")


if __name__ == "__main__":
    main()
