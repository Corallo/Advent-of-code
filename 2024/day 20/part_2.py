#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import networkx as nx

DAY=20
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)


"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""

data = data.split("\n")
data = [list(d) for d in data]

print(data)

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

def make_cheat_graph(data):
    G = nx.Graph()
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "." or data[i][j] == "S" or data[i][j] == "E" or data[i][j] == "#":
                if data[i+1][j] == "." or data[i+1][j] == "S" or data[i+1][j] == "E" or data[i+1][j] == "#":
                    G.add_edge((i,j), (i+1,j))
                if data[i][j+1] == "." or data[i][j+1] == "S" or data[i][j+1] == "E" or data[i][j+1] == "#":
                    G.add_edge((i,j), (i,j+1))
    return G

G=make_graph(data)
normal_shorest_path = nx.shortest_path(G, start, end)
print(normal_shorest_path)
print(len(normal_shorest_path))

count = 0
for x in range(len(normal_shorest_path)):
    for y in range(x+101, len(normal_shorest_path)):
        i,j = normal_shorest_path[x]
        a,b = normal_shorest_path[y]
        d = abs(i-a) + abs(j-b)
        if  d <= 20 and y-x-d >= 100:
            count += 1
print(count)

submit(count, part="b", day=DAY, year=2024, session=session_id)