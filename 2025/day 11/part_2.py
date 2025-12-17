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

print(nx.is_directed_acyclic_graph(G))
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

print("finding solution...")

def count_paths_dp(G, start, end):
    nodes = list(nx.topological_sort(G))
    counter = {node: 0 for node in nodes}
    counter[start] = 1
    for node in nodes:
        for neighbor in G.successors(node):
            counter[neighbor] += counter[node]
    return counter[end]

svr_fft=count_paths_dp(G, start="svr", end="fft")
svr_dac=count_paths_dp(G, start="svr", end="dac")
fft_dac=count_paths_dp(G, start="fft", end="dac")
dac_fft=count_paths_dp(G, start="dac", end="fft")
fft_out=count_paths_dp(G, start="fft", end="out")
dac_out=count_paths_dp(G, start="dac", end="out")

print("Paths from svr to fft:", svr_fft)
print("Paths from svr to dac:", svr_dac)
print("Paths from fft to dac:", fft_dac)
print("Paths from dac to fft:", dac_fft)
print("Paths from fft to out:", fft_out)
print("Paths from dac to out:", dac_out)
answer = svr_fft *fft_dac * dac_out \
    + svr_dac * dac_fft * fft_out 

print("Answer:", answer)

submit(answer, part="b", day=11, year=2025, session=session_id)