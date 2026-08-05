from config import COLORS,Colouring
from common.coloring_engine.satisfiability.satisfiability import satisfiability_from_graph

import itertools
import networkx as nx
from pysat.solvers import Solver


def colour_graph(
        graph: nx.Graph,
        minimal_attempt: int = 1
)-> Colouring:
    chromatic_number = minimal_attempt
    n_nodes = graph.number_of_nodes()
    sat_attempt = satisfiability_from_graph(graph, chromatic_number)
    while not sat_attempt[0]:  # loops until expression is satisfiable
        chromatic_number = chromatic_number + 1
        sat_attempt = satisfiability_from_graph(graph, chromatic_number)
    model = sat_attempt[1]  # the model when satisfied
    color_map = []
    for j in range(1, n_nodes + 1):  # this assigns the first possible color to each vertex
        it = j - 1
        number_of_colors = 0
        while model[it] < 0:
            it = it + n_nodes
            number_of_colors = number_of_colors + 1
        color_map.append(COLORS[number_of_colors])
    return chromatic_number, color_map