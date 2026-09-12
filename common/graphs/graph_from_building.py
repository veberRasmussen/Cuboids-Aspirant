from config import TOUCHING, Building
from common.bricks.touch_type import touch_type


import networkx as nx  # Graph Package
import itertools

def graph_from_building(
        building: Building
) -> nx.Graph:

    graph = nx.Graph()
    graph.add_nodes_from(building)

    for brick_1, brick_2 in itertools.combinations(building, 2):
        if touch_type(brick_1, brick_2) == TOUCHING:
            graph.add_edge(brick_1, brick_2)

    return graph