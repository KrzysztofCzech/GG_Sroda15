import unittest
import networkx as nx
import productions.p7 as p7
from utils import find_isomorphic_graph_p7_p8
from classes import Node
from draw import draw_graph


class P7Test(unittest.TestCase):

    def test_0(self):
        graph = p7.make_mock_graph(0, 0)
        self.assertIsNotNone(p7.p7(graph, 0))

    def test_1(self):
        graph = p7.make_mock_graph(0, 0)
        
        expected_graph = basic_expected_graph(0, 0)
        
        p7.p7(graph, 0)
        self.assertTrue(len(find_isomorphic_graph_p7_p8(graph, expected_graph)))

    def test_2(self):
        uid = 100
        level = 10
        graph = p7.make_mock_graph(uid, level)
        graph.remove_nodes_from([uid+4, uid+2, uid+10, uid+8])
        expected_graph = basic_expected_graph(uid, level)

        p7.p7(graph, level)
        draw_graph(graph, name='p7_test_2')

        self.assertTrue(len(find_isomorphic_graph_p7_p8(graph, expected_graph)))

    def test_3(self):
        uid = 50
        level = 2
        graph = p7.make_mock_graph(uid, level)
        graph.remove_node(uid+1) # removing 1 node
        expected_graph = basic_expected_graph(uid, level)

        p7.p7(graph, level)
        draw_graph(graph, name='p7_test_3')

        self.assertFalse(find_isomorphic_graph_p7_p8(graph, expected_graph))

    def test_4(self):
        uid = 50
        level = 2
        graph = p7.make_mock_graph(uid, level)
        graph.remove_node(uid+3)
        expected_graph = basic_expected_graph(uid, level)

        p7.p7(graph, level)
        draw_graph(graph, name='p7_test_4')

        self.assertFalse(find_isomorphic_graph_p7_p8(graph, expected_graph))

    def test_5(self):
        uid = 100
        level = 10
        graph = p7.make_mock_graph(uid, level)
        graph.add_edge(uid+10, uid+14)
        expected_graph = basic_expected_graph(uid, level)

        p7.p7(graph, level)
        draw_graph(graph, name='p7_test_5')

        self.assertTrue(len(find_isomorphic_graph_p7_p8(graph, expected_graph)))

    def test_6(self):
        uid = 0
        level = 0
        graph = p7.make_mock_graph(uid, level)
        nodes = graph._node
        nodes.get(uid+11)['x'] = 250
        expected_graph = basic_expected_graph(uid, level)

        p7.p7(graph, level)
        draw_graph(graph, name='p7_test_6')

        self.assertFalse(find_isomorphic_graph_p7_p8(graph, expected_graph))

    def test_7(self):
        uid = 0
        level = 0
        graph = p7.make_mock_graph(uid, level)
        nodes = graph._node
        nodes.get(uid+7)['x'] = 111
        expected_graph = basic_expected_graph(uid, level)

        p7.p7(graph, level)
        draw_graph(graph, name='p7_test_7')

        self.assertFalse(find_isomorphic_graph_p7_p8(graph, expected_graph))

    def test_8(self):
            uid = 0
            level = 0
            graph = p7.make_mock_graph(uid, level)
            nodes = graph._node
            nodes.get(uid+7)['label'] = 'I'
            expected_graph = basic_expected_graph(uid, level)

            p7.p7(graph, level)
            draw_graph(graph, name='p7_test_8')

            self.assertFalse(find_isomorphic_graph_p7_p8(graph, expected_graph))


def basic_expected_graph(uid, level):
    expected_graph = nx.Graph()

    expected_graph.add_nodes_from([
        Node(id=uid, label='el', level=level).graph_adapter()
    ])

    expected_graph.add_edges_from([
        (uid, uid + 5), (uid, uid + 6)
    ])

    expected_graph.add_nodes_from([
        Node(id=uid + 1, label='E', level=level + 1).graph_adapter(),
        Node(id=uid + 3, label='E', level=level + 1).graph_adapter(),
        Node(id=uid + 5, label='i', level=level + 1).graph_adapter(),
        Node(id=uid + 6, label='i', level=level + 1).graph_adapter()
    ])

    expected_graph.add_edges_from([
        (uid + 1, uid + 3), (uid + 1, uid + 5),
        (uid + 1, uid + 6), (uid + 3, uid + 6),
        (uid + 3, uid + 5),
    ])

    expected_graph.add_nodes_from([
        Node(id=uid + 7, label='E', level=level + 2).graph_adapter(),
        Node(id=uid + 9, label='E', level=level + 2).graph_adapter(),

        Node(id=uid + 11, label='E', level=level + 2).graph_adapter(),

        Node(id=uid + 13, label='I', level=level + 2).graph_adapter(),
        Node(id=uid + 14, label='I', level=level + 2).graph_adapter(),
        Node(id=uid + 15, label='I', level=level + 2).graph_adapter(),
        Node(id=uid + 16, label='I', level=level + 2).graph_adapter()
    ])

    expected_graph.add_edges_from([
        (uid + 7, uid + 16), (uid + 7, uid + 11), (uid + 7, uid + 11), (uid + 7, uid + 13),
        (uid + 9, uid + 14), (uid + 9, uid + 11), (uid + 9, uid + 11), (uid + 9, uid + 15),
        (uid + 16, uid + 11), (uid + 15, uid + 11), (uid + 14, uid + 11), (uid + 13, uid + 11),

        (uid + 5, uid + 15), (uid + 5, uid + 16),
        (uid + 6, uid + 13), (uid + 6, uid + 14)
    ])

    return expected_graph
