import networkx as nx
from classes import Node, Attr_MAP
from utils import compare_nodes, with_offset


def make_left_side_graph(uid: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()
    left_side_graph.add_nodes_from([
        Node(uid, label='E', level=level).graph_adapter(),
        Node(uid + 1, label='E', level=level).graph_adapter(),
        Node(uid + 2, label='E', level=level).graph_adapter(),
        Node(uid + 3, label='I', level=level).graph_adapter()
    ])

    left_side_graph.add_edges_from(with_offset([
        (0, 1),
        (1, 2),
        (2, 0),
        (0, 3),
        (1, 3),
        (2, 3)
    ], uid))

    return left_side_graph


def check_predicate(graph: nx.Graph, mapping: dict, uid: int) -> bool:
    return True


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
    new_nodes = []
    parent_node_id = None

    for _left_node, node in mapping.items():
        if graph.nodes[node][Attr_MAP.label] == 'E':
            new_nodes.append({**graph.nodes[node], 'level': level + 1})
        else:
            parent_node_id = node

    new_x = (new_nodes[0]['x'] + new_nodes[1]['x'] + new_nodes[2]['x']) / 3
    new_y = (new_nodes[0]['y'] + new_nodes[1]['y'] + new_nodes[2]['y']) / 3
    new_nodes.append(
        {'label': 'I', 'x': new_x, 'y': new_y, 'level': level + 1})

    new_edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (0, 3),
        (1, 3),
        (2, 3)
    ]

    offset = max(graph.nodes) + 1
    graph.add_nodes_from([Node(offset + index, **node).graph_adapter()
                         for index, node in enumerate(new_nodes)])
    graph.add_edges_from(with_offset(new_edges, offset))

    graph.nodes[parent_node_id]['label'] = 'i'
    graph.add_edges_from([(parent_node_id, 3 + offset)])


def p9(graph: nx.Graph, level) -> bool:
    unique_id = 10000
    left_graph = make_left_side_graph(unique_id, level)
    isomorphic_mapping = find_isomorphic_graph(graph, left_graph, unique_id)
    if isomorphic_mapping is None:
        return False
    make_right_side_nodes_and_edges(
        graph, isomorphic_mapping, unique_id, level)
    return True
