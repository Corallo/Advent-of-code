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

suspicious_nodes = set()
for d in data:
    if d[0].startswith("t"):
        suspicious_nodes.add(d[0])
    if d[1].startswith("t"):
        suspicious_nodes.add(d[1])

G = nx.Graph()
for d in data:
    G.add_edge(d[0], d[1])

cliques = [tuple(sorted(c)) for c in nx.enumerate_all_cliques(G) if len(c) == 3]
print(cliques)

answer = 0
for clique in cliques:
    if any([node in suspicious_nodes for node in clique]):
        print(clique)
        answer += 1
print(answer)


submit(answer, part="a", day=DAY, year=2024, session=session_id)