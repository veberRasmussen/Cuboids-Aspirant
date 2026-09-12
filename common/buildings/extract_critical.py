from config import Building
from common.coloring_engine.satisfiability.colour_building import colour_building
from common.coloring_engine.satisfiability.colour_graph import colour_graph
from common.graphs.graph_from_building import graph_from_building

import networkx as nx
import itertools


def extract_critical(
        building: Building
) -> Building:

    chrom = colour_building(building, 1)[0]

    for brick in building.copy():
        candidate_building = building - {brick}
        chrom_temp = colour_building(candidate_building, chrom - 1)[0]

        if chrom_temp == chrom:
            # Brick is insignificant, remove it
            building = candidate_building

    return building


def extract_critical_fast(
        building: Building
) -> Building:

    graph = graph_from_building(building)

    # Compute chromatic number once
    chrom = colour_graph(graph, 1)[0]

    # Find maximum cliques
    cliques = list(nx.find_cliques(graph))
    max_clique_size = max(len(c) for c in cliques)
    max_cliques = [c for c in cliques if len(c) == max_clique_size]

    # Keep only nodes that belong to at least one maximum clique
    significant_nodes = set(itertools.chain.from_iterable(max_cliques))

    return {
        brick
        for brick in building
        if brick in significant_nodes
    }


def extract_critical_combined(
        building: Building
) -> Building:

    fast_filtered = extract_critical_fast(building)
    refined = extract_critical(fast_filtered)

    return refined