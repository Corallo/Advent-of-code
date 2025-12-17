#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
import numpy as np
import networkx as nx

session_id = open("Session", "r").read()
data = get_data(day=8, year=2025, session=session_id)
#with open("./2025/day 8/data.txt", "r") as f:
#    data = f.read()
print(data)
data = data.splitlines()
data = [list(map(int, line.split(","))) for line in data]
data = np.array(data)
diff = data[:, None, :] - data[None, :, :] # shape (N, N, D)
distance_matrix = np.linalg.norm(diff, axis=2)   
print(distance_matrix)
np.fill_diagonal(distance_matrix, np.inf)

edges = []
G = nx.Graph()
answer = 0
N = data.shape[0]
G.add_nodes_from(range(N))
for i in range(N):
    for j in range(i+1, N):  # upper triangle
        edges.append((i, j, distance_matrix[i, j]))

edges.sort(key=lambda x: x[2])
print(edges)

for u, v, w in edges:
    G.add_edge(u, v, weight=w)
    if nx.is_connected(G):
        print(data[u], data[v])
        answer = data[u][0] * data[v][0]
        break

print(answer)   
submit(answer, part="b", day=8, year=2025, session=session_id)