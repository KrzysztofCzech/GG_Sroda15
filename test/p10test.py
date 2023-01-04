import unittest
import networkx as nx
from classes import Node
from draw import draw_graph
from productions.p10 import p10
from pprint import pprint


class P10Test(unittest.TestCase):
    def test_production_is_applied(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=90, level=1).graph_adapter(),
            Node(2, label='i', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='i', x=90, y=0, level=1).graph_adapter(),
            Node(4, label='E', x=0, y=0, level=2).graph_adapter(),
            Node(5, label='E', x=45, y=45, level=2).graph_adapter(),
            Node(6, label='E', x=90, y=90, level=2).graph_adapter(),
            Node(7, label='I', x=00, y=60, level=2).graph_adapter(),
            Node(8, label='I', x=60, y=90, level=2).graph_adapter(),
            Node(9, label='E', x=0, y=0, level=2).graph_adapter(),
            Node(10, label='E', x=90, y=90, level=2).graph_adapter(),
            Node(11, label='I', x=90, y=0, level=2).graph_adapter(),
        ])
        graph.add_edges_from([
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 2),
            (1, 3),

            (4, 5),
            (5, 6),
            (4, 7),
            (7, 5),
            (8, 5),
            (8, 6),

            (9, 10),
            (9, 11),
            (10, 11),

            (2, 7),
            (2, 8),
            (3, 11),
        ])
        draw_graph(graph, name='prod10_1-test_0')

        result = p10(graph, 1)
        draw_graph(graph, name='prod10_1-test_1')

        # pprint(graph._node)

        self.assertTrue(result)
        self.assertEqual(10, graph.number_of_nodes())
        self.assertEqual(16, graph.number_of_edges())

        # pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 90},
            2: {'label': 'i', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'i', 'level': 1, 'x': 90, 'y': 0},
            4: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            5: {'label': 'E', 'level': 2, 'x': 45, 'y': 45},
            6: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            7: {'label': 'I', 'level': 2, 'x': 0, 'y': 60},
            8: {'label': 'I', 'level': 2, 'x': 60, 'y': 90},
            11: {'label': 'I', 'level': 2, 'x': 90, 'y': 0},
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1), (0, 2), (0, 3), (1, 2),  (1, 3), (2, 7),
            (2, 8), (3, 11), (4, 5), (4, 7), (4, 11),
            (5, 6), (5, 7), (5, 8), (6, 8), (6, 11)
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
            Node(5, label='E', x=45, y=45, level=2).graph_adapter(),
            Node(6, label='E', x=90, y=90, level=2).graph_adapter(),
            Node(7, label='I', x=00, y=60, level=2).graph_adapter(),
            Node(8, label='I', x=60, y=90, level=2).graph_adapter(),
            Node(9, label='E', x=0, y=0, level=2).graph_adapter(),
            Node(10, label='E', x=90, y=90, level=2).graph_adapter(),
            Node(11, label='I', x=90, y=0, level=2).graph_adapter(),
            # More added
            Node(12, label='E', x=40, y=250, level=2).graph_adapter(),
            Node(13, label='E', x=80, y=220, level=2).graph_adapter(),
            Node(14, label='E', x=200, y=0, level=2).graph_adapter(),
            Node(15, label='E', x=400, y=45, level=2).graph_adapter(),
        ])
        graph.add_edges_from([
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 2),
            (1, 3),

            (4, 5),
            (5, 6),
            (4, 7),
            (7, 5),
            (8, 5),
            (8, 6),

            (9, 10),
            (9, 11),
            (10, 11),

            (2, 7),
            (2, 8),
            (3, 11),

            # More added
            (9, 12),
            (10, 13),
            (14, 15),
            (14, 11),
            (11, 15),
            (8, 15),
        ])
        draw_graph(graph, name='prod10_2-test_0')

        result = p10(graph, 1)
        draw_graph(graph, name='prod10_2-test_1')

        # pprint(graph._node)

        self.assertTrue(result)
        self.assertEqual(14, graph.number_of_nodes())
        self.assertEqual(22, graph.number_of_edges())

        # pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 90},
            2: {'label': 'i', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'i', 'level': 1, 'x': 90, 'y': 0},
            4: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            5: {'label': 'E', 'level': 2, 'x': 45, 'y': 45},
            6: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            7: {'label': 'I', 'level': 2, 'x': 0, 'y': 60},
            8: {'label': 'I', 'level': 2, 'x': 60, 'y': 90},
            11: {'label': 'I', 'level': 2, 'x': 90, 'y': 0},
            12: {'label': 'E', 'level': 2, 'x': 40, 'y': 250},
            13: {'label': 'E', 'level': 2, 'x': 80, 'y': 220},
            14: {'label': 'E', 'level': 2, 'x': 200, 'y': 0},
            15: {'label': 'E', 'level': 2, 'x': 400, 'y': 45},
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 7),
            (2, 8), (3, 11), (4, 5), (4, 7), (4, 12), (4, 11),
            (5, 6), (5, 7), (5, 8), (6, 8), (6, 13), (6, 11),
            (8, 15), (11, 14), (11, 15), (14, 15)
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
            Node(5, label='E', x=45, y=45, level=2).graph_adapter(),
            Node(6, label='E', x=90, y=90, level=2).graph_adapter(),
            Node(7, label='I', x=00, y=60, level=2).graph_adapter(),
            Node(8, label='I', x=60, y=90, level=2).graph_adapter(),
            Node(9, label='E', x=0, y=0, level=2).graph_adapter(),
            Node(10, label='E', x=90, y=90, level=2).graph_adapter(),
            Node(11, label='I', x=90, y=0, level=2).graph_adapter(),
        ])
        graph.add_edges_from([
            (1, 2),
            (1, 3),

            (4, 5),
            (5, 6),
            (4, 7),
            (7, 5),
            (8, 5),
            (8, 6),

            (9, 10),
            (9, 11),
            (10, 11),

            (2, 7),
            (2, 8),
            (3, 11),
        ])
        draw_graph(graph, name='prod10_3-test_0')

        result = p10(graph, 1)
        draw_graph(graph, name='prod10_3-test_1')

        # print(graph.number_of_nodes())
        # pprint(graph._node)
        # print(graph.number_of_edges())
        # pprint(list(graph.edges()))

        self.assertFalse(result)
        self.assertEqual(11, graph.number_of_nodes())
        self.assertEqual(14, graph.number_of_edges())

        expected_nodes = {
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 90},
            2: {'label': 'i', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'i', 'level': 1, 'x': 90, 'y': 0},
            4: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            5: {'label': 'E', 'level': 2, 'x': 45, 'y': 45},
            6: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            7: {'label': 'I', 'level': 2, 'x': 0, 'y': 60},
            8: {'label': 'I', 'level': 2, 'x': 60, 'y': 90},
            9: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            10: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            11: {'label': 'I', 'level': 2, 'x': 90, 'y': 0},
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (1, 2), (1, 3), (2, 7), (2, 8), (3, 11),
            (4, 5), (4, 7), (5, 6), (5, 7), (5, 8),
            (6, 8), (9, 10), (9, 11), (10, 11)
        ]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_without_one_node_replaced_with_other(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            # Node 0 removed
            Node(1, label='E', x=90, y=90, level=1).graph_adapter(),
            Node(2, label='i', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='i', x=90, y=0, level=1).graph_adapter(),
            Node(4, label='E', x=0, y=0, level=2).graph_adapter(),
            Node(5, label='E', x=45, y=45, level=2).graph_adapter(),
            Node(6, label='E', x=90, y=90, level=2).graph_adapter(),
            Node(7, label='I', x=00, y=60, level=2).graph_adapter(),
            Node(8, label='I', x=60, y=90, level=2).graph_adapter(),
            Node(9, label='E', x=0, y=0, level=2).graph_adapter(),
            Node(10, label='E', x=90, y=90, level=2).graph_adapter(),
            Node(11, label='I', x=90, y=0, level=2).graph_adapter(),
            # More
            Node(12, label='E', x=40, y=250, level=2).graph_adapter(),
            Node(13, label='E', x=80, y=220, level=2).graph_adapter(),
        ])
        graph.add_edges_from([
            (1, 2),
            (1, 3),

            (4, 5),
            (5, 6),
            (4, 7),
            (7, 5),
            (8, 5),
            (8, 6),

            (9, 10),
            (9, 11),
            (10, 11),

            (2, 7),
            (2, 8),
            (3, 11),

            # More
            (12, 13),
            (11, 12),
        ])
        draw_graph(graph, name='prod10_4-test_0')

        result = p10(graph, 1)
        draw_graph(graph, name='prod10_4-test_1')

        # print(graph.number_of_nodes())
        # pprint(graph._node)
        # print(graph.number_of_edges())
        # pprint(list(graph.edges()))

        self.assertFalse(result)
        self.assertEqual(13, graph.number_of_nodes())
        self.assertEqual(16, graph.number_of_edges())

        expected_nodes = {
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 90},
            2: {'label': 'i', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'i', 'level': 1, 'x': 90, 'y': 0},
            4: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            5: {'label': 'E', 'level': 2, 'x': 45, 'y': 45},
            6: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            7: {'label': 'I', 'level': 2, 'x': 0, 'y': 60},
            8: {'label': 'I', 'level': 2, 'x': 60, 'y': 90},
            9: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            10: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            11: {'label': 'I', 'level': 2, 'x': 90, 'y': 0},
            12: {'label': 'E', 'level': 2, 'x': 40, 'y': 250},
            13: {'label': 'E', 'level': 2, 'x': 80, 'y': 220}
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (1, 2),
            (1, 3),
            (2, 7),
            (2, 8),
            (3, 11),
            (4, 5),
            (4, 7),
            (5, 6),
            (5, 7),
            (5, 8),
            (6, 8),
            (9, 10),
            (9, 11),
            (10, 11),
            (11, 12),
            (12, 13)
        ]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_without_one_edge(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=90, level=1).graph_adapter(),
            Node(2, label='i', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='i', x=90, y=0, level=1).graph_adapter(),
            Node(4, label='E', x=0, y=0, level=2).graph_adapter(),
            Node(5, label='E', x=45, y=45, level=2).graph_adapter(),
            Node(6, label='E', x=90, y=90, level=2).graph_adapter(),
            Node(7, label='I', x=00, y=60, level=2).graph_adapter(),
            Node(8, label='I', x=60, y=90, level=2).graph_adapter(),
            Node(9, label='E', x=0, y=0, level=2).graph_adapter(),
            Node(10, label='E', x=90, y=90, level=2).graph_adapter(),
            Node(11, label='I', x=90, y=0, level=2).graph_adapter(),
        ])
        graph.add_edges_from([
            (0, 1),
            (0, 2),
            # Removed edge:
            # (0, 3),
            (1, 2),
            (1, 3),

            (4, 5),
            (5, 6),
            (4, 7),
            (7, 5),
            (8, 5),
            (8, 6),

            (9, 10),
            (9, 11),
            (10, 11),

            (2, 7),
            (2, 8),
            (3, 11),
        ])
        draw_graph(graph, name='prod10_5-test_0')

        result = p10(graph, 1)
        draw_graph(graph, name='prod10_5-test_1')

        print(graph.number_of_nodes())
        pprint(graph._node)
        print(graph.number_of_edges())
        pprint(list(graph.edges()))

        self.assertFalse(result)
        self.assertEqual(12, graph.number_of_nodes())
        self.assertEqual(16, graph.number_of_edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 90},
            2: {'label': 'i', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'i', 'level': 1, 'x': 90, 'y': 0},
            4: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            5: {'label': 'E', 'level': 2, 'x': 45, 'y': 45},
            6: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            7: {'label': 'I', 'level': 2, 'x': 0, 'y': 60},
            8: {'label': 'I', 'level': 2, 'x': 60, 'y': 90},
            9: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            10: {'label': 'E', 'level': 2, 'x': 90, 'y': 90},
            11: {'label': 'I', 'level': 2, 'x': 90, 'y': 0}
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1),
            (0, 2),
            (1, 2),
            (1, 3),
            (2, 7),
            (2, 8),
            (3, 11),
            (4, 5),
            (4, 7),
            (5, 6),
            (5, 7),
            (5, 8),
            (6, 8),
            (9, 10),
            (9, 11),
            (10, 11)
        ]

        self.assertEqual(expected_edges, list(graph.edges()))
