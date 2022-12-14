import networkx as nx
from classes import Node, Attr_MAP
from utils import find_isomorphic_graph, update_graph

WIP=123

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
            x_coords.append(graph.nodes[node][Attr_MAP.x] + 50)
            y_coords.append(graph.nodes[node][Attr_MAP.y] + 50)

    return x_coords, y_coords


def make_right_side_nodes_and_edges(unique_id: int, coords: tuple[list, list], level) -> tuple[list[Node], list, Node]:
    x, y = coords

    print("COORDS")
    print(x, y)

    parent_node = Node(id=unique_id, label='i', x=(x[0] + x[1] + x[2]) / 3, y=(y[0] + y[1] + y[2])/3, level=level+1)
    right_nodes = [
        Node(id=1, label='I', x=(x[0] + x[1] + x[2]) / 3, y=(y[0] + y[1] + y[2]) / 3, level=level+1),
        Node(id=2, label='E', x=x[0], y=y[0], level=level+1),
        Node(id=3, label='E', x=x[1], y=y[1], level=level+1),
        Node(id=4, label='E', x=x[2], y=y[2], level=level+1),
    ]

    edges = [
        (unique_id, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (2, 3),
        (2, 4),
        (3, 4),
    ]

    return right_nodes, edges, parent_node


def selector(graphs):
    print(graphs)
    return graphs[0]


def p10(graph: nx.Graph, level):
    unique_id = 555  # id that will be match egde from left side to right side production graph be used must be higher than max number of id used
    left_graph = make_left_side_graph(unique_id, level)
    isomorphic_mapping = find_isomorphic_graph(graph, left_graph, selector)
    right_side_nodes, right_side_edges, right_unique_node = make_right_side_nodes_and_edges(
        unique_id, update_x_y_coords(graph, isomorphic_mapping), level)
    update_graph(graph, isomorphic_mapping, right_unique_node,
                 right_side_nodes, right_side_edges)
