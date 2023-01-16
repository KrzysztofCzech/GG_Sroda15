from pprint import pprint

import networkx as nx
from draw import draw_graph
from productions.p1 import p1
from productions.p2 import p2
from productions.p3 import p3
from productions.p7 import p7
from productions.p9 import p9
from productions.p10 import p10
from productions.p12 import p12

from classes import Node

if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from([Node(0, label='El', x=0, y=0, level=0).graph_adapter()])

    p1(graph, 0)
    draw_graph(graph, name='task-d-01')

    draw_graph(graph, name='task-d-02-00', level=[1,2])
    p2(graph, 1)
    draw_graph(graph, name='task-d-02-01-p02', level=[1,2])
    p9(graph, 1)
    draw_graph(graph, name='task-d-02-02-p09', level=[1,2])
    draw_graph(graph, name='task-d-02')

    draw_graph(graph, name='task-d-03-00', level=[1,2])
    p10(graph, 1)
    draw_graph(graph, name='task-d-03-01-p10', level=[1,2])
    draw_graph(graph, name='task-d-03')

    draw_graph(graph, name='task-d-04-00', level=[2,3])
    p2(graph, 2)
    draw_graph(graph, name='task-d-04-01-p02', level=[2,3])
    p2(graph, 2)
    draw_graph(graph, name='task-d-04-02-p02', level=[2,3])
    p3(graph, 2)
    draw_graph(graph, name='task-d-04-03-p03', level=[2,3])

    graph.add_edges_from([(12, 16)])

    draw_graph(graph, name='task-d-04')

    draw_graph(graph, name='task-d-05-00', level=[2,3])
    p12(graph, 2)
    draw_graph(graph, name='task-d-05-01-p12', level=[2,3])
    p12(graph, 2)
    draw_graph(graph, name='task-d-05-02-p12', level=[2,3])
    draw_graph(graph, name='task-d-05')

    draw_graph(graph, name='task-d-06-00', level=[2,3])
    p7(graph, 1)
    draw_graph(graph, name='task-d-06-01-p07', level=[2,3])
    draw_graph(graph, name='task-d-06')
