from config import ColourMap

import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph: nx.Graph, color_map:ColourMap):
    nx.draw(graph, node_color=color_map, with_labels=True)
    plt.show()


