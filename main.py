import networkx as nx
from draw import draw_graph
from productions.p1 import p1
from productions.p2 import p2
from productions.p9 import p9
from productions.p10 import p10

from classes import Node, Attr_MAP


if __name__ == '__main__':

    graph = nx.Graph()
    graph.add_nodes_from([Node(0, label='El', x=0, y=0, level = 0).graph_adapter()])

    p1(graph, 0)
    print(graph._node)
    p2(graph, 1)
    # p2(graph, 1)
    p9(graph, 1)

    draw_graph(graph, name='production2')
    p10(graph, 1)

    print(graph._node)
    draw_graph(graph, name='production2')
