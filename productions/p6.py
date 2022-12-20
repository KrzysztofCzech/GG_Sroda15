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


def merge_nodes(unique_id: int, mapping: dict, graph: nx.Graph):
    adj = graph.adj
    nodes = graph.nodes

    nodes_to_join_list = [
        (unique_id + 12, unique_id + 7),
    ]
    
    candidate_left_1 = nodes[mapping[unique_id + 6]]
    candidate_right_1 = nodes[mapping[unique_id + 13]]
    candidate_right_2 = nodes[mapping[unique_id + 11]]
    
    candidate_mid = nodes[mapping[unique_id + 12]]
    
    if candidate_mid["x"] != (candidate_right_1["x"] + candidate_right_2["x"]) / 2 \
            or candidate_mid["y"] != (candidate_right_1["y"] + candidate_right_2["y"]) / 2:
        return    
    
    if candidate_left_1["x"] == candidate_right_1["x"] and candidate_left_1["y"] == candidate_right_1["y"]:
        nodes_to_join_list += [
            (unique_id + 6, unique_id + 13),
            (unique_id + 8, unique_id + 11),
        ]
    else:
        nodes_to_join_list += [
            (unique_id + 8, unique_id + 13),
            (unique_id + 6, unique_id + 11),
        ]

    for nodes_to_join in nodes_to_join_list:
        left_real_id = mapping[nodes_to_join[0]]
        right_real_id = mapping[nodes_to_join[1]]

        left_node = nodes[left_real_id]
        right_node = nodes[right_real_id]

        same_pos = left_node["x"] == right_node["x"] and left_node["y"] == right_node["y"] and left_node["level"] == right_node["level"]
        if not same_pos or left_node["label"] != right_node["label"]:
            return

    for nodes_to_join in nodes_to_join_list:
        left_real_id = mapping[nodes_to_join[0]]
        right_real_id = mapping[nodes_to_join[1]]
        
        lonely_nodes = adj[left_real_id]
        
        for lonely_node_id in lonely_nodes:
            graph.add_edge(right_real_id, lonely_node_id)
            
        graph.remove_node(left_real_id)


def p6(graph: nx.Graph, level):
    unique_id = 555  # id that will be match egde from left side to right side production graph be used must be higher than max number of id used
    left_graph = make_left_side_graph(unique_id, level)
    isomorphic_mapping = find_isomorphic_graph(graph, left_graph)

    merge_nodes(unique_id, isomorphic_mapping, graph)
