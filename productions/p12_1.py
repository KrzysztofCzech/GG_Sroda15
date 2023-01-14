import networkx as nx
from classes import Node

from utils import find_isomorphic_graph, find_all_isomorphic_graphs


def make_left_side_graph(unique_id: int, level) -> nx.Graph:
	left_side_graph = nx.Graph()

	left_side_graph.add_nodes_from([
		Node(id=unique_id, label="i", level=level).graph_adapter(),
		Node(id=unique_id + 1, label="i", level=level).graph_adapter(),
		Node(id=unique_id + 2, label="E", level=level).graph_adapter(),
		Node(id=unique_id + 3, label="E", level=level).graph_adapter(),

		Node(id=unique_id + 4, label="I", level=level + 1).graph_adapter(),
		Node(id=unique_id + 5, label="E", level=level + 1).graph_adapter(),
		Node(id=unique_id + 6, label="E", level=level + 1).graph_adapter(),

		Node(id=unique_id + 7, label="I", level=level + 1).graph_adapter(),
		Node(id=unique_id + 8, label="E", level=level + 1).graph_adapter(),
		Node(id=unique_id + 9, label="E", level=level + 1).graph_adapter(),
	])

	left_side_graph.add_edges_from([
		(unique_id, unique_id + 2),
		(unique_id, unique_id + 3),
		(unique_id + 1, unique_id + 2),
		(unique_id + 1, unique_id + 3),
		(unique_id + 2, unique_id + 3),

		(unique_id, unique_id + 4),
		(unique_id + 1, unique_id + 7),

		(unique_id + 4, unique_id + 5),
		(unique_id + 4, unique_id + 6),
		(unique_id + 5, unique_id + 6),

		(unique_id + 7, unique_id + 8),
		(unique_id + 7, unique_id + 9),
		(unique_id + 9, unique_id + 8),

	])

	return left_side_graph


def cmp_pos_and_label(node_1, node_2):
	return node_1["x"] == node_2["x"] \
		and node_1["y"] == node_2["y"] \
		and node_1["level"] == node_2["level"] \
		and node_1["label"] == node_2["label"]


def find_mergable(unique_id: int, mapping: dict, graph: nx.Graph):
	nodes = graph.nodes

	nodes_to_join_list = [
	]

	candidate_left_1 = nodes[mapping[unique_id + 5]]
	candidate_left_2 = nodes[mapping[unique_id + 6]]

	candidate_right_1 = nodes[mapping[unique_id + 8]]
	candidate_right_2 = nodes[mapping[unique_id + 9]]

	if cmp_pos_and_label(candidate_left_1, candidate_right_1) and cmp_pos_and_label(candidate_left_2, candidate_right_2):
		nodes_to_join_list.append((unique_id + 5, unique_id + 8))
		nodes_to_join_list.append((unique_id + 6, unique_id + 9))
	elif cmp_pos_and_label(candidate_left_1, candidate_right_2) and cmp_pos_and_label(candidate_left_2, candidate_right_1):
		nodes_to_join_list.append((unique_id + 5, unique_id + 9))
		nodes_to_join_list.append((unique_id + 6, unique_id + 8))

	return nodes_to_join_list


def merge_nodes(unique_id: int, mapping: dict, graph: nx.Graph):
	adj = graph.adj
	nodes = graph.nodes

	nodes_to_join_list = find_mergable(unique_id, mapping, graph)

	if len(nodes_to_join_list) == 0:
		return

	for nodes_to_join in nodes_to_join_list:
		left_real_id = mapping[nodes_to_join[0]]
		right_real_id = mapping[nodes_to_join[1]]

		lonely_nodes = adj[left_real_id]

		for lonely_node_id in lonely_nodes:
			graph.add_edge(right_real_id, lonely_node_id)

		graph.remove_node(left_real_id)

	return True


def p12(graph: nx.Graph, level, skip=0):
	unique_id = 555
	left_graph = make_left_side_graph(unique_id, level)
	isomorphic_mappings = find_all_isomorphic_graphs(graph, left_graph)

	skipped = 0
	for mapping in isomorphic_mappings:
		if find_mergable(unique_id, mapping, graph):
			if skipped >= skip:
				merge_nodes(unique_id, mapping, graph)
				return
			skipped += 1