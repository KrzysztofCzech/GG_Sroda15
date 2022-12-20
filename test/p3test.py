import unittest
import networkx as nx
from classes import Node
from productions.p3 import p3


class P3Test(unittest.TestCase):
    # 2c, 2d, 2e, 4a, 5a, 5d, 5e, 5f
    def test_production_is_applied(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='E', x=45, y=45, level=1).graph_adapter(),
            Node(4, label='I', x=30, y=30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (1, 3),
            (2, 3),
            (2, 0),
            (0, 4),
            (1, 4),
            (2, 4)
        ])

        result = p3(graph, 1)

        self.assertEqual(True, result)
        self.assertEqual(11, graph.number_of_nodes())
        self.assertEqual(20, graph.number_of_edges())

        expected_nodes = {
            0: {'label': 'E', 'x': 0, 'y': 0, 'level': 1},
            1: {'label': 'E', 'x': 90, 'y': 0, 'level': 1},
            2: {'label': 'E', 'x': 0, 'y': 90, 'level': 1},
            3: {'label': 'E', 'x': 45, 'y': 45, 'level': 1},
            4: {'label': 'i', 'x': 30, 'y': 30, 'level': 1},
            5: {'label': 'E', 'x': 0, 'y': 0, 'level': 2},
            6: {'label': 'E', 'x': 90, 'y': 0, 'level': 2},
            7: {'label': 'E', 'x': 0, 'y': 90, 'level': 2},
            8: {'label': 'E', 'x': 45, 'y': 45, 'level': 2},
            9: {'label': 'I', 'x': 45.0, 'y': 15.0, 'level': 2},
            10: {'label': 'I', 'x': 15.0, 'y': 45.0, 'level': 2}
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1), (0, 2), (0, 4),
            (1, 3), (1, 4),
            (2, 3), (2, 4),
            (4, 9), (4, 10),
            (5, 6), (5, 7), (5, 8), (5, 9), (5, 10),
            (6, 8), (6, 9),
            (7, 8), (7, 10),
            (8, 9), (8, 10)
        ]

        self.assertEqual(expected_edges, list(graph.edges()))

    # 1d, 2a, 2b, 5b, 5c
    def test_as_subgraph_is_applied(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='E', x=45, y=45, level=1).graph_adapter(),
            Node(4, label='I', x=30, y=30, level=1).graph_adapter(),
            # added nodes
            Node(-1, label='E', x=0, y=-30, level=1).graph_adapter(),
            Node(-2, label='E', x=0, y=-60, level=1).graph_adapter(),
            Node(-3, label='E', x=0, y=-90, level=1).graph_adapter(),
        ])
        # added few more edges
        graph.add_edges_from([
            (0, 1),
            (1, 3),
            (2, 3),
            (2, 0),
            (0, 4),
            (1, 4),
            (2, 4),
            (0, -1),
            (-1, -2),
            (-2, -3)
        ])

        result = p3(graph, 1)

        self.assertEqual(True, result)
        self.assertEqual(14, graph.number_of_nodes())
        self.assertEqual(23, graph.number_of_edges())

        expected_nodes = {
            -3: {'label': 'E', 'level': 1, 'x': 0, 'y': -90},
            -2: {'label': 'E', 'level': 1, 'x': 0, 'y': -60},
            -1: {'label': 'E', 'level': 1, 'x': 0, 'y': -30},
            0: {'label': 'E', 'x': 0, 'y': 0, 'level': 1},
            1: {'label': 'E', 'x': 90, 'y': 0, 'level': 1},
            2: {'label': 'E', 'x': 0, 'y': 90, 'level': 1},
            3: {'label': 'E', 'x': 45, 'y': 45, 'level': 1},
            4: {'label': 'i', 'x': 30, 'y': 30, 'level': 1},
            5: {'label': 'E', 'x': 0, 'y': 0, 'level': 2},
            6: {'label': 'E', 'x': 90, 'y': 0, 'level': 2},
            7: {'label': 'E', 'x': 0, 'y': 90, 'level': 2},
            8: {'label': 'E', 'x': 45, 'y': 45, 'level': 2},
            9: {'label': 'I', 'x': 45.0, 'y': 15.0, 'level': 2},
            10: {'label': 'I', 'x': 15.0, 'y': 45.0, 'level': 2}
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1), (0, 2), (0, 4), (0, -1),
            (1, 3), (1, 4),
            (2, 3), (2, 4),
            (4, 9), (4, 10),
            (-1, -2), (-2, -3),
            (5, 6), (5, 7), (5, 8), (5, 9), (5, 10),
            (6, 8), (6, 9),
            (7, 8), (7, 10),
            (8, 9), (8, 10)
        ]

        self.assertEqual(expected_edges, list(graph.edges()))

    # 1a, 4b
    def test_without_one_node_not_applied(self):
        graph = nx.Graph()
        # removed node with id 3
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(4, label='I', x=30, y=30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (2, 0),
            (0, 4),
            (1, 4),
            (2, 4)
        ])

        result = p3(graph, 1)

        self.assertEqual(False, result)
        self.assertEqual(4, graph.number_of_nodes())
        self.assertEqual(5, graph.number_of_edges())

    # 1b, 4c
    def test_without_one_edge_not_applied(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='E', x=45, y=45, level=1).graph_adapter(),
            Node(4, label='I', x=30, y=30, level=1).graph_adapter()
        ])
        # removed (2, 4) edge
        graph.add_edges_from([
            (0, 1),
            (1, 3),
            (2, 3),
            (2, 0),
            (0, 4),
            (1, 4),
        ])

        result = p3(graph, 1)

        self.assertEqual(False, result)
        self.assertEqual(5, graph.number_of_nodes())
        self.assertEqual(6, graph.number_of_edges())

    # 1c, 4d
    def test_changed_edge_label_not_applied(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            # changed label to 'I'
            Node(3, label='I', x=45, y=45, level=1).graph_adapter(),
            Node(4, label='I', x=30, y=30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (1, 3),
            (2, 3),
            (2, 0),
            (0, 4),
            (1, 4),
            (2, 4)
        ])

        result = p3(graph, 1)

        self.assertEqual(False, result)
        self.assertEqual(5, graph.number_of_nodes())
        self.assertEqual(7, graph.number_of_edges())

    # 4e
    def test_with_wrong_dims_on_one_edge_not_applied(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='E', x=60, y=60, level=1).graph_adapter(),
            Node(4, label='I', x=30, y=30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (1, 3),
            (2, 3),
            (2, 0),
            (0, 4),
            (1, 4),
            (2, 4)
        ])

        result = p3(graph, 1)

        self.assertEqual(False, result)
        self.assertEqual(5, graph.number_of_nodes())
        self.assertEqual(7, graph.number_of_edges())


