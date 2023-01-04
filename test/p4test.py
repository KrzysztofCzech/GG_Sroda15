import unittest
import networkx as nx
from classes import Node
from draw import draw_graph
from productions.p4 import p4


class P4Test(unittest.TestCase):
    maxDiff = None

    # 2c, 2d, 2e, 4a, 5a, 5d, 5e, 5f
    def test_p4_production_is_applied(self):
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

        result = p4(graph, 1)

        self.assertEqual(True, result)
        self.assertEqual(14, graph.number_of_nodes())
        self.assertEqual(27, graph.number_of_edges())

        expected_nodes = {
            0: {'label': 'E', 'x': 0, 'y': 0, 'level': 1},
            1: {'label': 'E', 'x': 90, 'y': 0, 'level': 1},
            2: {'label': 'E', 'x': 0, 'y': 90, 'level': 1},
            3: {'label': 'E', 'x': 45, 'y': 45, 'level': 1},
            4: {'label': 'i', 'x': 30, 'y': 30, 'level': 1},
            5: {'label': 'E', 'x': 0, 'y': 45, 'level': 1},
            6: {'label': 'E', 'x': 0, 'y': 0, 'level': 2},
            7: {'label': 'E', 'x': 90, 'y': 0, 'level': 2},
            8: {'label': 'E', 'x': 0, 'y': 90, 'level': 2},
            9: {'label': 'E', 'x': 45, 'y': 45, 'level': 2},
            10: {'label': 'E', 'x': 0, 'y': 45, 'level': 2},
            11: {'label': 'I', 'x': 45, 'y': 15, 'level': 2},
            12: {'label': 'I', 'x': 15, 'y': 60, 'level': 2},
            13: {'label': 'I', 'x': 15, 'y': 30, 'level': 2},
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1), (0, 5), (0, 4),
            (1, 3), (1, 4),
            (2, 3), (2, 4), (2, 5),
            (4, 11), (4, 12), (4, 13),
            (6, 7), (6, 9), (6, 10), (6, 11), (6, 13),
            (7, 9), (7, 11),
            (8, 9), (8, 10), (8, 12),
            (9, 10), (9, 11), (9, 12), (9, 13),
            (10, 12), (10, 13),
        ]

        self.assertListEqual(sorted(expected_edges), sorted(list(graph.edges())))

    # 1d, 2a, 2b, 5b, 5c
    def test_p4_as_subgraph_is_applied(self):
        graph = nx.Graph()

        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='E', x=45, y=45, level=1).graph_adapter(),
            Node(4, label='I', x=30, y=30, level=1).graph_adapter(),
            Node(5, label='E', x=0, y=45, level=1).graph_adapter(),
            # added nodes
            Node(-1, label='E', x=0, y=-30, level=1).graph_adapter(),
            Node(-2, label='E', x=0, y=-60, level=1).graph_adapter(),
            Node(-3, label='E', x=0, y=-90, level=1).graph_adapter(),
        ])
        graph.add_edges_from([
            (0, 1),
            (1, 3),
            (2, 3),
            (2, 5),
            (5, 0),
            (0, 4),
            (1, 4),
            (2, 4),
            (0, -1),
            (-1, -2),
            (-2, -3)
        ])

        result = p4(graph, 1)

        self.assertEqual(True, result)
        self.assertEqual(17, graph.number_of_nodes())
        self.assertEqual(30, graph.number_of_edges())

        expected_nodes = {
            -3: {'label': 'E', 'level': 1, 'x': 0, 'y': -90},
            -2: {'label': 'E', 'level': 1, 'x': 0, 'y': -60},
            -1: {'label': 'E', 'level': 1, 'x': 0, 'y': -30},
            0: {'label': 'E', 'x': 0, 'y': 0, 'level': 1},
            1: {'label': 'E', 'x': 90, 'y': 0, 'level': 1},
            2: {'label': 'E', 'x': 0, 'y': 90, 'level': 1},
            3: {'label': 'E', 'x': 45, 'y': 45, 'level': 1},
            4: {'label': 'i', 'x': 30, 'y': 30, 'level': 1},
            5: {'label': 'E', 'x': 0, 'y': 45, 'level': 1},
            6: {'label': 'E', 'x': 0, 'y': 0, 'level': 2},
            7: {'label': 'E', 'x': 90, 'y': 0, 'level': 2},
            8: {'label': 'E', 'x': 0, 'y': 90, 'level': 2},
            9: {'label': 'E', 'x': 45, 'y': 45, 'level': 2},
            10: {'label': 'E', 'x': 0, 'y': 45, 'level': 2},
            11: {'label': 'I', 'x': 45, 'y': 15, 'level': 2},
            12: {'label': 'I', 'x': 15, 'y': 60, 'level': 2},
            13: {'label': 'I', 'x': 15, 'y': 30, 'level': 2},
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (-2, -3),
            (-1, -2),
            (0, -1),
            (0, 1), (0, 5), (0, 4),
            (1, 3), (1, 4),
            (2, 3), (2, 4), (2, 5),
            (4, 11), (4, 12), (4, 13),
            (6, 7), (6, 9), (6, 10), (6, 11), (6, 13),
            (7, 9), (7, 11),
            (8, 9), (8, 10), (8, 12),
            (9, 10), (9, 11), (9, 12), (9, 13),
            (10, 12), (10, 13),
        ]

        self.assertListEqual(sorted(expected_edges), sorted(list(graph.edges())))

    # 1a, 4b
    def test_p4_without_one_node_not_applied(self):
        graph = nx.Graph()

        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(4, label='I', x=30, y=30, level=1).graph_adapter(),
            Node(5, label='E', x=0, y=45, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (2, 5),
            (5, 0),
            (0, 4),
            (1, 4),
            (2, 4)
        ])

        result = p4(graph, 1)

        self.assertEqual(False, result)
        self.assertEqual(5, graph.number_of_nodes())
        self.assertEqual(6, graph.number_of_edges())

    # # 1b, 4c
    def test_p4_without_one_edge_not_applied(self):
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
            (1, 4)
        ])

        result = p4(graph, 1)

        self.assertEqual(False, result)
        self.assertEqual(6, graph.number_of_nodes())
        self.assertEqual(7, graph.number_of_edges())

    # # 1c, 4d
    def test_p4_changed_edge_label_not_applied(self):
        graph = nx.Graph()

        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='E', x=45, y=45, level=1).graph_adapter(),
            Node(4, label='I', x=30, y=30, level=1).graph_adapter(),
            # modified label to I
            Node(5, label='I', x=0, y=45, level=1).graph_adapter()
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

        result = p4(graph, 1)

        self.assertEqual(False, result)
        self.assertEqual(6, graph.number_of_nodes())
        self.assertEqual(8, graph.number_of_edges())

    # 4e
    def test_p4_with_wrong_dims_on_one_edge_not_applied(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='E', x=60, y=60, level=1).graph_adapter(),
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

        result = p4(graph, 1)

        draw_graph(graph, name='prod4-test')

        self.assertEqual(False, result)
        self.assertEqual(6, graph.number_of_nodes())
        self.assertEqual(8, graph.number_of_edges())
