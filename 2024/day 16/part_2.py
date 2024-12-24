#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import networkx as nx
from tqdm import tqdm

DAY=16
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""

data = data.split("\n")
data = [list(d) for d in data]

print(data)
start_point = len(data)-2, 1
end_point = 1, len(data[0])-2

print(data[start_point[0]][start_point[1]])
print(data[end_point[0]][end_point[1]])
data[start_point[0]][start_point[1]] = "."
data[end_point[0]][end_point[1]] = "."
G = nx.Graph()

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == ".":
            G.add_edge(f"{i}_{j}_s", f"{i}_{j}_n", weight=0)
            G.add_edge(f"{i}_{j}_w", f"{i}_{j}_s", weight=1000)
            G.add_edge(f"{i}_{j}_w", f"{i}_{j}_e", weight=0)
            G.add_edge(f"{i}_{j}_w", f"{i}_{j}_n", weight=1000)
            if i > 0 and data[i-1][j] == ".":
                G.add_edge(f"{i}_{j}_n", f"{i-1}_{j}_s", weight=1)
            if i < len(data)-1 and data[i+1][j] == ".":
                G.add_edge(f"{i}_{j}_s", f"{i+1}_{j}_n", weight=1)
            if j > 0 and data[i][j-1] == ".":
                G.add_edge(f"{i}_{j}_w", f"{i}_{j-1}_e", weight=1)
            if j < len(data[i])-1 and data[i][j+1] == ".":
                G.add_edge(f"{i}_{j}_e", f"{i}_{j+1}_w", weight=1)

G.add_edge(f"{end_point[0]}_{end_point[1]}_n", f"{end_point[0]}_{end_point[1]}", weight=0)
G.add_edge(f"{end_point[0]}_{end_point[1]}_s", f"{end_point[0]}_{end_point[1]}", weight=0)
G.add_edge(f"{end_point[0]}_{end_point[1]}_e", f"{end_point[0]}_{end_point[1]}", weight=0)
G.add_edge(f"{end_point[0]}_{end_point[1]}_w", f"{end_point[0]}_{end_point[1]}", weight=0)

dist_from_start = nx.single_source_dijkstra_path_length(G, source=f"{start_point[0]}_{start_point[1]}_e", weight="weight")
dist_to_end = nx.single_source_dijkstra_path_length(G, source=f"{end_point[0]}_{end_point[1]}", weight="weight")
shortest_path_length = dist_from_start.get(f"{end_point[0]}_{end_point[1]}", float('inf'))

shortest_path_nodes = {
    node for node in G.nodes
    if dist_from_start.get(node, float('inf')) +
       dist_to_end.get(node, float('inf')) == shortest_path_length
}


good_tiles = set()

for n in tqdm(shortest_path_nodes):
    p = n.split("_")
    good_tiles.add((p[0], p[1]))
    data[int(p[0])][int(p[1])] = "*"

for d in data:
    print(''.join(d))

print(good_tiles)
print(len(good_tiles))
score= len(good_tiles)
submit(score, part="b", day=DAY, year=2024, session=session_id)