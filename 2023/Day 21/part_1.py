from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import networkx as nx
YEAR = 2023
DAY = 21
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data

#data = puzzle.examples[0][0]

print(data)

G = nx.DiGraph()

for y, line in enumerate(data.splitlines()):
    for x, char in enumerate(line):
        if char == "#":
            continue
        if char == ".":
            G.add_node((x,y))
        if char == "S":
            start = (x,y)
            G.add_node(start)

#add edges
for y in range(len(data.splitlines())):
    for x in range(len(data.splitlines()[y])):
        if (x,y) in G:
            if (x+1,y) in G:
                G.add_edge((x,y),(x+1,y))
            if (x-1,y) in G:
                G.add_edge((x,y),(x-1,y))
            if (x,y+1) in G:
                G.add_edge((x,y),(x,y+1))
            if (x,y-1) in G:
                G.add_edge((x,y),(x,y-1))


shortest_paths = nx.single_source_shortest_path_length(G, start)

#filter only path with length multiple of 2 and lower or equal than 64
shortest_paths = {k:v for k,v in shortest_paths.items() if v%2 == 0 and v <= 64}

print(shortest_paths)
print(len(shortest_paths))
answer = len(shortest_paths)
#Edit map to show nodes in shortest_path
"""
map = data.splitlines()
for node in shortest_paths.keys():
    x,y = node
    map[y] = map[y][:x] + "O" + map[y][x+1:]

print("\n".join(map))
"""


puzzle.answer_a = answer