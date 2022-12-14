import networkx as nx
from draw import draw_graph
from productions.p1 import p1
from productions.p2 import p2

from classes import Node, Attr_MAP


if __name__ == '__main__':

    graph = nx.Graph()
    graph.add_nodes_from([Node(0, label='El', x=0, y=0, level = 0).graph_adapter()])

    p1(graph, 0)
    print(graph._node)

    # graph.nodes[1][Attr_MAP.label] = "i"
    # graph.remove_edge(4,5)
    # # graph.add_nodes_from([Node(7, label='El', x=60, y=45, level = 1).graph_adapter()])
    # # graph.add_edges_from(((4,7),(5,7)))
    draw_graph(graph, name='production1')
    p2(graph, 1)
    # p2(graph, 1)

    print(graph._node)
    draw_graph(graph, name='production2')
