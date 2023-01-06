import networkx as nx
from draw import draw_graph
from productions.p12 import p12
from productions.p1 import p1

from pprint import pprint

from classes import Node

if __name__ == '__main__':

    graph = nx.Graph()
    graph.add_nodes_from([
        Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
        Node(1, label='E', x=90, y=90, level=1).graph_adapter(),
        Node(2, label='i', x=0, y=90, level=1).graph_adapter(),
        Node(3, label='i', x=90, y=0, level=1).graph_adapter(),
        Node(4, label='E', x=0, y=0, level=2).graph_adapter(),
        Node(5, label='E', x=90, y=90, level=2).graph_adapter(),
        Node(6, label='I', x=00, y=90, level=2).graph_adapter(),
        Node(7, label='E', x=0, y=0, level=2).graph_adapter(),
        Node(8, label='E', x=90, y=90, level=2).graph_adapter(),
        Node(9, label='I', x=90, y=0, level=2).graph_adapter(),
    ])
    graph.add_edges_from([
        (0, 1),
        (1, 2),
        (2, 0),
        (0, 3),
        (1, 3),

        (4, 5),
        (5, 6),
        (6, 4),

        (7, 8),
        (8, 9),
        (9, 7),

        (2, 6),
        (3, 9),
    ])
    draw_graph(graph, name='prod12-0', font_size=9,
               with_coords=True, level_offset=150)
    p12(graph, 1)
    # pprint(graph.nodes(data=True))
    draw_graph(graph, name='prod12-1', font_size=9,
               with_coords=True, level_offset=150)
