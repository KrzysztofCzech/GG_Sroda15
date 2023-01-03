from matplotlib import pyplot as plt
import networkx as nx
from classes import Attr_MAP
label_color_map = {
    "El": 'green',
    "I": 'red',
    "el": "blue",
    "E": "orange",
    "i": "yellow",
}


def draw_graph(graph: nx.Graph, name: str, level_offset=40, font_size=12, with_coords=False):
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
