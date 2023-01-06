import networkx as nx
from typing import Tuple, List

from classes import Node, Attr_MAP
from utils import find_isomorphic_graph, update_graph


def make_left_side_graph(unique_id: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()
    left_side_graph.add_nodes_from([Node(id=unique_id, label='El', level=level).graph_adapter()])

    return left_side_graph


def update_x_y_coords(graph: nx.Graph, mapping: dict) -> Tuple[list, list]:
    x_coords = []
    y_coords = []

    for _, node in mapping.items():
        x_coords.append(graph.nodes[node][Attr_MAP.x])
        y_coords.append(graph.nodes[node][Attr_MAP.y])

    return x_coords, y_coords


def make_right_side_nodes_and_edges(unique_id: int, coords: Tuple[list, list], level) -> Tuple[List[Node], list, Node]:
    upper = 30
    lower = 0
    x = coords[0]
    y = coords[1]
    parent_node = Node(id=unique_id, label='el', x=x[0], y=y[0], level=level)
    right_nodes = [
        Node(id=1, label='I', x=(lower * 2 + upper) / 3 + x[0], y=(lower * 2 + upper) / 3 + y[0], level=level + 1),
        Node(id=2, label='I', x=(lower + upper * 2) / 3 + x[0], y=(lower + upper * 2) / 3 + y[0], level=level + 1),
        Node(id=3, label='E', x=lower + x[0], y=lower + y[0], level=level + 1),
        Node(id=4, label='E', x=upper + x[0], y=lower + y[0], level=level + 1),
        Node(id=5, label='E', x=upper + x[0], y=upper + y[0], level=level + 1),
        Node(id=6, label='E', x=lower + x[0], y=upper + y[0], level=level + 1)
    ]

    nodes = [parent_node] + right_nodes

    edges = [
        (unique_id, 1), (unique_id, 2), (3, 4), (3, 6), (3, 1), (4, 5), (4, 6), (4, 1), (4, 2), (5, 2), (5, 6), (6, 1),
        (6, 2),
    ]

    return nodes, edges, parent_node


def p1(graph: nx.Graph, level):
    unique_id = 555  # id that will be match egde from left side to right side production graph be used must be higher than max number of id used
    left_graph = make_left_side_graph(unique_id, level)
    isomorphic_mapping = find_isomorphic_graph(graph, left_graph)

    if isomorphic_mapping is None:
        return False

    right_side_nodes, right_side_edges, right_unique_node = make_right_side_nodes_and_edges(unique_id,
                                                                                            update_x_y_coords(graph,
                                                                                                              isomorphic_mapping),
                                                                                            level)

    update_graph(graph, isomorphic_mapping, right_unique_node, right_side_nodes, right_side_edges)

    return True
