#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import re
import numpy as np
import networkx as nx
from tqdm import tqdm
import matplotlib.pyplot as plt
from pyvis.network import Network

DAY=24
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

#set_option('verbose', 10)

with open(f'day {DAY}/input.txt', 'r') as file:
    data = file.read()

inputs, rules = data.split("\n\n")
inputs = [[i.split(": ")[0], int(i.split(": ")[1])] for i in inputs.split("\n")]
print(inputs)

pattern = r'(\w+)\s+(XOR|OR|AND)\s+(\w+)\s+->\s+(\w+)'
rules = re.findall(pattern, rules)
print(rules)

x = 0
y = 0
for i,inp in enumerate(inputs):
    if inp[0].startswith("x"):
        x += 2**int(inp[0][1:]) * inp[1]
print(x)
for i,inp in enumerate(inputs):
    if inp[0].startswith("y"):
        y += 2**int(inp[0][1:]) * inp[1]
print(y)

z = x + y
# print z in binary
print(z)
z_str = bin(z)[2:]
print(z_str)

G = nx.DiGraph()


for r in rules:
    G.add_edge(r[0], r[3], type=r[1])
    G.add_edge(r[2], r[3], type=r[1])


space=4
# Perform a topological sort
def custom_layout(graph):
    positions = {}
    for node in graph.nodes:
        if node.startswith("x"):
            row = int(node[1:])*space
            positions[node] = (0, row)
        elif node.startswith("y"):
            row = int(node[1:])*space + 1
            positions[node] = (0, row)
        elif node.startswith("z"):
            row = int(node[1:])*space + 0.5
            positions[node] = (3, row)
    layer_two_nodes = []
    for node in graph.nodes:
        if node not in positions:
            predecessors = list(graph.predecessors(node))
            for pred in predecessors:
                if pred.startswith("x") and G.edges[pred, node]["type"] == "XOR":
                    row = int(pred[1:]) * space
                    positions[node] = (1, row)
                    layer_two_nodes.append(node)
                    break
                elif pred.startswith("x") and G.edges[pred, node]["type"] == "AND":
                    row = int(pred[1:]) * space
                    positions[node] = (1, row+1)
                    layer_two_nodes.append(node)
                    break

    for node in graph.nodes:
        if node not in positions:
            predecessors = list(graph.predecessors(node))
            for pred in predecessors:
                if pred in  layer_two_nodes:
                    if pred in positions and G.edges[pred, node]["type"] == "OR":
                        row = positions[pred][1]
                        positions[node] = (2, row)
                        break
                    if pred in positions and G.edges[pred, node]["type"] == "AND":
                        row = positions[pred][1]
                        positions[node] = (1.5, row-1)
                        break

    # Here we place the "odd" nodes
    y = 100
    x=4
    remaining_nodes = [node for node in graph.nodes if node not in positions]
    for node in remaining_nodes:
        positions[node] = (4, y)
        y += 2

    return positions


# Apply custom layout
pos = custom_layout(G)
nx.draw(G, pos, with_labels=True, node_size=250)
plt.show()
