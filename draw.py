import copy
from collections.abc import Iterable
from pprint import pprint

from matplotlib import pyplot as plt
import networkx as nx
from classes import Attr_MAP
label_color_map = {
    "El": 'green',
    "I": 'red',
    "el": "blue",
    "E": "orange",
    "i": "yellow",
    "L": "pink",
}


def draw_graph(graph: nx.Graph, name: str, level_offset=40, font_size=12, with_coords=False, level=None):

    graph = copy.deepcopy(graph)

    to_remove = []
    if level is not None:
        level_to_graph = []
        if isinstance(level, Iterable):
            level_to_graph = level
        else:
            level_to_graph.append(level)

        for node in graph.nodes():
            if graph.nodes[node][Attr_MAP.level] not in level_to_graph:
                to_remove.append(node)
    graph.remove_nodes_from(to_remove)
    data = graph._node

    pos = {k: (v[Attr_MAP.x]+level_offset*v[Attr_MAP.level], v[Attr_MAP.y] +
               level_offset*v[Attr_MAP.level])for k, v in data.items()}

    labels = {
        k: f"\n{k}\n{v[Attr_MAP.x]}, {v[Attr_MAP.y]}" for k, v in data.items()}
    color_list = [label_color_map[v[Attr_MAP.label]] for k, v in data.items()]

    if with_coords:
        nx.draw_networkx(graph, pos, labels=labels,
                         node_color=color_list, font_size=font_size)
    else:
        nx.draw_networkx(graph, pos, node_color=color_list,
                         font_size=font_size)
    ax = plt.gca()
    plt.axis("off")
    plt.savefig(f'./graphs/{name}.png')
    plt.clf()


def draw_unmerged_graph(graph: nx.Graph, starting_node: int, name: str):
    graph_copy = copy.deepcopy(graph)
    adj = graph_copy._adj
    nodes = graph_copy._node

    el_node = adj.get(starting_node)  # lvl 0 (start)
    i_node_1 = adj.get(list(el_node)[0])  # lvl 1
    i_node_2 = adj.get(list(el_node)[1])  # lvl 1
    I_node_1_id = list(i_node_1)[-1]
    I_node_2_id = list(i_node_2)[-2]
    I_node_1 = adj.get(I_node_1_id)  # lvl 2
    I_node_2 = adj.get(I_node_2_id)  # lvl 2

    node_to_remove = None
    node_to_stay = None
    for node_1_id in I_node_1.keys():
        node_1 = nodes.get(node_1_id)
        for node_2_id in I_node_2.keys():
            if node_1_id == node_2_id:
                continue
            node_2 = nodes.get(node_2_id)
            if node_1 == node_2:
                node_to_remove = node_2
                node_to_stay = node_1

    node_to_remove[Attr_MAP.x] = node_to_remove[Attr_MAP.x] + 5
    node_to_stay[Attr_MAP.x] = node_to_stay[Attr_MAP.x] - 5

    draw_graph(graph_copy, name=name)
