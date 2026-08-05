import itertools
import networkx as nx
from pysat.solvers import Solver

def satisfiability_from_graph(
        graph: nx.Graph,
        number_of_colors: int
):
    edges = list(graph.edges())
    number_of_nodes: int = graph.number_of_nodes()

    with Solver() as sat:
        # Assign colors to vertices
        for j in range(number_of_nodes):
            sat.add_clause(list(range(j + 1, number_of_nodes * number_of_colors + 1, number_of_nodes)))

        # No two connected vertices have same color
        for e, i in itertools.product(edges, range(number_of_colors)):
            v1 = e[0] + 1 + number_of_nodes * i
            v2 = e[1] + 1 + number_of_nodes * i
            sat.add_clause([-v1, -v2])

        return sat.solve(), sat.get_model()