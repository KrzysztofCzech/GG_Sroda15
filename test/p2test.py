import unittest
import networkx as nx
from classes import Node
from draw import draw_graph
from productions.p2 import p2

class P2Test(unittest.TestCase):
    def test_p2_production_is_applied(self):
        '''Testing if production was successfully applied.'''
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='I', x=6, y=6, level=1).graph_adapter(),
            Node(1, label='E', x=18, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=18, level=1).graph_adapter(),
            Node(3, label='E', x=0, y=0, level=1).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 1)
        ])

        draw_graph(graph, name='prod2_test1.0')

        result = p2(graph, 1)
        draw_graph(graph, name='prod2_test1.1')

        self.assertEqual(True, result)
        self.assertEqual(10, graph.number_of_nodes())
        self.assertEqual(20, graph.number_of_edges())

        expected_nodes = {
            0: {'label': 'i', 'x': 6.0, 'y': 6.0, 'level': 1},
            1: {'label': 'E', 'x': 18, 'y': 0, 'level': 1},
            2: {'label': 'E', 'x': 0, 'y': 18, 'level': 1},
            3: {'label': 'E', 'x': 0, 'y': 0, 'level': 1},
            4: {'label': 'I', 'x': 3.0, 'y': 9.0, 'level': 2},
            5: {'label': 'I', 'x': 9.0, 'y': 3.6, 'level': 2},
            6: {'label': 'E', 'x': 18, 'y': 0, 'level': 2},
            7: {'label': 'E', 'x': 0, 'y': 18, 'level': 2},
            8: {'label': 'E', 'x': 0, 'y': 0, 'level': 2},
            9: {'label': 'E', 'x': 9.0, 'y': 9.0, 'level': 2}
            }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1), (0, 2), (0, 3), (0, 4),
            (0, 5), (1, 2), (1, 3), (2, 3),
            (4, 7), (4, 8), (4, 9), (5, 6),
            (5, 8), (5, 9), (6, 7), (6, 9),
            (6, 8), (7, 8), (7, 9), (8, 9)
            ]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_p2_as_subgraph_is_applied(self):
        '''Testing if production was applied successfully with additional node.'''
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='I', x=6, y=6, level=1).graph_adapter(),
            Node(1, label='E', x=18, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=18, level=1).graph_adapter(),
            Node(3, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(4, label='el', x=-5, y=-5, level=1).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 1), (1, 4)
        ])

        draw_graph(graph, name='prod2_test2.0')

        result = p2(graph, 1)
        draw_graph(graph, name='prod2_test2.1')

        self.assertEqual(True, result)
        self.assertEqual(11, graph.number_of_nodes())
        self.assertEqual(21, graph.number_of_edges())

        expected_nodes = {
            0: {'label': 'i', 'x': 6.0, 'y': 6.0, 'level': 1},
            1: {'label': 'E', 'x': 18, 'y': 0, 'level': 1},
            2: {'label': 'E', 'x': 0, 'y': 18, 'level': 1},
            3: {'label': 'E', 'x': 0, 'y': 0, 'level': 1},
            4: {'label': 'el', 'x': -5, 'y': -5, 'level': 1},
            5: {'label': 'I', 'x': 3.0, 'y': 9.0, 'level': 2},
            6: {'label': 'I', 'x': 9.0, 'y': 3.6, 'level': 2},
            7: {'label': 'E', 'x': 18, 'y': 0, 'level': 2},
            8: {'label': 'E', 'x': 0, 'y': 18, 'level': 2},
            9: {'label': 'E', 'x': 0, 'y': 0, 'level': 2},
            10: {'label': 'E', 'x': 9.0, 'y': 9.0, 'level': 2}
            }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1), (0, 2), (0, 3), (0, 5), (0, 6),
            (1, 2), (1, 3), (1, 4), (2, 3), (5, 8),
            (5, 9), (5, 10), (6, 7), (6, 9), (6, 10),
            (7, 8), (7, 10), (7, 9), (8, 9), (8, 10),
            (9, 10)
            ]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_p2_production_is_not_applied(self):
        '''Testing if prodcution was not applied when main node "I" was changed.'''
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='i', x=6, y=6, level=1).graph_adapter(),
            Node(1, label='E', x=18, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=18, level=1).graph_adapter(),
            Node(3, label='E', x=0, y=0, level=1).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1), (0, 2), (0, 3), (1, 2), (2, 3), (3, 1)
        ])

        draw_graph(graph, name='prod2_test3.0')

        result = p2(graph, 1)
        draw_graph(graph, name='prod2_test3.1')

        self.assertEqual(False, result)
        self.assertEqual(4, graph.number_of_nodes())
        self.assertEqual(6, graph.number_of_edges())

        expected_nodes = {
            0: {'label': 'i', 'x': 6, 'y': 6, 'level': 1},
            1: {'label': 'E', 'x': 18, 'y': 0, 'level': 1},
            2: {'label': 'E', 'x': 0, 'y': 18, 'level': 1},
            3: {'label': 'E', 'x': 0, 'y': 0, 'level': 1}
            }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


        self.assertEqual(expected_edges, list(graph.edges()))

    def test_p2_production_is_not_applied_when_edge_removed(self):
        '''Testing if production was not successfully applied when edge removed.'''
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='I', x=6, y=6, level=1).graph_adapter(),
            Node(1, label='E', x=18, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=18, level=1).graph_adapter(),
            Node(3, label='E', x=0, y=0, level=1).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1), (0, 2), (0, 3), (1, 2), (2, 3)
        ])

        draw_graph(graph, name='prod2_test4.0')

        result = p2(graph, 1)
        draw_graph(graph, name='prod2_test4.1')

        self.assertEqual(False, result)
        self.assertEqual(4, graph.number_of_nodes())
        self.assertEqual(5, graph.number_of_edges())

        expected_nodes = {
            0: {'label': 'I', 'x': 6, 'y': 6, 'level': 1},
            1: {'label': 'E', 'x': 18, 'y': 0, 'level': 1},
            2: {'label': 'E', 'x': 0, 'y': 18, 'level': 1},
            3: {'label': 'E', 'x': 0, 'y': 0, 'level': 1}}

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]


        self.assertEqual(expected_edges, list(graph.edges()))

    def test_with_one_node_number_changed(self):
        '''Testing if production was successfully applied when node id changed.'''
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='I', x=6, y=6, level=1).graph_adapter(),
            Node(1, label='E', x=18, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=18, level=1).graph_adapter(),
            Node(4, label='E', x=0, y=0, level=1).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1), (0, 2), (0, 4), (1, 2), (2, 4), (4, 1)
        ])

        draw_graph(graph, name='prod2_test5.0')

        result = p2(graph, 1)
        draw_graph(graph, name='prod2_test5.1')

        expected_nodes = {
            0: {'label': 'i', 'x': 6.0, 'y': 6.0, 'level': 1},
            1: {'label': 'E', 'x': 18, 'y': 0, 'level': 1},
            2: {'label': 'E', 'x': 0, 'y': 18, 'level': 1},
            4: {'label': 'E', 'x': 0, 'y': 0, 'level': 1},
            5: {'label': 'I', 'x': 3.0, 'y': 9.0, 'level': 2},
            6: {'label': 'I', 'x': 9.0, 'y': 3.6, 'level': 2},
            7: {'label': 'E', 'x': 18, 'y': 0, 'level': 2},
            8: {'label': 'E', 'x': 0, 'y': 18, 'level': 2},
            9: {'label': 'E', 'x': 0, 'y': 0, 'level': 2},
            10: {'label': 'E', 'x': 9.0, 'y': 9.0, 'level': 2}
            }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [
            (0, 1), (0, 2), (0, 4), (0, 5), (0, 6),
            (1, 2), (1, 4), (2, 4), (5, 8), (5, 9),
            (5, 10), (6, 7), (6, 9), (6, 10), (7, 8),
            (7, 10), (7, 9), (8, 9), (8, 10), (9, 10)
            ]

        self.assertEqual(expected_edges, list(graph.edges()))

        self.assertEqual(True, result)
        self.assertEqual(10, graph.number_of_nodes())
        self.assertEqual(20, graph.number_of_edges())

    def test_p2_production_is_not_applied_when_node_removed(self):
        '''Testing if production was not successfully applied when node removed.'''
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='I', x=6, y=6, level=1).graph_adapter(),
            Node(1, label='E', x=18, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=18, level=1).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1), (0, 2), (1, 2)
        ])

        draw_graph(graph, name='prod2_test6.0')

        result = p2(graph, 1)
        draw_graph(graph, name='prod2_test6.1')

        # print(graph._node)
        # print(graph.edges())

        self.assertEqual(False, result)
        self.assertEqual(3, graph.number_of_nodes())
        self.assertEqual(3, graph.number_of_edges())

        expected_nodes = {
            0: {'label': 'I', 'x': 6, 'y': 6, 'level': 1},
            1: {'label': 'E', 'x': 18, 'y': 0, 'level': 1},
            2: {'label': 'E', 'x': 0, 'y': 18, 'level': 1}
            }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1), (0, 2), (1, 2)]


        self.assertEqual(expected_edges, list(graph.edges()))
