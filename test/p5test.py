import unittest
import networkx as nx
from classes import Node
from productions.p5 import p5


class P5Test(unittest.TestCase):
    def test_no_production(self):
        graph = nx.Graph()
        graph.add_nodes_from([Node(0, label='El', x=0, y=0).graph_adapter()])
        self.assertRaises(IndexError, lambda: p5(graph, 0))

        self.assertEqual(list(graph.nodes), [0])
        self.assertEqual(graph._node, {0: {'label': 'El', "level": 0, 'x': 0, 'y': 0}})

    def test_production_success(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=6, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
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

        p5(graph, 0)

        self.assertEqual(len(list(graph.nodes)), 17)

        self.assertTrue(graph.has_edge(0, 7))
        self.assertTrue(graph.has_edge(0, 8))
        self.assertTrue(graph.has_edge(0, 9))
        self.assertTrue(graph.has_edge(0, 10))

        self.assertTrue(graph.has_edge(7, 11))
        self.assertTrue(graph.has_edge(7, 12))
        self.assertTrue(graph.has_edge(7, 16))

        self.assertTrue(graph.has_edge(8, 12))
        self.assertTrue(graph.has_edge(8, 13))
        self.assertTrue(graph.has_edge(8, 16))

        self.assertTrue(graph.has_edge(9, 13))
        self.assertTrue(graph.has_edge(9, 14))
        self.assertTrue(graph.has_edge(9, 16))

        self.assertTrue(graph.has_edge(10, 14))
        self.assertTrue(graph.has_edge(10, 15))
        self.assertTrue(graph.has_edge(10, 16))

        self.assertTrue(graph.has_edge(11, 12))
        self.assertTrue(graph.has_edge(12, 13))
        self.assertTrue(graph.has_edge(13, 14))
        self.assertTrue(graph.has_edge(14, 15))
        self.assertTrue(graph.has_edge(15, 16))
        self.assertTrue(graph.has_edge(16, 11))

    def test_production_success_with_lonely_nodes(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=6, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
            Node(id=7, label="L", level=0, x=1.0, y=1.0).graph_adapter(),
            Node(id=8, label="L", level=0, x=1.5, y=1.5).graph_adapter(),
            Node(id=9, label="L", level=0, x=2.5, y=2.5).graph_adapter(),
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

        p5(graph, 0)

        self.assertEqual(len(list(graph.nodes)), 20)

        self.assertTrue(graph.has_edge(0, 10))
        self.assertTrue(graph.has_edge(0, 11))
        self.assertTrue(graph.has_edge(0, 12))
        self.assertTrue(graph.has_edge(0, 13))

        self.assertTrue(graph.has_edge(11, 15))
        self.assertTrue(graph.has_edge(7 + 3, 12 + 3))
        self.assertTrue(graph.has_edge(7 + 3, 16 + 3))

        self.assertTrue(graph.has_edge(8 + 3, 12 + 3))
        self.assertTrue(graph.has_edge(8 + 3, 13 + 3))
        self.assertTrue(graph.has_edge(8 + 3, 16 + 3))

        self.assertTrue(graph.has_edge(9 + 3, 13 + 3))
        self.assertTrue(graph.has_edge(9 + 3, 14 + 3))
        self.assertTrue(graph.has_edge(9 + 3, 16 + 3))

        self.assertTrue(graph.has_edge(10 + 3, 14 + 3))
        self.assertTrue(graph.has_edge(10 + 3, 15 + 3))
        self.assertTrue(graph.has_edge(10 + 3, 16 + 3))

        self.assertTrue(graph.has_edge(11 + 3, 12 + 3))
        self.assertTrue(graph.has_edge(12 + 3, 13 + 3))
        self.assertTrue(graph.has_edge(13 + 3, 14 + 3))
        self.assertTrue(graph.has_edge(14 + 3, 15 + 3))
        self.assertTrue(graph.has_edge(15 + 3, 16 + 3))
        self.assertTrue(graph.has_edge(16 + 3, 11 + 3))

    def test_production_wrong_edge(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=6, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
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
            # (6, 1),
        ])

        self.assertRaises(IndexError, lambda: p5(graph, 0))
        self.assertEqual(len(list(graph.nodes)), 7)

    def test_production_wrong_node(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            # Node(id=6, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1),
            (0, 3),
            (0, 5),

            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            # (5, 6),
            # (6, 1),
        ])

        self.assertRaises(IndexError, lambda: p5(graph, 0))
        self.assertEqual(len(list(graph.nodes)), 6)
