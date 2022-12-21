import networkx as nx
from classes import Node
from utils import find_isomorphic_graph


def make_mock_graph(uid: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()

    left_side_graph.add_nodes_from([
        Node(id=uid, label='el', x=-15, y=-15, level=level).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (uid, uid + 5), (uid, uid + 6)
    ])

    left_side_graph.add_nodes_from([
        Node(id=uid + 1, label='E', x=0, y=0, level=level + 1).graph_adapter(),
        Node(id=uid + 2, label='E', x=60, y=0, level=level + 1).graph_adapter(),
        Node(id=uid + 3, label='E', x=60, y=30, level=level + 1).graph_adapter(),
        Node(id=uid + 4, label='E', x=0, y=30, level=level + 1).graph_adapter(),
        Node(id=uid + 5, label='i', x=20, y=20, level=level + 1).graph_adapter(),
        Node(id=uid + 6, label='i', x=40, y=10, level=level + 1).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (uid + 1, uid + 2), (uid + 1, uid + 3), (uid + 1, uid + 4), (uid + 1, uid + 5),
        (uid + 1, uid + 6), (uid + 2, uid + 3), (uid + 2, uid + 6), (uid + 3, uid + 6),
        (uid + 3, uid + 5), (uid + 3, uid + 4), (uid + 4, uid + 5)
    ])

    level_shift = 60

    left_side_graph.add_nodes_from([
        Node(id=uid + 7, label='E', x=level_shift + 0, y=level_shift + 0, level=level + 2).graph_adapter(),
        Node(id=uid + 8, label='E', x=level_shift + 60, y=level_shift + 0, level=level + 2).graph_adapter(),
        Node(id=uid + 9, label='E', x=level_shift + 60, y=level_shift + 30, level=level + 2).graph_adapter(),
        Node(id=uid + 10, label='E', x=level_shift + 0, y=level_shift + 30, level=level + 2).graph_adapter(),

        Node(id=uid + 11, label='E', x=level_shift + 30, y=level_shift + 15, level=level + 2).graph_adapter(),
        Node(id=uid + 12, label='E', x=level_shift + 30, y=level_shift + 15, level=level + 2).graph_adapter(),

        Node(id=uid + 13, label='I', x=level_shift + 30, y=level_shift + 5, level=level + 2).graph_adapter(),
        Node(id=uid + 14, label='I', x=level_shift + 50, y=level_shift + 15, level=level + 2).graph_adapter(),
        Node(id=uid + 15, label='I', x=level_shift + 30, y=level_shift + 25, level=level + 2).graph_adapter(),
        Node(id=uid + 16, label='I', x=level_shift + 10, y=level_shift + 15, level=level + 2).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (uid + 7, uid + 10), (uid + 7, uid + 16), (uid + 7, uid + 11), (uid + 7, uid + 12), (uid + 7, uid + 13),
        (uid + 7, uid + 8),
        (uid + 8, uid + 13), (uid + 8, uid + 11), (uid + 8, uid + 14), (uid + 8, uid + 9),
        (uid + 9, uid + 14), (uid + 9, uid + 11), (uid + 9, uid + 12), (uid + 9, uid + 15), (uid + 9, uid + 10),
        (uid + 10, uid + 16), (uid + 10, uid + 15), (uid + 10, uid + 12),
        (uid + 16, uid + 12), (uid + 15, uid + 12), (uid + 14, uid + 11), (uid + 13, uid + 11),

        (uid + 5, uid + 15), (uid + 5, uid + 16),
        (uid + 6, uid + 13), (uid + 6, uid + 14)
    ])

    return left_side_graph


def make_left_side_graph(uid: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()

    left_side_graph.add_nodes_from([
        Node(id=uid + 1, label='E', level=level + 1).graph_adapter(),
        Node(id=uid + 3, label='E', level=level + 1).graph_adapter(),
        Node(id=uid + 5, label='i', level=level + 1).graph_adapter(),
        Node(id=uid + 6, label='i', level=level + 1).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (uid + 1, uid + 3), (uid + 1, uid + 5),
        (uid + 1, uid + 6), (uid + 3, uid + 6),
        (uid + 3, uid + 5),
    ])

    left_side_graph.add_nodes_from([
        Node(id=uid + 7, label='E', level=level + 2).graph_adapter(),
        Node(id=uid + 9, label='E', level=level + 2).graph_adapter(),

        Node(id=uid + 11, label='E', level=level + 2).graph_adapter(),
        Node(id=uid + 12, label='E', level=level + 2).graph_adapter(),

        Node(id=uid + 13, label='I', level=level + 2).graph_adapter(),
        Node(id=uid + 14, label='I', level=level + 2).graph_adapter(),
        Node(id=uid + 15, label='I', level=level + 2).graph_adapter(),
        Node(id=uid + 16, label='I', level=level + 2).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (uid + 7, uid + 16), (uid + 7, uid + 11), (uid + 7, uid + 12), (uid + 7, uid + 13),
        (uid + 9, uid + 14), (uid + 9, uid + 11), (uid + 9, uid + 12), (uid + 9, uid + 15),
        (uid + 16, uid + 12), (uid + 15, uid + 12), (uid + 14, uid + 11), (uid + 13, uid + 11),

        (uid + 5, uid + 15), (uid + 5, uid + 16),
        (uid + 6, uid + 13), (uid + 6, uid + 14)
    ])

    return left_side_graph


def check_if_subgraph_matches_p8(subgraph: dict, graph: nx.Graph):
    nodes_view = list(subgraph.values())
    print(nodes_view)

    adj = graph._adj
    graph_nodes = graph._node

    el_node = adj.get(nodes_view[0])  # lvl 0 (start)

    i_nodes = []
    for n in nodes_view:
        if graph_nodes.get(n)['label'] == 'i':
            i_nodes.append(n)

    i_node_1, i_node_2 = adj.get(i_nodes[0]), adj.get(i_nodes[1])  # lvl 1
    I_node_1_id, I_node_2_id = None, None

    for n in i_node_1:
        if n in nodes_view and graph_nodes.get(n)['label'] == 'I':
            I_node_1_id = n
            break

    for n in i_node_2:
        if n in nodes_view and graph_nodes.get(n)['label'] == 'I':
            I_node_2_id = n
            break

    I_node_1, I_node_2 = adj.get(I_node_1_id), adj.get(I_node_2_id)  # lvl 2

    node_to_remove = None
    node_to_remove_id = None
    node_to_stay = None
    node_to_stay_id = None
    for node_1_id in I_node_1.keys():
        if node_1_id not in nodes_view:
            continue
        node_1 = graph_nodes.get(node_1_id)
        for node_2_id in I_node_2.keys():
            if node_1_id == node_2_id or node_2_id not in nodes_view:
                continue
            node_2 = graph_nodes.get(node_2_id)
            if node_1['label'] == 'E' and node_1 == node_2:
                common_nodes = list(set(adj.get(node_1_id)).intersection(adj.get(node_2_id)).intersection(nodes_view))
                print(f"{common_nodes=}")
                if len(common_nodes) != 2:
                    continue

                e_node_1 = graph_nodes.get(common_nodes[0])
                e_node_2 = graph_nodes.get(common_nodes[1])

                if node_1['x'] != (e_node_1['x'] + e_node_2['x']) / 2 or \
                        node_1['y'] != (e_node_1['y'] + e_node_2['y']) / 2:
                    continue

                node_to_remove = node_2
                node_to_remove_id = node_2_id
                node_to_stay = node_1
                node_to_stay_id = node_1_id

    if node_to_remove_id is not None and node_to_stay_id is not None:
        print(f"Node to remove {node_to_remove_id}: {node_to_remove}")
        print(f"Node to stay {node_to_stay_id}: {node_to_stay}")
        removed_node_neighbours = adj.get(node_to_remove_id)
        print(f"Neighbours of the node to remove: {list(removed_node_neighbours)}")
        for lonely_neighbour_id in list(removed_node_neighbours):
            graph.add_edge(node_to_stay_id, lonely_neighbour_id)

        graph.remove_node(node_to_remove_id)

        return True
    else:
        return False


def find_and_merge_nodes(subgraphs, graph: nx.Graph):
    if not subgraphs:
        return False
    for subgraph in subgraphs:
        if check_if_subgraph_matches_p8(subgraph, graph):
            return True
    return False


def p8(graph: nx.Graph, level: int):
    unique_id = 555
    left_graph = make_left_side_graph(unique_id, level)
    isomorphic_mappings = find_isomorphic_graph(graph, left_graph)
    is_production_completed = find_and_merge_nodes(isomorphic_mappings, graph)
    print("Merged nodes successfully" if is_production_completed else "No compatible graph found")

    return is_production_completed
