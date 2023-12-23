from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import networkx as nx
import sys
import matplotlib.pyplot as plt
YEAR = 2023
DAY = 23
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
data=data.replace("^", ".")
data=data.replace("v", ".")
data=data.replace("<", ".")
data=data.replace(">", ".")
#print(data)
data = data.splitlines()

def create_graph_from_map(_map):
    graph = nx.Graph()

    for i in range(len(_map)):
        for j in range(len(_map[i])):
            current_cell = _map[i][j]

            if current_cell == '#':
                continue

            graph.add_node((i, j))
            neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for neighbor in neighbors:
                ni, nj = neighbor
                if 0 <= ni < len(_map) and 0 <= nj < len(_map[i]) and _map[ni][nj] != '#':
                    graph.add_edge((i, j), (ni, nj))

    return graph

def dfs_longest_path_to_target(graph, start, target, visited, current_path, longest_path):
    visited[start] = True
    current_path.append(start)

    if start == target:
        # use weight to calculate distance one line
        distance_to_target = sum(G[current_path[i]][current_path[i+1]]['weight'] for i in range(len(current_path)-1))
        longest_distance_to_target = sum(G[longest_path[i]][longest_path[i+1]]['weight'] for i in range(len(longest_path)-1))
        if distance_to_target > longest_distance_to_target:
            longest_path.clear()
            longest_path.extend(current_path[:])
            print("Found new longest path with length", distance_to_target)
    else:
        for neighbor in graph.neighbors(start):
            if not visited[neighbor]:
                dfs_longest_path_to_target(graph, neighbor, target, visited, current_path, longest_path)

    visited[start] = False
    current_path.pop()


def find_path_to_targets(G, start_node, targets):
    paths = []

    def dfs(current_path):
        current_node = current_path[-1]

        if current_node in targets:
            paths.append(list(current_path))
            return

        neighbors = G.neighbors(current_node)
        for neighbor in neighbors:
            if neighbor not in current_path:
                current_path.append(neighbor)
                dfs(current_path)
                current_path.pop()

    dfs([start_node])
    return paths

def simplify_graph(G,start, end):
    # Create a simpler graph, having only nodes with degree greater than 2, and start and end nodes
    # basically we delete all the "corridors" and replace that with a single weighted edge
    simplified_graph = nx.Graph()
    simplified_graph.add_node(start)
    simplified_graph.add_node(end)

    # Take all nodes with degree >2
    high_nodes = [node for node in G.nodes if G.degree(node) > 2]
    high_nodes.append(start)
    high_nodes.append(end)
    print("High degree nodes:", len(high_nodes))
    checked_nodes = set()
    for ni in tqdm(high_nodes):
        tmp_high_nodes = high_nodes.copy()
        tmp_high_nodes.remove(ni)
        paths=find_path_to_targets(G, ni, tmp_high_nodes)
        for path in paths:
            nj = path[-1]
            if ni == nj or (ni, nj) in checked_nodes or (nj, ni) in checked_nodes:
                continue
            simplified_graph.add_edge(ni, nj, weight=len(path)-1)

    return simplified_graph


G = create_graph_from_map(data)
print("Create Graph with %d nodes" % G.number_of_nodes())
start = (0,1)
end = (len(data)-1, len(data[0])-2)
G = simplify_graph(G,start,end)

# visualize graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()


print("Simplified Graph with %d nodes" % G.number_of_nodes())
visited = {node: False for node in G.nodes}
current_path = []
longest_path = []
dfs_longest_path_to_target(G, start, end, visited, current_path, longest_path)

# Calculate length of longest path
length=sum(G[longest_path[i]][longest_path[i+1]]['weight'] for i in range(len(longest_path)-1))
puzzle.answer_b = length