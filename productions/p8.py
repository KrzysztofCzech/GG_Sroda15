import networkx as nx
from classes import Node
from utils import find_isomorphic_graph
from draw import draw_unmerged_graph


def make_mock_graph(uid: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()

    left_side_graph.add_nodes_from([
        Node(id=uid, label='el', x=-15, y=-15, level=level).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (uid, uid+5), (uid, uid+6)
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
        (uid+1, uid+2), (uid+1, uid+3), (uid+1, uid+4), (uid+1, uid+5),
        (uid+1, uid+6), (uid+2, uid+3), (uid+2, uid+6), (uid+3, uid+6),
        (uid+3, uid+5), (uid+3, uid+4), (uid+4, uid+5)
    ])

    level_shift = 60

    left_side_graph.add_nodes_from([
        Node(id=uid+7, label='E', x=level_shift+0, y=level_shift+0, level=level+2).graph_adapter(),
        Node(id=uid+8, label='E', x=level_shift+60, y=level_shift+0, level=level+2).graph_adapter(),
        Node(id=uid+9, label='E', x=level_shift+60, y=level_shift+30, level=level+2).graph_adapter(),
        Node(id=uid+10, label='E', x=level_shift+0, y=level_shift+30, level=level+2).graph_adapter(),

        Node(id=uid+11, label='E', x=level_shift + 30, y=level_shift + 15, level=level+2).graph_adapter(),
        Node(id=uid+12, label='E', x=level_shift + 30, y=level_shift + 15, level=level+2).graph_adapter(),

        Node(id=uid+13, label='I', x=level_shift+30, y=level_shift+5, level=level+2).graph_adapter(),
        Node(id=uid+14, label='I', x=level_shift+50, y=level_shift+15, level=level+2).graph_adapter(),
        Node(id=uid+15, label='I', x=level_shift+30, y=level_shift+25, level=level+2).graph_adapter(),
        Node(id=uid+16, label='I', x=level_shift+10, y=level_shift+15, level=level+2).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (uid+7, uid+10), (uid+7, uid+16), (uid+7, uid+11), (uid+7, uid+12), (uid+7, uid+13), (uid+7, uid+8),
        (uid+8, uid+13), (uid+8, uid+11), (uid+8, uid+14), (uid+8, uid+9),
        (uid+9, uid+14), (uid+9, uid+11), (uid+9, uid+12), (uid+9, uid+15), (uid+9, uid+10),
        (uid+10, uid+16), (uid+10, uid+15), (uid+10, uid+12),
        (uid+16, uid+12), (uid+15, uid+12), (uid+14, uid+11), (uid+13, uid+11),

        (uid+5, uid+15), (uid+5, uid+16),
        (uid+6, uid+13), (uid+6, uid+14)
    ])

    return left_side_graph


def make_left_side_graph(uid: int, level) -> nx.Graph:
    left_side_graph = nx.Graph()

    left_side_graph.add_nodes_from([
        Node(id=uid, label='el', level=level).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (uid, uid+5), (uid, uid+6)
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
        (uid+1, uid+2), (uid+1, uid+3), (uid+1, uid+4), (uid+1, uid+5),
        (uid+1, uid+6), (uid+2, uid+3), (uid+2, uid+6), (uid+3, uid+6),
        (uid+3, uid+5), (uid+3, uid+4), (uid+4, uid+5)
    ])

    left_side_graph.add_nodes_from([
        Node(id=uid+7, label='E', level=level+2).graph_adapter(),
        Node(id=uid+8, label='E', level=level+2).graph_adapter(),
        Node(id=uid+9, label='E', level=level+2).graph_adapter(),
        Node(id=uid+10, label='E', level=level+2).graph_adapter(),

        Node(id=uid+11, label='E', level=level+2).graph_adapter(),
        Node(id=uid+12, label='E', level=level+2).graph_adapter(),

        Node(id=uid+13, label='I', level=level+2).graph_adapter(),
        Node(id=uid+14, label='I', level=level+2).graph_adapter(),
        Node(id=uid+15, label='I', level=level+2).graph_adapter(),
        Node(id=uid+16, label='I', level=level+2).graph_adapter()
    ])

    left_side_graph.add_edges_from([
        (uid+7, uid+10), (uid+7, uid+16), (uid+7, uid+11), (uid+7, uid+12), (uid+7, uid+13), (uid+7, uid+8),
        (uid+8, uid+13), (uid+8, uid+11), (uid+8, uid+14), (uid+8, uid+9),
        (uid+9, uid+14), (uid+9, uid+11), (uid+9, uid+12), (uid+9, uid+15), (uid+9, uid+10),
        (uid+10, uid+16), (uid+10, uid+15), (uid+10, uid+12),
        (uid+16, uid+12), (uid+15, uid+12), (uid+14, uid+11), (uid+13, uid+11),

        (uid+5, uid+15), (uid+5, uid+16),
        (uid+6, uid+13), (uid+6, uid+14)
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


def p8(graph: nx.Graph, level: int):
    unique_id = 555
    left_graph = make_left_side_graph(unique_id, level)
    isomorphic_mapping = find_isomorphic_graph(graph, left_graph)
    isomorphic_entry_node_id = isomorphic_mapping[unique_id]

    # drawing graph before production affects final result picture
    # draw_unmerged_graph(graph, isomorphic_entry_node_id, 'p8_unmerged_graph')

    merge_nodes(isomorphic_entry_node_id, graph)
