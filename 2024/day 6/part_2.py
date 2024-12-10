#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
from tqdm import tqdm
session_id = open("Session", "r").read()
data = get_data(day=6, year=2024,session=session_id)

data=data.split("\n")
data=[list(d) for d in data]
data = np.array(data)
print(data)

start_position = np.where(data=="^")
start_position = np.array([start_position[0][0], start_position[1][0]])
print(start_position)



result=0
data[start_position[0], start_position[1]] = "*"
color_map = np.copy(data)
color_map[color_map == "#"] = 1
color_map[color_map == "."] = 0
color_map[color_map == "*"] = 2


def search (start_position, data):
    # TODO: It would be more efficient to memorize visited cells and the direction when visited
    # but it is still O(N`2) so meh
    d_idx = 0
    directions = np.array([[-1,0],[0,1],[1,0],[0,-1]])
    max_time = data.shape[0]*data.shape[1]
    while max_time:
        new_position = start_position + directions[d_idx]
        if new_position[0]<0 or new_position[0]>=data.shape[0] or new_position[1]<0 or new_position[1]>=data.shape[1]:
            return 0
        elif data[new_position[0], new_position[1]] == "#":
            d_idx = (d_idx+1)%4
            continue
        elif data[new_position[0], new_position[1]] != "*":
            data[new_position[0], new_position[1]] = "*"
        start_position = new_position
        max_time -= 1
    return 1


for idx in tqdm(range(data.size)):
    i, j = divmod(idx, data.shape[1])
    if data[i,j] == ".":
        data[i,j] = "#"
        result += search(start_position, data.copy())
        data[i,j] = "."

print(result)
submit(result, part="b", day=6, year=2024, session=session_id)