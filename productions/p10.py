import networkx as nx
from classes import Node, Attr_MAP
from utils import compare_nodes, with_offset

from pprint import pprint


def make_left_side_graph(uid: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()
    left_side_graph.add_nodes_from([
        Node(uid, label='E', level=level).graph_adapter(),
        Node(uid + 1, label='E', level=level).graph_adapter(),
        Node(uid + 2, label='i', level=level).graph_adapter(),
        Node(uid + 3, label='i', level=level).graph_adapter(),

        Node(uid + 4, label='E', level=level+1).graph_adapter(),
        Node(uid + 5, label='E', level=level+1).graph_adapter(),
        Node(uid + 6, label='E', level=level+1).graph_adapter(),
        Node(uid + 7, label='I', level=level+1).graph_adapter(),
        Node(uid + 8, label='I', level=level+1).graph_adapter(),

        Node(uid + 9, label='E', level=level+1).graph_adapter(),
        Node(uid + 10, label='E', level=level+1).graph_adapter(),
        Node(uid + 11, label='I', level=level+1).graph_adapter(),
    ])

    left_side_graph.add_edges_from(with_offset([
        (0, 1),
        (1, 2),
        (2, 0),
        (0, 3),
        (1, 3),

        (4, 5),
        (5, 6),
        (7, 4),
        (7, 5),
        (8, 5),
        (8, 6),

        (9, 10),
        (10, 11),
        (9, 11),

        (2, 7),
        (2, 8),
        (3, 11)
    ], uid))

    return left_side_graph


def check_predicate(graph: nx.Graph, mapping: dict, uid: int) -> bool:
    tested_nodes = [graph._node[mapping[uid + i]] for i in range(0, 11)]

    x_diff_1 = (tested_nodes[4]['x'] + tested_nodes[6]
                ['x']) * 0.5 - tested_nodes[5]['x']
    y_diff_1 = (tested_nodes[4]['y'] + tested_nodes[6]
                ['y']) * 0.5 - tested_nodes[5]['y']
    x_diff_2 = tested_nodes[4]['x'] - tested_nodes[9]['x']
    y_diff_2 = tested_nodes[4]['y'] - tested_nodes[9]['y']

    x_diff_3 = tested_nodes[6]['x'] - tested_nodes[10]['x']
    y_diff_3 = tested_nodes[6]['y'] - tested_nodes[10]['y']

    return x_diff_1 == 0 and y_diff_1 == 0 and x_diff_2 == 0 and y_diff_2 == 0 and x_diff_3 == 0 and y_diff_3 == 0


def find_isomorphic_graph(graph: nx.Graph, left_side_graph: nx.Graph, uid: int) -> dict:
    isomorphic_g = []

    graphs_found = nx.algorithms.isomorphism.GraphMatcher(
        graph,
        left_side_graph,
        node_match=compare_nodes
    )

    for g in graphs_found.subgraph_isomorphisms_iter():
        mapping = {v: k for k, v in g.items()}

        if check_predicate(graph, mapping, uid):
            isomorphic_g.append(mapping)

    return None if len(isomorphic_g) == 0 else isomorphic_g[0]


def make_right_side_nodes_and_edges(graph: nx.Graph, mapping: dict, uid: int, level: int):
    new_edges = []

    to_merge_ids_1 = [mapping[uid+4], mapping[uid+9]]
    to_merge_ids_2 = [mapping[uid+6], mapping[uid+10]]

    mapping = dict(sorted(mapping.items()))

    # pprint(mapping)

    # get all edges connected to to_merge_ids_1[1] where the other node is not mapping[uid+10] or mapping[uid+11]
    edges_to_merge_1 = [edge for edge in graph.edges if edge[0] == to_merge_ids_1[1] and edge[1] != mapping[uid+10] and edge[1] != mapping[uid+11] or
                        edge[1] == to_merge_ids_1[1] and edge[0] != mapping[uid+10] and edge[0] != mapping[uid+11]]

    # get all edges connected to to_merge_ids_2[1] where the other node is not mapping[uid+10] or mapping[uid+11]
    edges_to_merge_2 = [edge for edge in graph.edges if edge[0] == to_merge_ids_2[1] and edge[1] != mapping[uid+9] and edge[1] != mapping[uid+11] or
                        edge[1] == to_merge_ids_2[1] and edge[0] != mapping[uid+9] and edge[0] != mapping[uid+11]]

    # remove nodes to_merge_ids_1[1] and to_merge_ids_2[1]
    graph.remove_nodes_from([to_merge_ids_1[1], to_merge_ids_2[1]])

    # for each edges in edges_to_merge_1
    for edge in edges_to_merge_1:
        if edge[0] == to_merge_ids_1[1]:
            new_edges.append((mapping[uid+4], edge[1]))
        else:
            new_edges.append((edge[0], mapping[uid+4]))

    for edge in edges_to_merge_2:
        if edge[0] == to_merge_ids_2[1]:
            new_edges.append((mapping[uid+6], edge[1]))
        else:
            new_edges.append((edge[0], mapping[uid+6]))

    new_edges.append((mapping[uid+6], mapping[uid+11]))
    new_edges.append((mapping[uid+4], mapping[uid+11]))

    graph.add_edges_from([(edge[0], edge[1])
                         for edge in new_edges])


def p10(graph: nx.Graph, level) -> bool:
    unique_id = 10000
    left_graph = make_left_side_graph(unique_id, level)
    isomorphic_mapping = find_isomorphic_graph(graph, left_graph, unique_id)
    if isomorphic_mapping is None:
        return False
    make_right_side_nodes_and_edges(
        graph, isomorphic_mapping, unique_id, level)
    return True
