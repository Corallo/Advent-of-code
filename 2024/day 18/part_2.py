#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import networkx as nx
from tqdm import tqdm

DAY=18
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""

data = data.split("\n")
data = [d.split(",") for d in data]

print(data)

matrix = np.zeros((71,71))
#matrix = np.zeros((7,7))

def check_exit(matrix):
    G = nx.Graph()

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i,j] == 0:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < matrix.shape[0] and 0 <= nj < matrix.shape[1] and matrix[ni, nj] == 0:
                        neighbor = (ni, nj)
                        G.add_edge((i,j), neighbor)

    path_exist = nx.has_path(G, (70,70), (0,0))
    #path_exist = nx.has_path(G, (6,6), (0,0))
    return path_exist


for i,d in tqdm(enumerate(data)):
    matrix[int(d[1]),int(d[0])]=1

    if not check_exit(matrix):
        print("The byte that block the way is", data[i])
        break
#submit(cost, part="a", day=DAY, year=2024, session=session_id)