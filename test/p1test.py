import unittest
import networkx as nx
from classes import Node
from draw import draw_graph
from productions.p1 import p1

class P1Test(unittest.TestCase):
    def test_p1_production_is_applied(self):
        '''Testing if production was successfully applied.'''
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='El', x=0, y=0, level=1).graph_adapter()
        ])

        draw_graph(graph, name='prod1_test1.0')

        result = p1(graph, 1)
        draw_graph(graph, name='prod1_test1.1')

        self.assertEqual(True, result)
        self.assertEqual(7, graph.number_of_nodes())
        self.assertEqual(13, graph.number_of_edges())

        expected_nodes = {
            0: {'label': 'el', 'x': 0.0, 'y': 0.0, 'level': 1},
            1: {'label': 'I', 'x': 10.0, 'y': 10.0, 'level': 2},
            2: {'label': 'I', 'x': 20.0, 'y': 20.0, 'level': 2},
            3: {'label': 'E', 'x': 0.0, 'y': 0.0, 'level': 2},
            4: {'label': 'E', 'x': 30.0, 'y': 0.0, 'level': 2},
            5: {'label': 'E', 'x': 30.0, 'y': 30.0, 'level': 2},
            6: {'label': 'E', 'x': 0.0, 'y': 30.0, 'level': 2},
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1),
            (0, 2),
            (1, 3),
            (1, 4),
            (1, 6),
            (2, 4),
            (2, 5),
            (2, 6),
            (3, 4),
            (3, 6),
            (4, 5),
            (4, 6),
            (5, 6)
            ]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_p1_as_subgraph_is_applied(self):
        '''Testing if production was applied successfully with additional node.'''
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='El', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=10, y=15, level=1).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1)
        ])

        draw_graph(graph, name='prod1_test2.0')

        result = p1(graph, 1)
        draw_graph(graph, name='prod1_test2.1')

        self.assertEqual(True, result)
        self.assertEqual(8, graph.number_of_nodes())
        self.assertEqual(14, graph.number_of_edges())

        expected_nodes = {
            0: {'label': 'el', 'x': 0, 'y': 0, 'level': 1},
            1: {'label': 'E', 'x': 10, 'y': 15, 'level': 1},
            2: {'label': 'I', 'x': 10.0, 'y': 10.0, 'level': 2},
            3: {'label': 'I', 'x': 20.0, 'y': 20.0, 'level': 2},
            4: {'label': 'E', 'x': 0, 'y': 0, 'level': 2},
            5: {'label': 'E', 'x': 30, 'y': 0, 'level': 2},
            6: {'label': 'E', 'x': 30, 'y': 30, 'level': 2},
            7: {'label': 'E', 'x': 0, 'y': 30, 'level': 2}}

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1), (0, 2), (0, 3), (2, 4),
            (2, 5), (2, 7), (3, 5), (3, 6),
            (3, 7), (4, 5), (4, 7), (5, 6),
            (5, 7), (6, 7)
            ]


        self.assertEqual(expected_edges, list(graph.edges()))

    def test_p1_production_is_not_applied(self):
        '''Testing if prodcution was not applied when main node "El" was changed.'''
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter()
        ])

        draw_graph(graph, name='prod1_test3.0')

        result = p1(graph, 1)
        draw_graph(graph, name='prod1_test3.1')

        self.assertEqual(False, result)
        self.assertEqual(1, graph.number_of_nodes())
        self.assertEqual(0, graph.number_of_edges())

        expected_nodes = {
            0: {'label': 'E', 'x': 0.0, 'y': 0.0, 'level': 1}
        }

        self.assertEqual(expected_nodes, graph._node)
