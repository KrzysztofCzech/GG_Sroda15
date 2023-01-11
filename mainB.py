import networkx as nx
from draw import draw_graph
from productions.p1 import p1
from productions.p2 import p2
from productions.p3 import p3
from productions.p9 import p9
from productions.p10 import p10
from productions.p12 import p12
from productions.p13 import p13

from classes import Node

if __name__ == '__main__':

    graph = nx.Graph()
    graph.add_nodes_from(
        [Node(0, label='El', x=0, y=0, level=0).graph_adapter()])

    draw_graph(graph, name='b-0', font_size=9, with_coords=True)

    p1(graph, 0)
    draw_graph(graph, name='b-1', font_size=9, with_coords=True)
# ---
    p2(graph, 1)
    draw_graph(graph, name='b-2', font_size=9, with_coords=True)
    draw_graph(graph, name='b-2_l2', font_size=9, with_coords=True, level=2)

    p9(graph, 1)
    draw_graph(graph, name='b-3', font_size=9, with_coords=True)
    draw_graph(graph, name='b-3_l2', font_size=9, with_coords=True, level=2)
# ---
    p10(graph, 1)
    draw_graph(graph, name='b-4', font_size=9, with_coords=True)
    draw_graph(graph, name='b-4_l2', font_size=9, with_coords=True, level=2)
# ---
    p9(graph, 2)
    draw_graph(graph, name='b-5', font_size=9, with_coords=True)
    draw_graph(graph, name='b-5_l3', font_size=9, with_coords=True, level=3)

    p9(graph, 2)
    draw_graph(graph, name='b-6', font_size=9, with_coords=True)
    draw_graph(graph, name='b-6_l3', font_size=9, with_coords=True, level=3)

    p3(graph, 2)
    draw_graph(graph, name='b-7', font_size=9, with_coords=True)
    draw_graph(graph, name='b-7_l3', font_size=9, with_coords=True, level=3)
# ---
    p12(graph, 3)
    draw_graph(graph, name='b-8', font_size=9, with_coords=True)
    draw_graph(graph, name='b-8_l3', font_size=9, with_coords=True, level=3)

    p12(graph, 3)
    draw_graph(graph, name='b-9', font_size=9, with_coords=True)
    draw_graph(graph, name='b-9_l3', font_size=9, with_coords=True, level=3)
# ---
    p13(graph, 3)
    draw_graph(graph, name='b-10', font_size=9, with_coords=True)
    draw_graph(graph, name='b-10_l3', font_size=9, with_coords=True, level=3)
