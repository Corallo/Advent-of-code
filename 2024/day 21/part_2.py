#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle

import networkx as nx
from functools import lru_cache
import matplotlib.pyplot as plt

DAY=21
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)


"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""

data = data.split("\n")
data = [list(d) for d in data]

print(data)


number_G = nx.DiGraph()

number_G.add_edge("7", "8", direction=">")
number_G.add_edge("8", "9", direction=">")
number_G.add_edge("4", "5", direction=">")
number_G.add_edge("5", "6", direction=">")
number_G.add_edge("1", "2", direction=">")
number_G.add_edge("2", "3", direction=">")
number_G.add_edge("0", "A", direction=">")
number_G.add_edge("7", "4", direction="v")
number_G.add_edge("8", "5", direction="v")
number_G.add_edge("9", "6", direction="v")
number_G.add_edge("4", "1", direction="v")
number_G.add_edge("5", "2", direction="v")
number_G.add_edge("6", "3", direction="v")
number_G.add_edge("2", "0", direction="v")
number_G.add_edge("3", "A", direction="v")

number_G.add_edge("8", "7", direction="<")
number_G.add_edge("9", "8", direction="<")
number_G.add_edge("5", "4", direction="<")
number_G.add_edge("6", "5", direction="<")
number_G.add_edge("2", "1", direction="<")
number_G.add_edge("3", "2", direction="<")
number_G.add_edge("A", "0", direction="<")
number_G.add_edge("4", "7", direction="^")
number_G.add_edge("5", "8", direction="^")
number_G.add_edge("6", "9", direction="^")
number_G.add_edge("1", "4", direction="^")
number_G.add_edge("2", "5", direction="^")
number_G.add_edge("3", "6", direction="^")
number_G.add_edge("0", "2", direction="^")
number_G.add_edge("A", "3", direction="^")



#display
#nx.draw(number_G, with_labels=True)
#plt.show()

arrow_G = nx.DiGraph()

arrow_G.add_edge("^", "A", direction=">")
arrow_G.add_edge("<", "v", direction=">")
arrow_G.add_edge("v", ">", direction=">")
arrow_G.add_edge("v", "^", direction="^")
arrow_G.add_edge(">", "A", direction="^")

arrow_G.add_edge("A", "^", direction="<")
arrow_G.add_edge("v", "<", direction="<")
arrow_G.add_edge(">", "v", direction="<")
arrow_G.add_edge("^", "v", direction="v")
arrow_G.add_edge("A", ">", direction="v")

#display
#nx.draw(arrow_G, with_labels=True)
#plt.show()

def find_all_shortest_paths_numberpad(G, nodes):
    all_paths = []
    for i in range(len(nodes) - 1):
        start = nodes[i]
        end = nodes[i + 1]
        paths = list(nx.all_shortest_paths(G, start, end))
        if i == 0:
            all_paths = paths
        else:
            new_paths = []
            for path in all_paths:
                for p in paths:
                    new_paths.append( path +p[1:])
            all_paths = new_paths
    for i,p in enumerate(all_paths):
        all_paths[i] = find_directions(G, p, nodes[1:])
    min_len=float('inf')
    for path in all_paths:
        if count_changes_in_path(path) < min_len:
            min_len = count_changes_in_path(path)
    return [path for path in all_paths if count_changes_in_path(path) == min_len]

# This function is probably not useful at this point, it should be removed
def count_changes_in_path(path):
    count=0
    for i in range(len(path)-1):
        if path[i]!= path[i+1]:
            count += 1
    return count

def find_directions(G, nodes, target_node):
    directions = []
    j=0
    for i in range(len(nodes) - 1):
        start = nodes[i]
        end = nodes[i + 1]
        directions.append(G[start][end]["direction"])
        while j<len(target_node) and end == target_node[j]:
            j += 1
            directions.append("A")
    return directions

def find_all_shortest_paths_pad(G, start, end):
    paths =  list(nx.all_shortest_paths(G, start, end))
    all_paths = []
    for path in paths:
        directions = find_directions(G, path, [end])
        if directions == []:
            directions = ["A"]
        all_paths.append(directions)
    return all_paths

@lru_cache
def recursive_find_len(sequence, n):
    if n==0:
        return len(sequence)
    start_node = "A"

    l =0
    for end_node in sequence:
        paths = find_all_shortest_paths_pad(arrow_G, start_node, end_node)
        l += min(recursive_find_len("".join(path), n - 1) for path in paths)
        start_node=end_node

    return l


n=25
answer = 0
for code in data:
    number_shortest_paths = find_all_shortest_paths_numberpad(number_G, ["A"] + code)
    shortest_len = min(recursive_find_len("".join(number_path),n) for number_path in number_shortest_paths)


    str_code = "".join(code)
    print(f"{str_code}: {int(str_code[:-1])}*{shortest_len}= {int(str_code[:-1])*shortest_len}")
    answer += int(str_code[:-1])*shortest_len

print(answer)
submit(answer, part="b", day=DAY, year=2024, session=session_id)