from config import Building, Colouring
from common.graphs.graph_from_building import graph_from_building
from common.coloring_engine.satisfiability.colour_graph import colour_graph

def colour_building(
        building: Building,
        minimal_attempt: int = 1
) -> Colouring:
    return colour_graph(graph_from_building(building), minimal_attempt)