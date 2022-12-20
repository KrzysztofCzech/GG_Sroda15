from re import A
import unittest
from draw import draw_graph
import networkx as nx
from classes import Node
from productions.p9 import p9


class P9Test(unittest.TestCase):
    def test_P9(self):

        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.5, y=0.5).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=3, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
        ])
        graph.add_edges_from([
            (0, 1),
            (0, 2),
            (0, 3),

            (1, 2),
            (1, 3),
            (2, 3),
        ])
        p9(graph, 0)

        target_graph = {
            0: {'label': 'I', 'x': 0.5, 'y': 0.5, 'level': 0},
            1: {'label': 'E', 'x': 0.0, 'y': 1.0, 'level': 0},
            2: {'label': 'E', 'x': 0.0, 'y': 0.0, 'level': 0},
            3: {'label': 'E', 'x': 1.0, 'y': 0.0, 'level': 0},
            4: {'label': 'I', 'x': 0.3333333333333333, 'y': 0.3333333333333333, 'level': 1},
            5: {'label': 'E', 'x': 0.0, 'y': 1.0, 'level': 1},
            6: {'label': 'E', 'x': 0.0, 'y': 0.0, 'level': 1},
            7: {'label': 'E', 'x': 1.0, 'y': 0.0, 'level': 1}
        }

        draw_graph(graph, name='t9_result')

        self.assertEqual(list(graph.nodes), list(range(0, 8)))
        self.assertEqual(graph._node, target_graph)
