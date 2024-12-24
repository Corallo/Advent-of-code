#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import networkx as nx
from tqdm import tqdm

DAY=20
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)


"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""

data = data.split("\n")
data = [list(d) for d in data]

print(data)

# start position has an S
for i,line in enumerate(data):
    for j,c in enumerate(line):
        if c == "S":
            start = (i,j)
        if c == "E":
            end = (i,j)

print(start, end)

def make_graph(data):
    G = nx.Graph()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "." or data[i][j] == "S" or data[i][j] == "E":
                if data[i+1][j] == "." or data[i+1][j] == "S" or data[i+1][j] == "E":
                    G.add_edge((i,j), (i+1,j))
                if data[i][j+1] == "." or data[i][j+1] == "S" or data[i][j+1] == "E":
                    G.add_edge((i,j), (i,j+1))
    return G

G=make_graph(data)
normal_shorest_path_length = nx.shortest_path_length(G, start, end)
print(normal_shorest_path_length)

count =0
for i in tqdm(range(1, len(data)-1)):
    for j in range(1, len(data[i])-1):
        if data[i][j] != "#":
            continue
        data[i][j] = "."
        G = make_graph(data)
        shorest_path_length = nx.shortest_path_length(G, start, end)
        if normal_shorest_path_length-shorest_path_length >= 100 :
            count += 1
        data[i][j] = "#"

print(count)

submit(count, part="a", day=DAY, year=2024, session=session_id)