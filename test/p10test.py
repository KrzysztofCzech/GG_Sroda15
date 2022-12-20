from re import A
import unittest
from draw import draw_graph
import networkx as nx
from classes import Node
from productions.p10 import p10


class P10Test(unittest.TestCase):
    def test_P10(self):
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

        p10(graph, 0)

        draw_graph(graph, name='t10_result')

        target_graph = {
            0: {'label': 'i', 'x': 1, 'y': 2, 'level': 0},
            1: {'label': 'i', 'x': 2, 'y': 1, 'level': 0},
            2: {'label': 'E', 'x': 1, 'y': 1, 'level': 0},
            3: {'label': 'E', 'x': 2, 'y': 2, 'level': 0},
            4: {'label': 'I', 'x': 1, 'y': 1.3, 'level': 1},
            5: {'label': 'I', 'x': 1.5, 'y': 2, 'level': 1},
            6: {'label': 'I', 'x': 2, 'y': 1, 'level': 1},
            7: {'label': 'E', 'x': 1.0, 'y': 1.0, 'level': 1},
            8: {'label': 'E', 'x': 1.5, 'y': 1.5, 'level': 1},
            9: {'label': 'E', 'x': 2.0, 'y': 2.0, 'level': 1}
        }

        self.assertEqual(list(graph.nodes), list(range(0, 10)))
        self.assertEqual(graph._node, target_graph)
