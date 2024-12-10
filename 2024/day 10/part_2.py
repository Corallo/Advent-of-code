#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt

session_id = open("Session", "r").read()
data = get_data(day=10, year=2024,session=session_id)

"""with open('day 10/data.txt', 'r') as file:
    data = file.read()"""

data=data.strip().split("\n")
data = [list(d) for d in data]
data = np.array(data)

G = nx.DiGraph()

for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        for p in [(0,1), (1,0), (-1,0), (0,-1)]:
                if 0 <= i+p[0] < data.shape[0] and 0 <= j+p[1] < data.shape[1]:
                    if int(data[i+p[0],j+p[1]])-int(data[i,j]) == 1:
                        G.add_edge((i,j), (i+p[0], j+p[1]))


print(data)

start_points = []
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if data[i,j] == "0":
            start_points.append((i,j))

find_end_points = []
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        if data[i,j] == "9":
            find_end_points.append((i,j))

def count_all_path(G, start, end):
    return len(list(nx.all_simple_paths(G, start, end)))

answer = sum(count_all_path(G, start, end) for start in start_points for end in find_end_points)

print(answer)
submit(answer, part="b", day=10, year=2024, session=session_id)