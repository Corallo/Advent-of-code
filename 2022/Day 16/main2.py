import networkx as nx
import re
import matplotlib.pyplot as plt
import functools
#Read file
with open('./input.txt') as f:
    lines = f.readlines()

#Extract values
lines = [re.findall(r'[A-Z]{2}|\d+|[A-Z]{2}', line) for line in lines]
#make elment 1 int
lines = [[line[0], int(line[1]), line[2:]] for line in lines]
print(lines)

start_node = 'AA'

#Create graph
G = nx.Graph()

for line in lines:
    #if node not in graph, add it
    if line[0] not in G.nodes:
        G.add_node(line[0])
    #Add value to node
    G.nodes[line[0]]['value'] = line[1]
    G.nodes[line[0]]['visited'] = 1
    #Add edges
    for edge in line[2]:
        G.add_edge(line[0], edge, weight=1)

small_G = nx.Graph()
#Keep in small G only nodes that have value != 0 and mantain correct distances between nodes
for node in G.nodes:
    if G.nodes[node]['value'] != 0:
        #Copy node to small_G
        small_G.add_node(node)
        small_G.nodes[node]['value'] = G.nodes[node]['value']
        small_G.nodes[node]['visited'] = G.nodes[node]['visited']

small_G.add_node(start_node)
small_G.nodes[start_node]['value'] = G.nodes[start_node]['value']
small_G.nodes[start_node]['visited'] = G.nodes[start_node]['visited']
for node1 in small_G.nodes:
    for node2 in small_G.nodes:
        if node1 != node2:
            small_G.add_edge(node1, node2, weight=nx.shortest_path_length(G, node1, node2, weight='weight'))
print("Original graph")
print(G.nodes)
print(G.edges)
print("Small graph")
print(small_G.nodes)
print(small_G.edges)
for edge in small_G.edges:
    print(edge, small_G.edges[edge]['weight'])

#Print number of nodes
print("Number of nodes in small_G: ", len(small_G.nodes))

#draw graph
nx.draw(small_G, with_labels=True)
plt.show()



time = 26
current_node = start_node
total_score =0
best_score = 0
@functools.cache
def dfs_human(small_G, current_node, time, total_score):
    global best_score
    # Pruning, stop if best_score is already higher than the current score + the remaining time*sum(values)
    if time <= 0:
        dfs_elephant(small_G, start_node, 26, total_score)
        return 

    #for neighbor of current node
    for neighbor in small_G.neighbors(current_node):
        if small_G.nodes[neighbor]['visited'] == 1:
            small_G.nodes[neighbor]['visited'] = 0
            time_ = time - small_G.edges[current_node, neighbor]['weight']-1
            dfs_human(small_G, neighbor, time_, total_score+(small_G.nodes[neighbor]['value']*time_))
            small_G.nodes[neighbor]['visited'] = 1
    
    if total_score > best_score:
            print("Best score is ", total_score)
            best_score = total_score
@functools.cache
def dfs_elephant(small_G, current_node, time, total_score):
    global best_score
    # Pruning, stop if best_score is already higher than the current score + the remaining time*sum(values)
    if time <= 0:
        if total_score > best_score:
            print("Best score is ", total_score)
            best_score = total_score
        return 

    #for neighbor of current node
    for neighbor in small_G.neighbors(current_node):
        if small_G.nodes[neighbor]['visited'] == 1:
            small_G.nodes[neighbor]['visited'] = 0
            time_ = time - small_G.edges[current_node, neighbor]['weight']-1
            dfs_elephant(small_G, neighbor, time_, total_score+(small_G.nodes[neighbor]['value']*time_))
            small_G.nodes[neighbor]['visited'] = 1
    
    if total_score > best_score:
            print("Best score is ", total_score)
            best_score = total_score

dfs_human(small_G, current_node, time, total_score)
print("Total score is ", best_score)
