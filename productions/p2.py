import networkx as nx
from typing import Tuple, List

from classes import Node, Attr_MAP
from utils import find_isomorphic_graph, update_graph


def make_left_side_graph(unique_id: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()
    left_side_graph.add_nodes_from([
        Node(id=unique_id, label="I", level=level).graph_adapter(),
        Node(id=unique_id + 1, label="E", level=level).graph_adapter(),
        Node(id=unique_id + 2, label="E", level=level).graph_adapter(),
        Node(id=unique_id + 3, label="E", level=level).graph_adapter(),
    ])

    left_side_graph.add_edges_from([
        (unique_id, unique_id + 1),
        (unique_id, unique_id + 2),
        (unique_id, unique_id + 3),
        (unique_id + 1, unique_id + 2),
        (unique_id + 1, unique_id + 3),
        (unique_id + 2, unique_id + 3),
    ])

    return left_side_graph


def update_x_y_coords(graph: nx.Graph, mapping: dict) -> Tuple[list, list]:
    x_coords = []
    y_coords = []
    nodes_id = []
    for left_node, node in mapping.items():
        if graph.nodes[node][Attr_MAP.label] == 'E':
            x_coords.append(graph.nodes[node][Attr_MAP.x])
            y_coords.append(graph.nodes[node][Attr_MAP.y])

    x_coords.append((x_coords[1] + x_coords[2]) / 2)
    y_coords.append((y_coords[1] + y_coords[2]) / 2)

    return x_coords, y_coords


def make_right_side_nodes_and_edges(unique_id: int, coords: Tuple[list, list], level) -> Tuple[List[Node], list, Node]:
    x = coords[0]
    y = coords[1]
    print(x)
    print(y)

    parent_node = Node(id=unique_id, label='i', x=(x[0] + x[1] + x[2]) / 3, y=(y[0] + y[1] + y[2]) / 3, level=level)
    right_nodes = [
        Node(id=1, label='I', x=(x[0] + x[1] + x[3]) / 3, y=(y[0] + y[1] + y[3]) / 3, level=level + 1),
        Node(id=2, label='I', x=(x[0] + x[2] + x[3]) / 3, y=(y[0] + y[2] + y[3]) / 3, level=level + 1),
        Node(id=3, label='E', x=x[0], y=y[0], level=level + 1),
        Node(id=4, label='E', x=x[1], y=y[1], level=level + 1),
        Node(id=5, label='E', x=x[2], y=y[2], level=level + 1),
        Node(id=6, label='E', x=x[3], y=y[3], level=level + 1)
    ]

    nodes = [parent_node] + right_nodes

    edges = [
        (unique_id, 1), (unique_id, 2),
        (1, 3), (1, 4), (1, 6), (2, 3), (2, 5), (2, 6),
        (3, 4), (3, 5), (3, 6), (4, 6), (5, 6)
    ]

    return nodes, edges, parent_node


def p2(graph: nx.Graph, level):
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
