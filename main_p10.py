import networkx as nx
from draw import draw_graph
from productions.p10 import p10
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
        Node(5, label='E', x=45, y=45, level=2).graph_adapter(),
        Node(6, label='E', x=90, y=90, level=2).graph_adapter(),
        Node(7, label='I', x=00, y=60, level=2).graph_adapter(),
        Node(8, label='I', x=60, y=90, level=2).graph_adapter(),
        Node(9, label='E', x=0, y=0, level=2).graph_adapter(),
        Node(10, label='E', x=90, y=90, level=2).graph_adapter(),
        Node(11, label='I', x=90, y=0, level=2).graph_adapter(),
        Node(12, label='E', x=40, y=250, level=2).graph_adapter(),
        Node(13, label='E', x=80, y=220, level=2).graph_adapter(),
    ])
    graph.add_edges_from([
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),

        (4, 5),
        (5, 6),
        (4, 7),
        (7, 5),
        (8, 5),
        (8, 6),

        (9, 10),
        (9, 11),
        (10, 11),

        (2, 7),
        (2, 8),
        (3, 11),


        (9, 12),
        (10, 13),
    ])
    draw_graph(graph, name='prod10-0', font_size=9,
               with_coords=True, level_offset=150)
    p10(graph, 1)
    # pprint(graph.nodes(data=True))
    draw_graph(graph, name='prod10-1', font_size=9,
               with_coords=True, level_offset=150)
