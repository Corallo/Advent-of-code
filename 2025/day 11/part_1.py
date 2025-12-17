#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
import re
import networkx as nx
session_id = open("Session", "r").read()
data = get_data(day=11, year=2025, session=session_id)
#with open("./2025/day 11/data.txt", "r") as f:
#    data = f.read()
data = data.splitlines()
re = re.compile(r"(.*): (.*)")
parsed_data = []
for line in data:
    match = re.match(line)
    source = match.group(1)
    out = list(match.group(2).split(" "))
    parsed_data.append((source, out))
data = parsed_data

G = nx.DiGraph()
for line in data:
    source, out = line
    for dest in out:
        G.add_edge(source, dest)
        print(f"Added edge from {source} to {dest}")

answer = len(list(nx.all_simple_paths(G, source="you", target="out")))
print("Answer:", answer)
submit(answer, part="a", day=11, year=2025, session=session_id)