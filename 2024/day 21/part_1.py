#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle


import networkx as nx

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



def find_all_shortest_paths(G, nodes):
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
                    new_paths.append(path + p[1:])
            all_paths = new_paths
    return all_paths

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
answer = 0
for code in data:
    shorest_len = 1_000_000
    best_path= ""
    number_shortest_paths = find_all_shortest_paths(number_G, ["A"] + code)
    for number_path in number_shortest_paths:
        arrow_code_1 = find_directions(number_G, number_path, code)
        arrow_shortest_paths_1 = find_all_shortest_paths(arrow_G, ["A"] + arrow_code_1)
        for arrow_path in arrow_shortest_paths_1:
            arrow_code_2 = find_directions(arrow_G, arrow_path, arrow_code_1)
            arrow_shortest_paths_2 = find_all_shortest_paths(arrow_G, ["A"] + arrow_code_2)
            for arrow_path_2 in arrow_shortest_paths_2:
                arrow_code_3 = find_directions(arrow_G, arrow_path_2, arrow_code_2)
                if len(arrow_code_3)<shorest_len:
                    shorest_len= len(arrow_code_3)
                    best_path = arrow_code_3
    str_code = "".join(code)
    best_path = "".join(best_path)
    print(f"Shortest path for {str_code}, {best_path}")
    print(f"{str_code}: {int(str_code[:-1])}*{shorest_len}= {int(str_code[:-1])*shorest_len}")
    answer += int(str_code[:-1])*shorest_len

print(answer)
#submit(answer, part="a", day=DAY, year=2024, session=session_id)