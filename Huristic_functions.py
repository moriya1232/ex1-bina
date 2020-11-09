import math


def h_distance(graph, node):
    loc_goal = graph.goal.location
    row_goal = math.floor(loc_goal / graph.size)
    col_goal = loc_goal % graph.size
    loc_cur = node.location
    row_cur = math.floor(loc_cur / graph.size)
    col_cur = loc_cur % graph.size
    row_gap = abs(row_goal - row_cur)
    col_gap = abs(col_goal - col_cur)
    return math.ceil((row_gap + col_gap)/2)