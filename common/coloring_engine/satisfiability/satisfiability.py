import networkx as nx
from pysat.solvers import Solver


def satisfiability_from_graph(
        graph: nx.Graph,
        node_index: dict,
        number_of_colors: int
):
    number_of_nodes = len(node_index)

    with Solver() as sat:

        # Every node gets at least one colour
        for i in range(number_of_nodes):
            sat.add_clause([
                i + 1 + number_of_nodes * colour
                for colour in range(number_of_colors)
            ])

        # Connected nodes cannot have the same colour
        for brick_1, brick_2 in graph.edges():

            i = node_index[brick_1]
            j = node_index[brick_2]

            for colour in range(number_of_colors):

                v1 = i + 1 + number_of_nodes * colour
                v2 = j + 1 + number_of_nodes * colour

                sat.add_clause([-v1, -v2])

        return sat.solve(), sat.get_model()