import networkx as nx
from draw import draw_graph
from productions.p9 import p9
from productions.p1 import p1

from classes import Node

if __name__ == '__main__':

    graph = nx.Graph()
    graph.add_nodes_from(
        [Node(0, label='El', x=0, y=0, level=0).graph_adapter()])

    p1(graph, 0)

    draw_graph(graph, name='prod9-0', font_size=9, with_coords=True)
    p9(graph, 1)
    draw_graph(graph, name='prod9-1', font_size=9, with_coords=True)
    p9(graph, 1)
    draw_graph(graph, name='prod9-2', font_size=9, with_coords=True)
    p9(graph, 2)
    draw_graph(graph, name='prod9-3', font_size=9, with_coords=True)
