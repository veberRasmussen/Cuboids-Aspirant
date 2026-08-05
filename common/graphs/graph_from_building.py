from config import TOUCHING, Building
from common.bricks.touch_type import touch_type


import networkx as nx  # Graph Package
import itertools

def graph_from_building(
        building: Building
) -> nx.Graph:

    building_list = list(building)  # convert set/tuple to list for indexing
    n_bricks = len(building_list)

    graph = nx.Graph()

    # Add a node for each brick
    graph.add_nodes_from(range(n_bricks))

    # Add an edge if two bricks touch
    for i, j in itertools.combinations(range(n_bricks), 2):
        if touch_type(building_list[i], building_list[j]) == TOUCHING:
            graph.add_edge(i, j)

    return graph