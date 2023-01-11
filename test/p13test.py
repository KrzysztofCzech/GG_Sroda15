import unittest
import networkx as nx
from classes import Node
from draw import draw_graph
from productions.p13 import p13
from pprint import pprint


class p13Test(unittest.TestCase):
    def test_production_is_applied(self):
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
            Node(8, label='I', x=90, y=0, level=2).graph_adapter(),
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

            (7, 5),
            (8, 5),
            (8, 7),

            (2, 6),
            (3, 8),
        ])
        draw_graph(graph, name='prod13_1-test_0', level_offset=150)

        result = p13(graph, 1)
        draw_graph(graph, name='prod13_1-test_1', level_offset=150)

        # pprint(graph._node)

        self.assertTrue(result)
        self.assertEqual(8, graph.number_of_nodes())
        self.assertEqual(12, graph.number_of_edges())

        # pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 90},
            2: {'label': 'i', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'i', 'level': 1, 'x': 90, 'y': 0},
            4: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            5: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            6: {'label': 'I', 'level': 2, 'x': 0, 'y': 90},
            8: {'label': 'I', 'level': 2, 'x': 90, 'y': 0}
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1), (0, 2), (0, 3), (1, 2), (1, 3),
            (2, 6), (3, 8), (4, 5), (4, 6), (4, 8), (5, 6),  (5, 8)
        ]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_as_subgraph_is_applied(self):
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
            Node(8, label='I', x=90, y=0, level=2).graph_adapter(),
            # More added
            Node(9, label='E', x=40, y=250, level=2).graph_adapter(),
            Node(10, label='E', x=80, y=220, level=2).graph_adapter(),
            Node(11, label='E', x=200, y=0, level=2).graph_adapter(),
            Node(12, label='E', x=400, y=45, level=2).graph_adapter(),
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

            (7, 5),
            (8, 5),
            (8, 7),

            (2, 6),
            (3, 8),

            # More added
            (9, 7),
            (9, 4),
            (4, 10),
            (7, 11),
            (11, 10),
            (12, 10),
            (12, 7),
        ])
        draw_graph(graph, name='prod13_2-test_0', level_offset=150)

        result = p13(graph, 1)
        draw_graph(graph, name='prod13_2-test_1', level_offset=150)

        pprint(graph._node)

        self.assertTrue(result)
        self.assertEqual(12, graph.number_of_nodes())
        self.assertEqual(18, graph.number_of_edges())

        # pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 90},
            2: {'label': 'i', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'i', 'level': 1, 'x': 90, 'y': 0},
            4: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            5: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            6: {'label': 'I', 'level': 2, 'x': 0, 'y': 90},
            8: {'label': 'I', 'level': 2, 'x': 90, 'y': 0},
            9: {'label': 'E', 'level': 2, 'x': 40, 'y': 250},
            10: {'label': 'E', 'level': 2, 'x': 80, 'y': 220},
            11: {'label': 'E', 'level': 2, 'x': 200, 'y': 0},
            12: {'label': 'E', 'level': 2, 'x': 400, 'y': 45}
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 6),
                          (3, 8), (4, 5), (4, 6), (4, 9), (4, 10), (4, 11), (4, 12),
                          (4, 8), (5, 6), (5, 8), (10, 11), (10, 12)
                          ]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_without_one_node_removed(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            # Node 0 removed
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
            (1, 2),
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
        draw_graph(graph, name='prod13_3-test_0', level_offset=150)

        result = p13(graph, 1)
        draw_graph(graph, name='prod13_3-test_1', level_offset=150)

        # pprint(graph._node)

        self.assertFalse(result)
        self.assertEqual(9, graph.number_of_nodes())
        self.assertEqual(10, graph.number_of_edges())

        # pprint(graph.edges())

        expected_nodes = {
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 90},
            2: {'label': 'i', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'i', 'level': 1, 'x': 90, 'y': 0},
            4: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            5: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            6: {'label': 'I', 'level': 2, 'x': 0, 'y': 90},
            7: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            8: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            9: {'label': 'I', 'level': 2, 'x': 90, 'y': 0}
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(1, 2), (1, 3), (2, 6), (3, 9), (4, 5), (4, 6), (5, 6), (7, 8), (7, 9), (8, 9)
                          ]

        self.assertEqual(expected_edges, list(graph.edges()))
