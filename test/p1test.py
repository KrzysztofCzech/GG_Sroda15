from re import A
import unittest
import networkx as nx
from classes import Node
from productions.p1 import p1

class P1Test(unittest.TestCase):

    def test_P1(self):
        graph = nx.Graph()
        graph.add_nodes_from([Node(0, label='El', x=0, y=0).graph_adapter()])
        p1(graph)

        self.assertEqual(list(graph.nodes), list(range(0,7)))
        self.assertEqual(graph._node, {0: {'label': 'el', 'x': 0, 'y': 0}, 1: {'label': 'I', 'x': 33.333333333333336, 'y': 33.333333333333336}, 2: {'label': 'I', 'x': 16.666666666666668, 'y': 30.0}, 3: {'label': 'E', 'x': 10.0, 'y': 10.0}, 4: {'label': 'E', 'x': 40.0, 'y': 10.0}, 5: {'label': 'E', 'x': 40.0, 'y': 40.0}, 6: {'label': 'E', 'x': 10.0, 'y': 40.0}})