from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import networkx as nx
import sys
YEAR = 2023
DAY = 23
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]

print(data)
data = data.splitlines()

def create_graph_from_map(_map):
    graph = nx.DiGraph()

    for i in range(len(_map)):
        for j in range(len(_map[i])):
            current_cell = _map[i][j]

            if current_cell == '#':
                continue

            graph.add_node((i, j))

            if current_cell == "^":
                graph.add_edge((i, j), (i-1, j))
                continue
            elif current_cell == "v":
                graph.add_edge((i, j), (i+1, j))
                continue
            elif current_cell == "<":
                graph.add_edge((i, j), (i, j-1))
                continue
            elif current_cell == ">":
                graph.add_edge((i, j), (i, j+1))
                continue

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
        if len(current_path) > len(longest_path):
            longest_path.clear()
            longest_path.extend(current_path[:])
    else:
        for neighbor in graph.neighbors(start):
            if not visited[neighbor]:
                dfs_longest_path_to_target(graph, neighbor, target, visited, current_path, longest_path)

    visited[start] = False
    current_path.pop()

G = create_graph_from_map(data)

start = (0,1)
end = (len(data)-1, len(data[0])-2)

visited = {node: False for node in G.nodes}
current_path = []
longest_path = []
sys.setrecursionlimit(G.number_of_nodes())
dfs_longest_path_to_target(G, start, end, visited, current_path, longest_path)
print(len(longest_path))

# update map with path
for node in longest_path:
    i, j = node
    data[i] = data[i][:j] + "O" + data[i][j+1:]

#print("\n".join(data))
answer = len(longest_path)-1
puzzle.answer_a = answer