import networkx as nx
from draw import draw_graph
from productions.p4 import p4

from classes import Node

if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from([
        Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
        Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
        Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
        Node(3, label='E', x=45, y=45, level=1).graph_adapter(),
        Node(4, label='I', x=30, y=30, level=1).graph_adapter(),
        Node(5, label='E', x=0, y=45, level=1).graph_adapter()
    ])
    graph.add_edges_from([
        (0, 1),
        (1, 3),
        (2, 3),
        (2, 5),
        (5, 0),
        (0, 4),
        (1, 4),
        (2, 4)
    ])

    draw_graph(graph, name='prod4-0')
    p4(graph, 1)
    draw_graph(graph, name='prod4-1')