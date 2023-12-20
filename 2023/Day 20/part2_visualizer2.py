from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout
YEAR = 2023
DAY = 20
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data

#data = puzzle.examples[0][0]

print(data)

def parse_schematics(data):
    schematics = {}

    for part in data.splitlines():
        name, targets = part.split(" -> ")
        type = None
        if name[0] == "%":
            name = name[1:]
            type = "flip"
            status = 0
        elif name[0] == "&":
            name = name[1:]
            type = "conj"
            status = {}
        else:
            type = "brod"
            status = None
        targets = targets.split(", ")
        schematics[name] = {"type":type,"outputs": targets,"state": status}

    #Set inital state of conj parts
    for name_conj, part_conj in schematics.items():
        if part_conj["type"] == "conj":
            state = {}
            for name, part in schematics.items():
                if name_conj in part["outputs"]:
                    state[name] = 0
            part_conj["state"] = state
    return schematics


schematics = parse_schematics(data)
print(schematics)
signal_queue = []


#visualize schematics as graph

G = nx.DiGraph()
for name, part in schematics.items():
    for output in part["outputs"]:
        G.add_edge(name, output)

#distances = nx.single_source_shortest_path_length(G, 'broadcaster')
"""
y_positions = {}

# Set the x-axis position based on the distances and y-axis position incrementally
pos = {}
for node in G.nodes():
    x_value = distances[node]
    if x_value not in y_positions:
        y_positions[x_value] = 0  # Initialize y-axis position
    y_value = y_positions[x_value]
    pos[node] = (x_value, y_value)
    y_positions[x_value] += 1  # Increment y-axis position for the next node with the same x-axis value
"""
#initial position for each node at 0,0

pos = {}
for node in G.nodes():
    pos[node] = (0,0)

"""set manually these positions
boradcaster -5,0
qs -0 -5
bx -0 -3
pz -0 +3
lp -0 +5

rx 8,0
vr 7,0"""

pos["broadcaster"] = (-5,0)
pos["qs"] = (0,-5)
pos["bx"] = (0,-3)
pos["pz"] = (0,3)
pos["lp"] = (0,5)
pos["rx"] = (8,0)
pos["vr"] = (7,0)
pos["bm"] = (6,-5)
pos["cl"] = (7,-3)
pos["dr"] = (6,5)
pos["tn"] = (7,3)

# Create a layout with left-to-right ordering
pos = nx.spring_layout(G,pos=pos, fixed=["broadcaster", "rx","qs","bx","pz","lp","vr","bm","cl","dr","tn"], center = (0,0), k=0.5, iterations=1000)

#print node by distance to "rx" using pos to calculate distance
distances = {}
for node in G.nodes():
    distances[node] = np.linalg.norm(np.array(pos[node])-np.array(pos["rx"]))
#sort distances
distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
print(distances)


# Draw the graph
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000, node_color="lightblue", font_color="black", font_size=10, arrowsize=20)


# Draw the graph
#nx.draw(G,  with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black', font_weight='bold', arrowsize=15)

plt.show()
