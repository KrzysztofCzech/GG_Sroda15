import unittest
import networkx as nx
from classes import Node
from productions.p6 import p6


class P6Test(unittest.TestCase):
    def test_no_production(self):
        graph = nx.Graph()
        graph.add_nodes_from([Node(0, label='El', x=0, y=0).graph_adapter()])
        self.assertRaises(IndexError, lambda: p6(graph, 0))

        self.assertEqual(list(graph.nodes), [0])
        self.assertEqual(graph._node, {0: {'label': 'El', "level": 0, 'x': 0, 'y': 0}})

    def test_production_success(self):
        graph = nx.Graph()
        graph.add_nodes_from([
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

        graph.add_edges_from([
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
        
        p6(graph, 0)
        
        self.assertEqual(len(list(graph.nodes)), 11)
        
        self.assertTrue(graph.has_edge(0, 4))
        self.assertTrue(graph.has_edge(0, 5))
        self.assertTrue(graph.has_edge(2, 10))
        self.assertTrue(graph.has_edge(2, 9))
        
        self.assertTrue(graph.has_edge(9, 7))
        self.assertTrue(graph.has_edge(9, 11))
        self.assertTrue(graph.has_edge(10, 7))
        self.assertTrue(graph.has_edge(10, 13))
        
        self.assertTrue(graph.has_edge(4, 11))
        self.assertTrue(graph.has_edge(4, 7))
        self.assertTrue(graph.has_edge(5, 7))
        self.assertTrue(graph.has_edge(5, 13))
        
        self.assertTrue(graph.has_edge(11, 7))
        self.assertTrue(graph.has_edge(11, 4))
        self.assertTrue(graph.has_edge(11, 9))
        
        self.assertTrue(graph.has_edge(13, 7))
        self.assertTrue(graph.has_edge(13, 5))
        self.assertTrue(graph.has_edge(13, 10))

    def test_production_success_with_lonely_nodes(self):
        graph = nx.Graph()
        graph.add_nodes_from([
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
            
            Node(id=0 + 14, label="L", level=0 + 1, x=20.0, y=1.0).graph_adapter(),
            Node(id=0 + 15, label="L", level=0 + 1, x=21.0, y=1.0).graph_adapter(),
            Node(id=0 + 16, label="L", level=0 + 1, x=22.0, y=1.0).graph_adapter(),
            
        ])

        graph.add_edges_from([
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

            (0 + 6, 0 + 14),
            (0 + 12, 0 + 15),
            (0 + 8, 0 + 16),
        ])

        p6(graph, 0)

        self.assertEqual(len(list(graph.nodes)), 14)

        self.assertTrue(graph.has_edge(0, 4))
        self.assertTrue(graph.has_edge(0, 5))
        self.assertTrue(graph.has_edge(2, 10))
        self.assertTrue(graph.has_edge(2, 9))

        self.assertTrue(graph.has_edge(9, 7))
        self.assertTrue(graph.has_edge(9, 11))
        self.assertTrue(graph.has_edge(10, 7))
        self.assertTrue(graph.has_edge(10, 13))

        self.assertTrue(graph.has_edge(4, 11))
        self.assertTrue(graph.has_edge(4, 7))
        self.assertTrue(graph.has_edge(5, 7))
        self.assertTrue(graph.has_edge(5, 13))

        self.assertTrue(graph.has_edge(11, 7))
        self.assertTrue(graph.has_edge(11, 4))
        self.assertTrue(graph.has_edge(11, 9))

        self.assertTrue(graph.has_edge(13, 7))
        self.assertTrue(graph.has_edge(13, 5))
        self.assertTrue(graph.has_edge(13, 10))
        
        self.assertTrue(graph.has_edge(11, 14))
        self.assertTrue(graph.has_edge(7, 15))
        self.assertTrue(graph.has_edge(13, 16))

    def test_production_wrong_pos(self):
        graph = nx.Graph()
        graph.add_nodes_from([
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
            Node(id=0 + 12, label="E", level=0 + 1, x=0.51, y=0.5).graph_adapter(),
            Node(id=0 + 13, label="E", level=0 + 1, x=1.0, y=1.0).graph_adapter(),
        ])

        graph.add_edges_from([
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

        graph_copy = graph.copy()
        
        p6(graph, 0)

        self.assertEqual(len(list(graph.nodes)), 14)

        for node in graph_copy.nodes:
            self.assertTrue(graph.has_node(node))
            
        for key, value in graph_copy.edges.items():
            self.assertTrue(graph.has_edge(key[0], key[1]))

    def test_production_wrong_mid_pos(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="i", level=0, x=0.5, y=1.0).graph_adapter(),
            Node(id=0 + 2, label="i", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=0 + 1, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=0 + 3, label="E", level=0, x=1.0, y=1.0).graph_adapter(),

            Node(id=0 + 4, label="I", level=0 + 1, x=0.33, y=1.33).graph_adapter(),
            Node(id=0 + 5, label="I", level=0 + 1, x=0.66, y=1.33).graph_adapter(),
            Node(id=0 + 6, label="E", level=0 + 1, x=0.0, y=0.0).graph_adapter(),
            Node(id=0 + 7, label="E", level=0 + 1, x=0.6, y=0.6).graph_adapter(),
            Node(id=0 + 8, label="E", level=0 + 1, x=1.0, y=1.0).graph_adapter(),

            Node(id=0 + 9, label="I", level=0 + 1, x=0.33, y=-0.33).graph_adapter(),
            Node(id=0 + 10, label="I", level=0 + 1, x=0.66, y=-0.33).graph_adapter(),
            Node(id=0 + 11, label="E", level=0 + 1, x=0.0, y=0.0).graph_adapter(),
            Node(id=0 + 12, label="E", level=0 + 1, x=0.6, y=0.6).graph_adapter(),
            Node(id=0 + 13, label="E", level=0 + 1, x=1.0, y=1.0).graph_adapter(),
        ])

        graph.add_edges_from([
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

        graph_copy = graph.copy()

        p6(graph, 0)

        self.assertEqual(len(list(graph.nodes)), 14)

        for node in graph_copy.nodes:
            self.assertTrue(graph.has_node(node))

        for key, value in graph_copy.edges.items():
            self.assertTrue(graph.has_edge(key[0], key[1]))
