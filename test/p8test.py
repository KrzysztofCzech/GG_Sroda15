import unittest
import networkx as nx
import productions.p8 as p8
from utils import find_isomorphic_graph_p7_p8
from classes import Node
from draw import draw_graph


class P8Test(unittest.TestCase):

    def test_0(self):
        graph = p8.make_mock_graph(0, 0)
        self.assertTrue(p8.p8(graph, 0))

    def test_1(self):
        graph = p8.make_mock_graph(0, 0)
        
        expected_graph = basic_expected_graph(0, 0)
        
        p8.p8(graph, 0)
        draw_graph(graph, name='p8_test_1')

        self.assertTrue(len(find_isomorphic_graph_p7_p8(graph, expected_graph)))

    def test_2(self):
        uid = 100
        level = 10
        graph = p8.make_mock_graph(uid, level)
        graph.remove_nodes_from([uid+4, uid+2, uid+10, uid+8])
        expected_graph = basic_expected_graph(uid, level)

        p8.p8(graph, level)
        draw_graph(graph, name='p8_test_2')

        self.assertTrue(len(find_isomorphic_graph_p7_p8(graph, expected_graph)))

    def test_3(self):
        uid = 100
        level = 10
        graph = p8.make_mock_graph(uid, level)
        graph.remove_nodes_from([uid+4, uid+2, uid+10, uid+8])
        expected_graph = basic_expected_graph(uid, level)

        p8.p8(graph, level)
        draw_graph(graph, name='p8_test_3')

        self.assertTrue(len(find_isomorphic_graph_p7_p8(graph, expected_graph)))

    def test_4(self):
        uid = 50
        level = 2
        graph = p8.make_mock_graph(uid, level)
        graph.remove_node(uid+3)
        expected_graph = basic_expected_graph(uid, level)

        p8.p8(graph, level)
        draw_graph(graph, name='p8_test_4')

        self.assertFalse(find_isomorphic_graph_p7_p8(graph, expected_graph))

    def test_5(self):
        uid = 100
        level = 10
        graph = p8.make_mock_graph(uid, level)
        graph.add_edge(uid+10, uid+14)
        expected_graph = basic_expected_graph(uid, level)

        p8.p8(graph, level)
        draw_graph(graph, name='p8_test_5')

        self.assertTrue(len(find_isomorphic_graph_p7_p8(graph, expected_graph)))

    def test_6(self):
        uid = 0
        level = 0
        graph = p8.make_mock_graph(uid, level)
        nodes = graph._node
        nodes.get(uid+11)['x'] = 111
        expected_graph = basic_expected_graph(uid, level)

        p8.p8(graph, level)
        draw_graph(graph, name='p8_test_6')

        self.assertFalse(find_isomorphic_graph_p7_p8(graph, expected_graph))

    def test_7(self):
        uid = 0
        level = 0
        graph = p8.make_mock_graph(uid, level)
        nodes = graph._node
        nodes.get(uid+7)['x'] = 111
        expected_graph = basic_expected_graph(uid, level)

        p8.p8(graph, level)
        draw_graph(graph, name='p8_test_7')

        self.assertFalse(find_isomorphic_graph_p7_p8(graph, expected_graph))

    def test_8(self):
        uid = 0
        level = 0

        new_nodes = [
            Node(id=uid+111, label='i', x=-10, y=10, level=level+1).graph_adapter(),
            Node(id=uid+222, label='i', x=-25, y=35, level=level+1).graph_adapter(),
            Node(id=uid+333, label='I', x=85, y=35, level=level+2).graph_adapter(),
            Node(id=uid+444, label='I', x=40, y=60, level=level+2).graph_adapter(),
        ]

        new_edges = [
            (uid+111, uid+5), (uid+222, uid+5),
            (uid+333, uid+14), (uid+444, uid+16)
        ]

        graph = p8.make_mock_graph(uid, level)
        graph.add_nodes_from(new_nodes)
        graph.add_edges_from(new_edges)

        expected_graph = basic_expected_graph(uid, level)
        expected_graph.add_nodes_from(new_nodes)
        expected_graph.add_edges_from(new_edges)

        print(p8.p8(graph, level))
        draw_graph(graph, name='p8_test_8')

        self.assertTrue(find_isomorphic_graph_p7_p8(graph, expected_graph))


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
