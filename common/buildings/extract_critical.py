from config import Building
from common.coloring_engine.satisfiability.colour_building import colour_building
from common.coloring_engine.satisfiability.colour_graph import colour_graph
from common.graphs.graph_from_building import graph_from_building

import networkx as nx
import itertools

def extract_critical(
        building: Building
) -> Building:

    building_list = list(building)
    n_bricks = len(building_list)

    chrom = colour_building(building_list, 1)[0]

    # Iterate backwards to safely remove bricks
    for i in range(n_bricks - 1, -1, -1):
        candidate_building = building_list[:i] + building_list[i + 1:]
        chrom_temp = colour_building(candidate_building, chrom - 1)[0]

        if chrom_temp == chrom:
            # Brick is insignificant, remove it
            building_list = candidate_building

    return tuple(building_list)


def extract_critical_fast(
        building: Building
) -> Building:

    building_list = list(building)
    graph = graph_from_building(building_list)

    # Compute chromatic number once
    chrom = colour_graph(graph, 1)[0]

    # Find maximum cliques
    cliques = list(nx.find_cliques(graph))
    max_clique_size = max(len(c) for c in cliques)
    max_cliques = [c for c in cliques if len(c) == max_clique_size]

    # Keep only nodes that belong to at least one maximum clique
    significant_nodes = set(itertools.chain.from_iterable(max_cliques))
    new_building = [brick for i, brick in enumerate(building_list) if i in significant_nodes]

    return tuple(new_building)


def extract_critical_combined(building: Building) -> Building:
    fast_filtered = extract_critical_fast(building)
    refined = extract_critical(fast_filtered)
    return refined