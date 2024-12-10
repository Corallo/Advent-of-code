#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
session_id = open("Session", "r").read()
data = get_data(day=6, year=2024,session=session_id)

data=data.split("\n")
data=[list(d) for d in data]
data = np.array(data)
print(data)

start_position = np.where(data=="^")
start_position = np.array([start_position[0][0], start_position[1][0]])
print(start_position)

directions = np.array([[-1,0],[0,1],[1,0],[0,-1]])
continue_search = True
d_idx = 0
result=1
data[start_position[0], start_position[1]] = "*"
color_map = np.copy(data)
color_map[color_map == "#"] = 1
color_map[color_map == "."] = 0
color_map[color_map == "*"] = 2

while continue_search:
    new_position = start_position + directions[d_idx]
    if new_position[0]<0 or new_position[0]>=data.shape[0] or new_position[1]<0 or new_position[1]>=data.shape[1]:
        break
    elif data[new_position[0], new_position[1]] == "#":
        d_idx = (d_idx+1)%4
        continue
    elif data[new_position[0], new_position[1]] != "*":
        data[new_position[0], new_position[1]] = "*"
        result += 1
    start_position = new_position
    print(data)

print(result)
print(data)
submit(result, part="a", day=6, year=2024, session=session_id)