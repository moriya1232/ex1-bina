from PriorityQueue import *
from BestFirstSearch import *


# UCS algorithm is type of best first search algorithm
def ucs(graph):
    # dont have huristic function
    def h(node):
        return 0
    return best_first_search(graph, h)