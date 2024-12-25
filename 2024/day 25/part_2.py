#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle

import networkx as nx

DAY=23
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)


"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""

data = data.split("\n")
data = [d.split("-") for d in data]

G = nx.Graph()
for d in data:
    G.add_edge(d[0], d[1])

cliques = [list(sorted(c)) for c in nx.enumerate_all_cliques(G)]
print(cliques)

max_size = 0
max_clique = []
for clique in cliques:
    if len(clique) > max_size:
        max_size = len(clique)
        max_clique = clique

print(max_clique)
answer = ",".join(max_clique)
print(answer)

submit(answer, part ="b", day=DAY, year=2024, session=session_id)