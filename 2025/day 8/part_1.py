#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
import numpy as np
import networkx as nx

session_id = open("Session", "r").read()
data = get_data(day=8, year=2025, session=session_id)
#with open("./2025/day 7/data.txt", "r") as f:
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
for t in range(1000):
    best_edge = distance_matrix.argmin()
    i,j = best_edge // distance_matrix.shape[1], best_edge % distance_matrix.shape[1]
    edges.append((i,j))
    edges.append((j,i))
    distance_matrix[i,j] = np.inf
    distance_matrix[j,i] = np.inf

G = nx.Graph()
G.add_edges_from(edges)

sizes = sorted((len(c) for c in nx.connected_components(G)), reverse=True)
answer= np.prod(sizes[:3])
print(answer)
submit(answer, part="a", day=8, year=2025, session=session_id)