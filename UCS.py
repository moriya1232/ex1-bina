from PriorityQueue import *
from BestFirstSearch import *


def ucs(graph):          # UCS algorithm
    def h(node):
        return 0
    return best_first_search(graph, h)