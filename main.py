def main():
    file = open("input4.txt", "r")
    graph = GraphFactory().create_graph(file)

    print(graph.start.location)
    print(graph.goal.location)



if __name__ == "__main__":
    main()