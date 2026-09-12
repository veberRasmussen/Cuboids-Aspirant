from config import COLORS, ColourMap, Colouring
from common.coloring_engine.satisfiability.satisfiability import (
    satisfiability_from_graph
)

import networkx as nx


def colour_graph(
        graph: nx.Graph,
        minimal_attempt: int = 1
) -> Colouring:

    nodes = list(graph.nodes())

    node_index = {
        node: i
        for i, node in enumerate(nodes)
    }

    chromatic_number = minimal_attempt

    sat_attempt = satisfiability_from_graph(
        graph,
        node_index,
        chromatic_number
    )

    while not sat_attempt[0]:
        chromatic_number += 1

        sat_attempt = satisfiability_from_graph(
            graph,
            node_index,
            chromatic_number
        )

    model = set(sat_attempt[1])
    number_of_nodes = len(nodes)

    colour_map: ColourMap = {}

    for node, i in node_index.items():

        for colour in range(chromatic_number):

            variable = i + 1 + number_of_nodes * colour

            if variable in model:
                colour_map[node] = COLORS[colour]
                break

    return chromatic_number, colour_map