from math import prod
import networkx as nx


with open('Day25/input.in', 'r') as file:
    lines = file.read().splitlines()
    
graph = nx.Graph()

for line in lines:
    v, others = line.split(': ')
    for o in others.split():
        graph.add_edge(v, o)
        
min_edge_cut = nx.minimum_edge_cut(graph)
print(min_edge_cut)
graph.remove_edges_from(min_edge_cut)
print(prod([len(c) for c in nx.connected_components(graph)]))