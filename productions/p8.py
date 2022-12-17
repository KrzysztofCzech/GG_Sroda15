import networkx as nx
from classes import Node, Attr_MAP
from utils import find_isomorphic_graph, update_graph


def make_mock_graph(uid: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()

    left_side_graph.add_nodes_from([
        Node(id=uid, label='el', x=-15, y=-15, level=level).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (0, 5), (0, 6)
    ])

    left_side_graph.add_nodes_from([
        Node(id=uid+1, label='E', x=0, y=0, level=level+1).graph_adapter(),
        Node(id=uid+2, label='E', x=60, y=0, level=level+1).graph_adapter(),
        Node(id=uid+3, label='E', x=60, y=30, level=level+1).graph_adapter(),
        Node(id=uid+4, label='E', x=0, y=30, level=level+1).graph_adapter(),
        Node(id=uid+5, label='i', x=20, y=20, level=level+1).graph_adapter(),
        Node(id=uid+6, label='i', x=40, y=10, level=level+1).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (1, 2), (1, 3), (1, 4), (1, 5),
        (1, 6), (2, 3), (2, 6), (3, 6),
        (3, 5), (3, 4), (4, 5)
    ])

    level_shift = 60

    left_side_graph.add_nodes_from([
        Node(id=uid+7, label='E', x=level_shift+0, y=level_shift+0, level=level+2).graph_adapter(),
        Node(id=uid+8, label='E', x=level_shift+60, y=level_shift+0, level=level+2).graph_adapter(),
        Node(id=uid+9, label='E', x=level_shift+60, y=level_shift+30, level=level+2).graph_adapter(),
        Node(id=uid+10, label='E', x=level_shift+0, y=level_shift+30, level=level+2).graph_adapter(),

        # Node(id=uid+11, label='E', x=level_shift+35, y=level_shift+15, level=level+2).graph_adapter(),
        # Node(id=uid+12, label='E', x=level_shift+25, y=level_shift+15, level=level+2).graph_adapter(),

        Node(id=uid+11, label='E', x=level_shift + 30, y=level_shift + 15, level=level+2).graph_adapter(),
        Node(id=uid+12, label='E', x=level_shift + 30, y=level_shift + 15, level=level+2).graph_adapter(),

        Node(id=uid+13, label='I', x=level_shift+30, y=level_shift+5, level=level+2).graph_adapter(),
        Node(id=uid+14, label='I', x=level_shift+50, y=level_shift+15, level=level+2).graph_adapter(),
        Node(id=uid+15, label='I', x=level_shift+30, y=level_shift+25, level=level+2).graph_adapter(),
        Node(id=uid+16, label='I', x=level_shift+10, y=level_shift+15, level=level+2).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (7, 10), (7, 16), (7, 11), (7, 12), (7, 13), (7, 8),
        (8, 13), (8, 11), (8, 14), (8, 9),
        (9, 14), (9, 11), (9, 12), (9, 15), (9, 10),
        (10, 16), (10, 15), (10, 12),
        (16, 12), (15, 12), (14, 11), (13, 11),

        (5, 15), (5, 16),
        (6, 13), (6, 14)
    ])

    return left_side_graph


def make_left_side_graph(uid: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()

    left_side_graph.add_nodes_from([
        Node(id=uid, label='el', x=-15, y=-15, level=level).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (0, 5), (0, 6)
    ])

    left_side_graph.add_nodes_from([
        Node(id=uid+1, label='E', level=level+1).graph_adapter(),
        Node(id=uid+2, label='E', level=level+1).graph_adapter(),
        Node(id=uid+3, label='E', level=level+1).graph_adapter(),
        Node(id=uid+4, label='E', level=level+1).graph_adapter(),
        Node(id=uid+5, label='i', level=level+1).graph_adapter(),
        Node(id=uid+6, label='i', level=level+1).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (1, 2), (1, 3), (1, 4), (1, 5),
        (1, 6), (2, 3), (2, 6), (3, 6),
        (3, 5), (3, 4), (4, 5)
    ])

    level_shift = 60

    left_side_graph.add_nodes_from([
        Node(id=uid+7, label='E', level=level+2).graph_adapter(),
        Node(id=uid+8, label='E', level=level+2).graph_adapter(),
        Node(id=uid+9, label='E', level=level+2).graph_adapter(),
        Node(id=uid+10, label='E', level=level+2).graph_adapter(),

        # Node(id=uid+11, label='E', level=level+2).graph_adapter(),
        # Node(id=uid+12, label='E', level=level+2).graph_adapter(),

        Node(id=uid+11, label='E', level=level+2).graph_adapter(),
        Node(id=uid+12, label='E', level=level+2).graph_adapter(),

        Node(id=uid+13, label='I', level=level+2).graph_adapter(),
        Node(id=uid+14, label='I', level=level+2).graph_adapter(),
        Node(id=uid+15, label='I', level=level+2).graph_adapter(),
        Node(id=uid+16, label='I', level=level+2).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (7, 10), (7, 16), (7, 11), (7, 12), (7, 13), (7, 8),
        (8, 13), (8, 11), (8, 14), (8, 9),
        (9, 14), (9, 11), (9, 12), (9, 15), (9, 10),
        (10, 16), (10, 15), (10, 12),
        (16, 12), (15, 12), (14, 11), (13, 11),

        (5, 15), (5, 16),
        (6, 13), (6, 14)
    ])

    return left_side_graph


def merge_nodes(unique_id: int, graph: nx.Graph):
    adj = graph._adj
    nodes = graph._node

    el_node = adj.get(unique_id)  # lvl 0 (start)
    i_node_1 = adj.get(list(el_node)[0])  # lvl 1
    i_node_2 = adj.get(list(el_node)[1])  # lvl 1
    I_node_1_id = list(i_node_1)[-1]
    I_node_2_id = list(i_node_2)[-2]
    I_node_1 = adj.get(I_node_1_id)  # lvl 2
    I_node_2 = adj.get(I_node_2_id)  # lvl 2

    node_to_remove = None
    node_to_remove_key = None
    node_to_stay = None
    node_to_stay_key = None
    for node_1_id in I_node_1.keys():
        node_1 = nodes.get(node_1_id)
        for node_2_id in I_node_2.keys():
            if node_1_id == node_2_id:
                continue
            node_2 = nodes.get(node_2_id)
            if node_1 == node_2:
                node_to_remove = node_2
                node_to_remove_key = node_2_id
                node_to_stay = node_1
                node_to_stay_key = node_1_id

    print(f"Node to remove {node_to_remove_key}: {node_to_remove}")
    print(f"Node to stay {node_to_stay_key}: {node_to_stay}")

    removed_node_neighbours = adj.get(node_to_remove_key)
    print(f"Neighbours of the node to remove: {list(removed_node_neighbours)}")

    for lonely_neighbour in list(removed_node_neighbours):
        graph.add_edge(node_to_stay_key, lonely_neighbour)

    graph.remove_node(node_to_remove_key)


def make_right_side_nodes_and_edges(unique_id: int, coords: tuple[list, list], level) -> tuple[list[Node], list, Node]:
    x, y = coords


def update_x_y_coords(graph: nx.Graph, mapping: dict) -> tuple[list, list]:
    x_coords = []
    y_coords = []
    for _, node in mapping.items():
        if graph.nodes[node][Attr_MAP.label] == 'E':
            x_coords.append(graph.nodes[node][Attr_MAP.x])
            y_coords.append(graph.nodes[node][Attr_MAP.y])

    return x_coords, y_coords


def p8(graph: nx.Graph, level: int):
    unique_id = 555
    left_graph = make_left_side_graph(unique_id, level)
    isomorphic_mapping = find_isomorphic_graph(graph, left_graph)
    merge_nodes(unique_id, graph)
    # right_side_nodes, right_side_edges, right_unique_node = make_right_side_nodes_and_edges(
    #     unique_id, update_x_y_coords(graph, isomorphic_mapping), level)
    # update_graph(graph, isomorphic_mapping, right_unique_node,
    #              right_side_nodes, right_side_edges)
