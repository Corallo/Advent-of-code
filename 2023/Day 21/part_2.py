from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import networkx as nx
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

YEAR = 2023
DAY = 21
puzzle = Puzzle(year=YEAR, day=DAY)
TESTING = False
data = puzzle.input_data

if TESTING:
    data = puzzle.examples[0][0]

#with open("Day 21/map_expand.txt", "r") as f:
#    data_test= f.read()

original_len = len(data.splitlines()[0])
print("original map size", len(data.splitlines()), len(data.splitlines()[0]))


#Repeate the map n times in each direction
def expand_map(original_map, _n):
    n = _n*2+1
    rows = len(original_map)
    cols = len(original_map[0])

    start_pos = None
    #Replace S with .
    for y in range(rows):
        for x in range(cols):
            if original_map[y][x] == "S":
                start_pos = (x,y)
                original_map[y] = original_map[y][:x] + "." + original_map[y][x+1:]

    # Expand the map horizontally
    expanded_map = [row * n for row in original_map]

    # Expand the map vertically
    expanded_map = expanded_map * n

    new_start_pos = (start_pos[0] + cols*_n, start_pos[1] + rows*_n)
    expanded_map[new_start_pos[1]] = expanded_map[new_start_pos[1]][:new_start_pos[0]] + "S" + expanded_map[new_start_pos[1]][new_start_pos[0]+1:]


    return "\n".join(expanded_map)

# Biggest map my pc can handled in 1-2 minutes
map_rep = 5
data = expand_map(data.splitlines(), map_rep)
print("Map expanded")

#assert data == data_test

G = nx.DiGraph()

for y, line in enumerate(data.splitlines()):
    for x, char in enumerate(line):
        if char == "#":
            continue
        if char == ".":
            G.add_node((x,y))
        if char == "S":
            start = (x,y)
            G.add_node(start)
print("Nodes added")
#add edges
for y in range(len(data.splitlines())):
    for x in range(len(data.splitlines()[y])):
        if (x,y) in G:
            if (x+1,y) in G:
                G.add_edge((x,y),(x+1,y))
            if (x-1,y) in G:
                G.add_edge((x,y),(x-1,y))
            if (x,y+1) in G:
                G.add_edge((x,y),(x,y+1))
            if (x,y-1) in G:
                G.add_edge((x,y),(x,y-1))
print("Edges added")
#Find the shortest path from start to all nodes

shortest_paths = nx.single_source_shortest_path_length(G, start)
print("Shortest paths found")


print("Generating solution dictionary")
required_steps = 26501365


# Here I try to generate the "releavant" solutions for the problem as the number of steps increase, so I can fit a curve to it and find the solution for the problem
# To make it faster, and easier to fit the function, I only generate the solutions for the steps that are multiple of the original map size
# Not sure at all if this make sense or not, but it worked
sol_dict = {}
for path_size in tqdm(range(required_steps%original_len, (original_len*map_rep)+(required_steps%original_len)+1, original_len)):
    shortest_paths_filtered = {k:v for k,v in shortest_paths.items() if v%2 == path_size%2 and v <= path_size}
    #print("In %d Steps, he can reach %d nodes"%(path_size, len(shortest_paths_filtered)))
    sol_dict[path_size] = len(shortest_paths_filtered)


# plot the curve, to see if it makes sense.
# Plotting it in step of 1 instead of original_len make the curve look really smooth, but doesn't seem to be very reliable
# I suspect the curve is not really a polynomial (at least of order 2), unless you mange to sample the points exactly at the size of the map, or something like that

plt.plot(list(sol_dict.keys()), list(sol_dict.values()))
plt.show()


def fit_function(x, a, b, c):
    return a*x**2 + b*x + c

print("Fitting curve")
# Perform the curve fitting
params, covariance = curve_fit(fit_function, list(sol_dict.keys()), list(sol_dict.values()))
print("Parameters estimated:", params)
print("Covariance matrix:", covariance)

x=26501365
solution = int(fit_function(x, *params)+1)

if TESTING:
    for test in [6,10,50,100,500,1000,5000]:
        print("In %d steps he can reach %d nodes"%(test, fit_function(test, *params)))
print(solution)

# This assertion is the result spitted out from fitting all the points, instead of steps of original_len, it was off quite a lot
assert solution > 608150363135920
puzzle.answer_b = solution
