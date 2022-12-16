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


def draw_graph(graph : nx.Graph, name: str):
    data =  graph._node

    pos = {k:(v[Attr_MAP.x]+40*v[Attr_MAP.level], v[Attr_MAP.y]+35*v[Attr_MAP.level])for k,v in data.items()}
    color_list = [label_color_map[v[Attr_MAP.label]] for k,v in data.items()]

    nx.draw_networkx(graph, pos, node_color=color_list)
    ax = plt.gca()
    plt.axis("off")
    plt.savefig(f'./graphs/{name}.png')
