import networkx as nx

from classes import Node
from draw import draw_graph
from productions.p5 import p5
from productions.p6 import p6


def makeP5():
    graph = nx.Graph()

    graph.add_nodes_from([
        Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
        Node(id=0 + 1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
        Node(id=0 + 2, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
        Node(id=0 + 3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
        Node(id=0 + 4, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
        Node(id=0 + 5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
        Node(id=0 + 6, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
    ])

    graph.add_edges_from([
        (0, 1),
        (0, 3),
        (0, 5),

        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 1),
    ])

    draw_graph(graph, name='production5_1')
    p5(graph, 0)
    draw_graph(graph, name='production5_2')


def makeP6():
    graph2 = nx.Graph()
    graph2.add_nodes_from([
        Node(id=0, label="i", level=0, x=0.5, y=1.0).graph_adapter(),
        Node(id=0 + 2, label="i", level=0, x=1.0, y=0.0).graph_adapter(),
        Node(id=0 + 1, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
        Node(id=0 + 3, label="E", level=0, x=1.0, y=1.0).graph_adapter(),

        Node(id=0 + 4, label="I", level=0 + 1, x=0.33, y=1.33).graph_adapter(),
        Node(id=0 + 5, label="I", level=0 + 1, x=0.66, y=1.33).graph_adapter(),
        Node(id=0 + 6, label="E", level=0 + 1, x=0.0, y=0.0).graph_adapter(),
        Node(id=0 + 7, label="E", level=0 + 1, x=0.5, y=0.5).graph_adapter(),
        Node(id=0 + 8, label="E", level=0 + 1, x=1.0, y=1.0).graph_adapter(),

        Node(id=0 + 9, label="I", level=0 + 1, x=0.33, y=-0.33).graph_adapter(),
        Node(id=0 + 10, label="I", level=0 + 1, x=0.66, y=-0.33).graph_adapter(),
        Node(id=0 + 11, label="E", level=0 + 1, x=0.0, y=0.0).graph_adapter(),
        Node(id=0 + 12, label="E", level=0 + 1, x=0.5, y=0.5).graph_adapter(),
        Node(id=0 + 13, label="E", level=0 + 1, x=1.0, y=1.0).graph_adapter(),
    ])

    graph2.add_edges_from([
        (0, 0 + 1),
        (0, 0 + 3),
        (0 + 2, 0 + 1),
        (0 + 2, 0 + 3),
        (0 + 1, 0 + 3),

        (0, 0 + 4),
        (0, 0 + 5),

        (0 + 2, 0 + 9),
        (0 + 2, 0 + 10),

        (0 + 4, 0 + 6),
        (0 + 4, 0 + 7),

        (0 + 5, 0 + 7),
        (0 + 5, 0 + 8),

        (0 + 6, 0 + 7),
        (0 + 7, 0 + 8),

        (0 + 9, 0 + 11),
        (0 + 9, 0 + 12),

        (0 + 10, 0 + 12),
        (0 + 10, 0 + 13),

        (0 + 11, 0 + 12),
        (0 + 12, 0 + 13),
    ])

    draw_graph(graph2, name='production6_1')
    p6(graph2, 0)
    draw_graph(graph2, name='production6_2')


if __name__ == '__main__':
    # makeP6()
    makeP5()

    # print(graph._node)
