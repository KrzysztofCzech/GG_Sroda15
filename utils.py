import networkx as nx
from classes import Attr_MAP


def compare_nodes(node1, node2):
    return node1[Attr_MAP.label] == node2[Attr_MAP.label] and node1[Attr_MAP.level] == node2[Attr_MAP.level]

# find graphs on which production can be made and inversed result form GraphMatcher


def find_isomorphic_graph(graph: nx.Graph, left_side_graph: nx.Graph) -> dict:
    isomorphic_g = []

    graphs_found = nx.algorithms.isomorphism.GraphMatcher(
        graph,
        left_side_graph,
        node_match=compare_nodes)

    for graph in graphs_found.subgraph_isomorphisms_iter():
        inversed = {v: k for k, v in graph.items()}
        isomorphic_g.append(inversed)
    try:
        return isomorphic_g[0]
    except IndexError as e:
        print('No isomorphic graph found')
        raise e


def update_graph(
    graph: nx.Graph,
    isomorphic_mapping: dict,
    right_side_parent_node: tuple,
    right_side_nodes_new: list,
    right_side_edges: list
):

    temp_id = right_side_parent_node.id

    # print(graph._node[temp_id_mapped])
    n = len(graph.nodes) - 1

    right_side_nodes_mapping = {
        node.id: node.id + n for node in right_side_nodes_new}

    for k, v in isomorphic_mapping.items():
        right_side_nodes_mapping[k] = v

    for i in range(len(right_side_nodes_new)):
        if right_side_nodes_new[i].id not in isomorphic_mapping.keys():
            right_side_nodes_new[i].id = right_side_nodes_new[i].id + n
        else:
            right_side_nodes_new[i].id = isomorphic_mapping[right_side_nodes_new[i].id]

    right_side_edges_mapped = list(
        map(lambda edge: (right_side_nodes_mapping[edge[0]], right_side_nodes_mapping[edge[1]]), right_side_edges))

    graph.add_nodes_from([node.graph_adapter()
                         for node in right_side_nodes_new])
    graph.add_edges_from(right_side_edges_mapped)


def with_offset(arg: list[tuple[int, int]], offset):
    return [(v1+offset, v2+offset) for (v1, v2) in arg]
