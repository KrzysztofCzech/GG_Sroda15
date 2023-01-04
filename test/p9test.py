import unittest
import networkx as nx
from classes import Node
from draw import draw_graph
from productions.p9 import p9
from pprint import pprint


class P9Test(unittest.TestCase):
    def test_production_is_applied(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='I', x=30, y=30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (1, 2),
            (2, 0),
            (0, 3),
            (1, 3),
            (2, 3)
        ])
        draw_graph(graph, name='prod9_1-test_0')

        result = p9(graph, 1)
        draw_graph(graph, name='prod9_1-test_1')

        pprint(graph._node)

        self.assertEqual(True, result)
        self.assertEqual(8, graph.number_of_nodes())
        self.assertEqual(13, graph.number_of_edges())

        pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 0},
            2: {'label': 'E', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'i', 'level': 1, 'x': 30, 'y': 30},
            4: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            5: {'label': 'E', 'level': 2, 'x': 90, 'y': 0},
            6: {'label': 'E', 'level': 2, 'x': 0, 'y': 90},
            7: {'label': 'I', 'level': 2, 'x': 30.0, 'y': 30.0}
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1), (0, 2), (0, 3),
                          (1, 2), (1, 3), (2, 3),
                          (3, 7),
                          (4, 5), (4, 6), (4, 7),
                          (5, 6), (5, 7), (6, 7)]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_as_subgraph_is_applied(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='I', x=30, y=30, level=1).graph_adapter(),
            # More added
            Node(55, label='E', x=90, y=90, level=1).graph_adapter(),
            Node(56, label='E', x=45, y=-30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (1, 2),
            (2, 0),
            (0, 3),
            (1, 3),
            (2, 3),
            # More added
            (1, 55),
            (2, 55),
            (0, 56),
            (1, 56),
        ])
        draw_graph(graph, name='prod9_2-test_0', level_offset=150)

        result = p9(graph, 1)
        draw_graph(graph, name='prod9_2-test_1', level_offset=150)

        pprint(graph._node)

        self.assertEqual(True, result)
        self.assertEqual(10, graph.number_of_nodes())
        self.assertEqual(17, graph.number_of_edges())

        pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 0},
            2: {'label': 'E', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'i', 'level': 1, 'x': 30, 'y': 30},
            55: {'label': 'E', 'level': 1, 'x': 90, 'y': 90},
            56: {'label': 'E', 'level': 1, 'x': 45, 'y': -30},
            57: {'label': 'E', 'level': 2, 'x': 0, 'y': 0},
            58: {'label': 'E', 'level': 2, 'x': 90, 'y': 0},
            59: {'label': 'E', 'level': 2, 'x': 0, 'y': 90},
            60: {'label': 'I', 'level': 2, 'x': 30.0, 'y': 30.0}
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1), (0, 2), (0, 3), (0, 56), (1, 2), (1, 3), (1, 55), (1, 56), (2, 3), (2, 55),
                          (3, 60),
                          (57, 58), (57, 59), (57, 60), (58, 59), (58, 60), (59, 60)]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_without_one_node_removed(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            # Node 2 removed
            Node(3, label='I', x=30, y=30, level=1).graph_adapter(),
        ])
        graph.add_edges_from([
            (0, 1),
            (0, 3),
            (1, 3),
        ])
        draw_graph(graph, name='prod9_3-test_0')

        result = p9(graph, 1)
        draw_graph(graph, name='prod9_3-test_1')

        pprint(graph._node)

        self.assertEqual(False, result)
        self.assertEqual(3, graph.number_of_nodes())
        self.assertEqual(3, graph.number_of_edges())

        pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 0},
            3: {'label': 'I', 'level': 1, 'x': 30, 'y': 30},
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1),
                          (0, 3),
                          (1, 3)]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_without_one_node_replaced_with_other(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            # Node 2 removed
            Node(3, label='I', x=30, y=30, level=1).graph_adapter(),
            # More added
            Node(55, label='E', x=90, y=90, level=1).graph_adapter(),
            Node(56, label='E', x=45, y=-30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (0, 3),
            (1, 3),
            # More added
            (1, 55),
            (0, 56),
            (1, 56),
        ])
        draw_graph(graph, name='prod9_4-test_0')

        result = p9(graph, 1)
        draw_graph(graph, name='prod9_4-test_1')

        pprint(graph._node)

        self.assertEqual(False, result)
        self.assertEqual(5, graph.number_of_nodes())
        self.assertEqual(6, graph.number_of_edges())

        pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 0},
            3: {'label': 'I', 'level': 1, 'x': 30, 'y': 30},
            55: {'label': 'E', 'level': 1, 'x': 90, 'y': 90},
            56: {'label': 'E', 'level': 1, 'x': 45, 'y': -30}
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1),
                          (0, 3),
                          (0, 56),
                          (1, 3),
                          (1, 55),
                          (1, 56)]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_without_one_edge_not_applied(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='I', x=30, y=30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (1, 2),
            (2, 0),
            (0, 3),
            (1, 3),
            # Missing edge: (2, 3)
        ])
        draw_graph(graph, name='prod9_5-test_0')

        result = p9(graph, 1)
        draw_graph(graph, name='prod9_5-test_1')

        pprint(graph._node)

        self.assertEqual(False, result)
        self.assertEqual(4, graph.number_of_nodes())
        self.assertEqual(5, graph.number_of_edges())

        pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 0},
            2: {'label': 'E', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'I', 'level': 1, 'x': 30, 'y': 30},
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1), (0, 2), (0, 3),
                          (1, 2), (1, 3)]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_changed_wrong_e_label(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='I', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='I', x=30, y=30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (1, 2),
            (2, 0),
            (0, 3),
            (1, 3),
            (2, 3)
        ])
        draw_graph(graph, name='prod9_6-test_0')

        result = p9(graph, 1)
        draw_graph(graph, name='prod9_6-test_1')

        pprint(graph._node)

        self.assertEqual(False, result)
        self.assertEqual(4, graph.number_of_nodes())
        self.assertEqual(6, graph.number_of_edges())

        pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 0},
            2: {'label': 'I', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'I', 'level': 1, 'x': 30, 'y': 30},
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1), (0, 2), (0, 3),
                          (1, 2), (1, 3), (2, 3)]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_changed_edge_wrong_i_label(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            # Small `i` letter - production already applied
            Node(3, label='i', x=30, y=30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (1, 2),
            (2, 0),
            (0, 3),
            (1, 3),
            (2, 3)
        ])
        draw_graph(graph, name='prod9_7-test_0')

        result = p9(graph, 1)
        draw_graph(graph, name='prod9_7-test_1')

        pprint(graph._node)

        self.assertEqual(False, result)
        self.assertEqual(4, graph.number_of_nodes())
        self.assertEqual(6, graph.number_of_edges())

        pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 0},
            2: {'label': 'E', 'level': 1, 'x': 0, 'y': 90},
            3: {'label': 'i', 'level': 1, 'x': 30, 'y': 30},
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1), (0, 2), (0, 3),
                          (1, 2), (1, 3), (2, 3)]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_with_wrong_node_level_not_applied(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=2).graph_adapter(),
            Node(3, label='I', x=30, y=30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (1, 2),
            (2, 0),
            (0, 3),
            (1, 3),
            (2, 3)
        ])
        draw_graph(graph, name='prod9_8-test_0', level_offset=0)

        result = p9(graph, 1)
        draw_graph(graph, name='prod9_8-test_1', level_offset=0)

        pprint(graph._node)
        self.assertEqual(False, result)
        self.assertEqual(4, graph.number_of_nodes())
        self.assertEqual(6, graph.number_of_edges())

        pprint(graph.edges())

        expected_nodes = {
            0: {'label': 'E', 'level': 1, 'x': 0, 'y': 0},
            1: {'label': 'E', 'level': 1, 'x': 90, 'y': 0},
            2: {'label': 'E', 'level': 2, 'x': 0, 'y': 90},
            3: {'label': 'I', 'level': 1, 'x': 30, 'y': 30},
        }

        self.assertEqual(expected_nodes, graph._node)

        expected_edges = [(0, 1), (0, 2), (0, 3),
                          (1, 2), (1, 3), (2, 3)]

        self.assertEqual(expected_edges, list(graph.edges()))

    def test_production_is_applied_only_once(self):
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(0, label='E', x=0, y=0, level=1).graph_adapter(),
            Node(1, label='E', x=90, y=0, level=1).graph_adapter(),
            Node(2, label='E', x=0, y=90, level=1).graph_adapter(),
            Node(3, label='I', x=30, y=30, level=1).graph_adapter()
        ])
        graph.add_edges_from([
            (0, 1),
            (1, 2),
            (2, 0),
            (0, 3),
            (1, 3),
            (2, 3)
        ])
        draw_graph(graph, name='prod9_9-test_0')

        result = p9(graph, 1)
        draw_graph(graph, name='prod9_9-test_1')

        pprint(graph._node)

        self.assertEqual(True, result)
        self.assertEqual(8, graph.number_of_nodes())
        self.assertEqual(13, graph.number_of_edges())

        result = p9(graph, 1)

        self.assertEqual(False, result)
        self.assertEqual(8, graph.number_of_nodes())
        self.assertEqual(13, graph.number_of_edges())
        draw_graph(graph, name='prod9_9-test_2')
