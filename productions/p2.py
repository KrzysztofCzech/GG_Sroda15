import networkx as nx
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


# def check_predicate(graph: nx.Graph, mapping: dict, uid: int) -> bool:
#     tested_nodes = [graph._node[mapping[uid + i]] for i in range(1, 4)]
#
#     edge_1 = ((tested_nodes[0]['x'] - tested_nodes[1]['x']) ** 2 + (tested_nodes[0]['y'] - tested_nodes[1]['y']) ** 2) ** 0.5
#     edge_2 = ((tested_nodes[1]['x'] - tested_nodes[2]['x']) ** 2 + (tested_nodes[1]['y'] - tested_nodes[2]['y']) ** 2) ** 0.5
#     edge_3 = ((tested_nodes[0]['x'] - tested_nodes[2]['x']) ** 2 + (tested_nodes[0]['y'] - tested_nodes[2]['y']) ** 2) ** 0.5
#
#     return edge_1 >= edge_2 and edge_1 >= edge_3


# def find_isomorphic_graph(graph: nx.Graph, left_side_graph: nx.Graph, uid: int) -> dict:
#     isomorphic_g = []
#
#     graphs_found = nx.algorithms.isomorphism.GraphMatcher(
#         graph,
#         left_side_graph,
#         node_match=compare_nodes
#     )
#
#     for g in graphs_found.subgraph_isomorphisms_iter():
#         mapping = {v: k for k, v in g.items()}
#
#         if check_predicate(graph, mapping, uid):
#             isomorphic_g.append(mapping)
#
#     return None if len(isomorphic_g) == 0 else isomorphic_g[0]


def update_x_y_coords(graph: nx.Graph, mapping: dict) -> tuple[list, list]:
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


def make_right_side_nodes_and_edges(unique_id: int, coords: tuple[list, list], level) -> tuple[list[Node], list, Node]:
    x = coords[0]
    y = coords[1]

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
