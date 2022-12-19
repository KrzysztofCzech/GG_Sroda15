import networkx as nx
from classes import Node, Attr_MAP
from utils import find_isomorphic_graph, update_graph


def make_left_side_graph(unique_id: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()
    left_side_graph.add_nodes_from([
        Node(id=unique_id, label="i", level=level).graph_adapter(),
        Node(id=unique_id + 2, label="i", level=level).graph_adapter(),
        Node(id=unique_id + 1, label="E", level=level).graph_adapter(),
        Node(id=unique_id + 3, label="E", level=level).graph_adapter(),

        Node(id=unique_id + 4, label="I", level=level + 1).graph_adapter(),
        Node(id=unique_id + 5, label="I", level=level + 1).graph_adapter(),
        Node(id=unique_id + 6, label="E", level=level + 1).graph_adapter(),
        Node(id=unique_id + 7, label="E", level=level + 1).graph_adapter(),
        Node(id=unique_id + 8, label="E", level=level + 1).graph_adapter(),

        Node(id=unique_id + 9, label="I", level=level + 1).graph_adapter(),
        Node(id=unique_id + 10, label="I", level=level + 1).graph_adapter(),
        Node(id=unique_id + 11, label="E", level=level + 1).graph_adapter(),
        Node(id=unique_id + 12, label="E", level=level + 1).graph_adapter(),
        Node(id=unique_id + 13, label="E", level=level + 1).graph_adapter(),
    ])

    left_side_graph.add_edges_from([
        (unique_id, unique_id + 1),
        (unique_id, unique_id + 3),
        (unique_id + 2, unique_id + 1),
        (unique_id + 2, unique_id + 3),
        (unique_id + 1, unique_id + 3), 

        (unique_id, unique_id + 4),
        (unique_id, unique_id + 5),

        (unique_id + 2, unique_id + 9),
        (unique_id + 2, unique_id + 10),

        (unique_id + 4, unique_id + 6),
        (unique_id + 4, unique_id + 7),

        (unique_id + 5, unique_id + 7),
        (unique_id + 5, unique_id + 8),

        (unique_id + 6, unique_id + 7),
        (unique_id + 7, unique_id + 8),

        (unique_id + 9, unique_id + 11),
        (unique_id + 9, unique_id + 12),

        (unique_id + 10, unique_id + 12),
        (unique_id + 10, unique_id + 13),

        (unique_id + 11, unique_id + 12),
        (unique_id + 12, unique_id + 13),

    ])

    return left_side_graph


def update_x_y_coords(graph: nx.Graph, mapping: dict) -> tuple[list, list]:
    x_coords = []
    y_coords = []
    for _, node in mapping.items():
        if graph.nodes[node][Attr_MAP.label] == 'E':
            x_coords.append(graph.nodes[node][Attr_MAP.x])
            y_coords.append(graph.nodes[node][Attr_MAP.y])

    return x_coords, y_coords


def make_right_side_nodes_and_edges(unique_id: int, coords: tuple[list, list], level) -> tuple[list[Node], list, Node]:
    print(coords)
    x, y = coords

    parent_node = Node(id=unique_id, label='i', x=(x[0] + x[1] + x[2]) / 3, y=(y[0] + y[1] + y[2]) / 3, level=level + 1)
    right_nodes = [
        Node(id=1, label='I', x=(x[0] + x[5] + x[1]) / 3, y=(y[0] + y[1] + y[5]) / 3, level=level + 1),
        Node(id=2, label='I',
             x=((x[1] + x[2] + x[3]) / 3) - (((x[1] + x[2] + x[3]) / 3) * 0.1),
             y=((y[1] + y[2] + y[3]) / 3) + (((y[1] + y[2] + y[3]) / 3) * 0.1),
             level=level + 1),
        Node(id=3, label='I',
             x=((x[2] + x[3] + x[5]) / 3) + (((x[2] + x[3] + x[5]) / 3) * 0.1),
             y=((y[2] + y[3] + y[5]) / 3) - (((y[2] + y[3] + y[5]) / 3) * 0.1),
             level=level + 1),
        Node(id=4, label='I', x=(x[3] + x[4] + x[5]) / 3, y=(y[3] + y[4] + y[5]) / 3, level=level + 1),

        Node(id=5, label='E', x=x[0], y=y[0], level=level + 1),
        Node(id=7, label='E', x=x[2], y=y[2], level=level + 1),
        Node(id=9, label='E', x=x[4], y=y[4], level=level + 1),

        Node(id=6, label='E', x=x[1], y=y[1], level=level + 1),
        Node(id=8, label='E', x=x[3], y=y[3], level=level + 1),
        Node(id=10, label='E', x=x[5], y=y[5], level=level + 1),

    ]

    edges = [
        (unique_id, 1),
        (unique_id, 2),
        (unique_id, 3),
        (unique_id, 4),

        (1, 5),
        (1, 6),
        (1, 10),
        (2, 6),
        (2, 7),
        (2, 10),
        (3, 7),
        (3, 8),
        (3, 10),
        (4, 8),
        (4, 9),
        (4, 10),

        (5, 6),
        (6, 7),
        (7, 8),
        (8, 9),
        (9, 10),
        (10, 5),
    ]

    return right_nodes, edges, parent_node


def p6(graph: nx.Graph, level):
    unique_id = 555  # id that will be match egde from left side to right side production graph be used must be higher than max number of id used
    left_graph = make_left_side_graph(unique_id, level)
    isomorphic_mapping = find_isomorphic_graph(graph, left_graph)
    right_side_nodes, right_side_edges, right_unique_node = make_right_side_nodes_and_edges(
        unique_id, update_x_y_coords(graph, isomorphic_mapping), level)
    update_graph(graph, isomorphic_mapping, right_unique_node,
                 right_side_nodes, right_side_edges)
