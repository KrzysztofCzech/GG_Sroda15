import networkx as nx
from draw import draw_graph
from productions.p1 import p1
from productions.p2 import p2
from productions.p9 import p9
from productions.p10 import p10

from classes import Node, Attr_MAP


if __name__ == '__main__':

    graph = nx.Graph()
    graph.add_nodes_from([
        Node(id=0, label="i", level=0, x=1, y=2).graph_adapter(),
        Node(id=1, label="i", level=0, x=2, y=1).graph_adapter(),
        Node(id=2, label="E", level=0, x=1, y=1).graph_adapter(),
        Node(id=3, label="E", level=0, x=2, y=2).graph_adapter(),

        Node(id=4, label="I", level=0+1, x=1, y=1.3).graph_adapter(),
        Node(id=5, label="I", level=0+1, x=1.5, y=2).graph_adapter(),
        Node(id=6, label="I", level=0+1, x=2, y=1).graph_adapter(),

        Node(id=7, label="E", level=0+1, x=1, y=1).graph_adapter(),
        Node(id=8, label="E", level=0+1, x=1.5, y=1.5).graph_adapter(),
        Node(id=9, label="E", level=0+1, x=2, y=2).graph_adapter(),
        Node(id=10, label="E", level=0+1, x=1, y=1).graph_adapter(),
        Node(id=11, label="E", level=0+1, x=2, y=2).graph_adapter(),
    ])

    graph.add_edges_from([
        (0, 2),
        (0, 3),
        (2, 3),
        (1, 2),
        (1, 3),

        (0, 4),
        (0, 5),
        (4, 7),
        (4, 8),
        (7, 8),
        (5, 8),
        (9, 8),
        (5, 9),

        (1, 6),
        (6, 10),
        (6, 11),
        (10, 11),
    ])

    # p1(graph, 0)
    # print(graph._node)
    # p2(graph, 1)
    # p2(graph, 1)
    # p9(graph, 1)

    print(graph.nodes.data())
    draw_graph(graph, name='production1')
    p10(graph, 0)

    print(graph.nodes.data())
    draw_graph(graph, name='production2')
