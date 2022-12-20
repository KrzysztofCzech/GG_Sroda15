import networkx as nx
from classes import Node, Attr_MAP
from utils import find_isomorphic_graph, is_almost_equal, update_graph

unique_id = 500  # id that will be match egde from left side to right side production graph be used must be higher than max number of id used


def make_left_side_graph(uid: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()
    left_side_graph.add_nodes_from([
        Node(id=uid+0, label="i", level=level).graph_adapter(),
        Node(id=uid+1, label="i", level=level).graph_adapter(),
        Node(id=uid+2, label="E", level=level).graph_adapter(),
        Node(id=uid+3, label="E", level=level).graph_adapter(),

        Node(id=uid+4, label="I", level=level+1).graph_adapter(),
        Node(id=uid+5, label="I", level=level+1).graph_adapter(),
        Node(id=uid+6, label="I", level=level+1).graph_adapter(),

        Node(id=uid+7, label="E", level=level+1).graph_adapter(),
        Node(id=uid+8, label="E", level=level+1).graph_adapter(),
        Node(id=uid+9, label="E", level=level+1).graph_adapter(),
        Node(id=uid+10, label="E", level=level+1).graph_adapter(),
        Node(id=uid+11, label="E", level=level+1).graph_adapter(),
    ])

    left_side_graph.add_edges_from([
        (uid+0, uid+2),
        (uid+0, uid+3),
        (uid+2, uid+3),
        (uid+1, uid+2),
        (uid+1, uid+3),

        (uid+0, uid+4),
        (uid+0, uid+5),
        (uid+4, uid+7),
        (uid+4, uid+8),
        (uid+7, uid+8),
        (uid+5, uid+8),
        (uid+9, uid+8),
        (uid+5, uid+9),

        (uid+1, uid+6),
        (uid+6, uid+10),
        (uid+6, uid+11),
        (uid+10, uid+11),
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


# Merge two nodes in graph, merge edges as well
def merge_nodes(graph: nx.Graph, node1_id: int, node2_id: int):
    node1 = graph.nodes[node1_id]
    node2 = graph.nodes[node2_id]

    # update node1
    graph.nodes[node1_id][Attr_MAP.x] = (
        node1[Attr_MAP.x] + node2[Attr_MAP.x]) / 2
    graph.nodes[node1_id][Attr_MAP.y] = (
        node1[Attr_MAP.y] + node2[Attr_MAP.y]) / 2

    # merge edges
    for edge in graph.edges(node2_id):
        if edge[0] == node2_id:
            graph.add_edge(node1_id, edge[1])
        else:
            graph.add_edge(edge[0], node1_id)

    # remove node2
    graph.remove_node(node2_id)


def make_right_side_nodes_and_edges(graph: nx.Graph, mapping: dict, uid: int, level: int):
    merge_nodes(graph, 9, 11)
    merge_nodes(graph, 7, 10)


def check_if_subgraph_match_p10(found_subgraph, graph: nx.Graph):
    # vertices 3 and 11 from left side must have the same position
    if not is_almost_equal(graph.nodes[found_subgraph[unique_id+3]][Attr_MAP.x], graph.nodes[found_subgraph[unique_id+11]][Attr_MAP.x]) \
            or not is_almost_equal(graph.nodes[found_subgraph[unique_id+3]][Attr_MAP.y], graph.nodes[found_subgraph[unique_id+11]][Attr_MAP.y]):
        return False

    # vertices 7 and 10 from left side must have the same position
    if not is_almost_equal(graph.nodes[found_subgraph[unique_id+7]][Attr_MAP.x], graph.nodes[found_subgraph[unique_id+10]][Attr_MAP.x]) \
            or not is_almost_equal(graph.nodes[found_subgraph[unique_id+7]][Attr_MAP.y], graph.nodes[found_subgraph[unique_id+10]][Attr_MAP.y]):
        return False

    return True


def selector(subgraphs, graph: nx.Graph):
    subgraphs = [subgraph for subgraph in subgraphs if
                 check_if_subgraph_match_p10(subgraph, graph)]
    if (len(subgraphs) == 0):
        return None
    return subgraphs[0]


def p10(graph: nx.Graph, level):

    [print(node) for node in graph.nodes.data()]
    left_graph = make_left_side_graph(unique_id, level)
    isomorphic_mapping = find_isomorphic_graph(graph, left_graph, selector)
    make_right_side_nodes_and_edges(
        graph, isomorphic_mapping, unique_id, level)
