#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import networkx as nx
session_id = open("Session", "r").read()
data = get_data(day=5, year=2024,session=session_id)

rules, manuals = data.split("\n\n")
print(rules)
print(manuals)
rules = [[int(r[0:2]), int(r[3:])] for r in rules.split("\n")]
manuals = [m.split(",") for m in manuals.split("\n")]
manuals = [[int(m) for m in manual] for manual in manuals]
rules = np.array(rules)
print("===================")

result=0
for manual in manuals:
    small_g = nx.DiGraph()
    for r in rules:
        if r[0] in manual and r[1] in manual:
            small_g.add_edge(r[0], r[1])
    sorted_manual = list(nx.topological_sort(small_g))
    if(sorted_manual != manual):
        result += sorted_manual[len(manual)//2]

print(result)
#submit(result, part="b", day=5, year=2024, session=session_id)