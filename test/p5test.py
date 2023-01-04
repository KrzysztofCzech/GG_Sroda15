import unittest
import networkx as nx
from classes import Node
from draw import draw_graph
from productions.p5 import p5


class P5Test(unittest.TestCase):
    production_name = 'productionP5'

    def test_no_production(self):
        test_name = 'test1'
        graph = nx.Graph()
        graph.add_nodes_from([Node(0, label='El', x=0, y=0).graph_adapter()])
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-1')

        self.assertEqual(list(graph.nodes), [0])
        self.assertEqual(graph._node, {0: {'label': 'El', "level": 0, 'x': 0, 'y': 0}})
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-2')

    def test_production_success(self):
        test_name = 'test2'
        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=6, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1),
            (0, 3),
            (0, 5),

            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 1),
        ])
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-1')
        p5(graph, 0)
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-2')

        self.assertEqual(len(list(graph.nodes)), 17)

        self.assertTrue(graph.has_edge(0, 13))
        self.assertTrue(graph.has_edge(0, 14))
        self.assertTrue(graph.has_edge(0, 15))
        self.assertTrue(graph.has_edge(0, 16))

        self.assertTrue(graph.has_edge(13, 7))
        self.assertTrue(graph.has_edge(13, 8))
        self.assertTrue(graph.has_edge(13, 12))

        self.assertTrue(graph.has_edge(14, 8))
        self.assertTrue(graph.has_edge(14, 9))
        self.assertTrue(graph.has_edge(14, 12))

        self.assertTrue(graph.has_edge(15, 9))
        self.assertTrue(graph.has_edge(15, 10))
        self.assertTrue(graph.has_edge(15, 12))

        self.assertTrue(graph.has_edge(16, 10))
        self.assertTrue(graph.has_edge(16, 11))
        self.assertTrue(graph.has_edge(16, 12))

        self.assertTrue(graph.has_edge(7, 8))
        self.assertTrue(graph.has_edge(8, 9))
        self.assertTrue(graph.has_edge(9, 10))
        self.assertTrue(graph.has_edge(10, 11))
        self.assertTrue(graph.has_edge(11, 12))
        self.assertTrue(graph.has_edge(12, 7))
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-2')

    def test_production_success_with_lonely_nodes(self):
        test_name = 'test3'

        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=6, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
            Node(id=7, label="L", level=0, x=0.5, y=1.8).graph_adapter(),
            Node(id=8, label="L", level=0, x=0.7, y=2.2).graph_adapter(),
            Node(id=9, label="L", level=0, x=0.2, y=2.2).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1),
            (0, 3),
            (0, 5),

            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (9, 2),
            (6, 1),
            (9, 8),
            (7, 8),
            (7, 6),
        ])
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-1')
        p5(graph, 0)
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-2')
        self.assertEqual(len(list(graph.nodes)), 20)

        self.assertTrue(graph.has_edge(0, 13 + 3))
        self.assertTrue(graph.has_edge(0, 14 + 3))
        self.assertTrue(graph.has_edge(0, 15 + 3))
        self.assertTrue(graph.has_edge(0, 16 + 3))

        self.assertTrue(graph.has_edge(13 + 3, 7 + 3))
        self.assertTrue(graph.has_edge(13 + 3, 8 + 3))
        self.assertTrue(graph.has_edge(13 + 3, 12 + 3))

        self.assertTrue(graph.has_edge(14 + 3, 8 + 3))
        self.assertTrue(graph.has_edge(14 + 3, 9 + 3))
        self.assertTrue(graph.has_edge(14 + 3, 12 + 3))

        self.assertTrue(graph.has_edge(15 + 3, 9 + 3))
        self.assertTrue(graph.has_edge(15 + 3, 10 + 3))
        self.assertTrue(graph.has_edge(15 + 3, 12 + 3))

        self.assertTrue(graph.has_edge(16 + 3, 10 + 3))
        self.assertTrue(graph.has_edge(16 + 3, 11 + 3))
        self.assertTrue(graph.has_edge(16 + 3, 12 + 3))

        self.assertTrue(graph.has_edge(7 + 3, 8 + 3))
        self.assertTrue(graph.has_edge(8 + 3, 9 + 3))
        self.assertTrue(graph.has_edge(9 + 3, 10 + 3))
        self.assertTrue(graph.has_edge(10 + 3, 11 + 3))
        self.assertTrue(graph.has_edge(11 + 3, 12 + 3))
        self.assertTrue(graph.has_edge(12 + 3, 7 + 3))

    def test_production_wrong_edge(self):
        test_name = 'test4'

        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=6, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1),
            (0, 3),
            (0, 5),

            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            # (6, 1),
        ])
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-1')
        self.assertEqual(len(list(graph.nodes)), 7)

        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-2')

    def test_production_wrong_node(self):
        test_name = 'test5'

        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            # Node(id=6, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
        ])

        graph.add_edges_from([
            (0, 1),
            (0, 3),
            (0, 5),

            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            # (5, 6),
            # (6, 1),
        ])
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-1')
        self.assertEqual(len(list(graph.nodes)), 6)
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-2')

    def test_production_wrong_position_1(self):
        test_name = 'test6'

        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.6).graph_adapter(),
            Node(id=3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=6, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
        ])
        graph.add_edges_from([
            (0, 1),
            (0, 3),
            (0, 5),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 1),
        ])
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-1')
        p5(graph, 0)
        self.assertEqual(len(list(graph.nodes)), 7)
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-2')

    def test_production_wrong_position_2(self):
        test_name = 'test7'

        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4, label="E", level=0, x=0.6, y=0.0).graph_adapter(),
            Node(id=5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=6, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
        ])
        graph.add_edges_from([
            (0, 1),
            (0, 3),
            (0, 5),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 1),
        ])
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-1')
        p5(graph, 0)
        self.assertEqual(len(list(graph.nodes)), 7)
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-2')

    def test_production_wrong_position_3(self):
        test_name = 'test8'

        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=6, label="E", level=0, x=0.6, y=0.6).graph_adapter(),
        ])
        graph.add_edges_from([
            (0, 1),
            (0, 3),
            (0, 5),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (6, 1),
        ])
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-1')
        p5(graph, 0)
        self.assertEqual(len(list(graph.nodes)), 7)
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-2')

    def test_production_success_with_changed_numeration(self):
        test_name = 'test9'

        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0 + 1, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1 + 1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2 + 1, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3 + 1, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4 + 1, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5 + 1, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=6 + 1, label="E", level=0, x=0.5, y=0.5).graph_adapter(),
        ])

        graph.add_edges_from([
            (0 + 1, 1 + 1),
            (0 + 1, 3 + 1),
            (0 + 1, 5 + 1),

            (1 + 1, 2 + 1),
            (2 + 1, 3 + 1),
            (3 + 1, 4 + 1),
            (4 + 1, 5 + 1),
            (5 + 1, 6 + 1),
            (6 + 1, 1 + 1),
        ])
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-1')
        p5(graph, 0)
        print(list(graph.nodes))
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-2')
        self.assertEqual(len(list(graph.nodes)), 17)

    def test_production_success_with_changed_label(self):
        test_name = 'test10'

        graph = nx.Graph()
        graph.add_nodes_from([
            Node(id=0 + 1, label="I", level=0, x=0.33, y=0.33).graph_adapter(),
            Node(id=1 + 1, label="E", level=0, x=0.0, y=1.0).graph_adapter(),
            Node(id=2 + 1, label="E", level=0, x=0.0, y=0.5).graph_adapter(),
            Node(id=3 + 1, label="E", level=0, x=0.0, y=0.0).graph_adapter(),
            Node(id=4 + 1, label="E", level=0, x=0.5, y=0.0).graph_adapter(),
            Node(id=5 + 1, label="E", level=0, x=1.0, y=0.0).graph_adapter(),
            Node(id=6 + 1, label="I", level=0, x=0.5, y=0.5).graph_adapter(),
        ])

        graph.add_edges_from([
            (0 + 1, 1 + 1),
            (0 + 1, 3 + 1),
            (0 + 1, 5 + 1),

            (1 + 1, 2 + 1),
            (2 + 1, 3 + 1),
            (3 + 1, 4 + 1),
            (4 + 1, 5 + 1),
            (5 + 1, 6 + 1),
            (6 + 1, 1 + 1),
        ])
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-1')
        p5(graph, 0)
        self.assertEqual(len(list(graph.nodes)), 7)
        draw_graph(graph, name=f'{P5Test.production_name}-{test_name}-2')
