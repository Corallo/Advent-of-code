#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
from itertools import combinations
session_id = open("Session", "r").read()
data = get_data(day=8, year=2024,session=session_id)


data=data.strip()
data = data.split("\n")
data = np.array([list(d) for d in data])
unique_symbles = np.unique(data)
print(unique_symbles)

result_map = np.zeros_like(data)
for symble in unique_symbles:
    if symble == ".":
        continue
    antenna_coordinates = np.array(np.where(data==symble)).T
    print(symble, antenna_coordinates)
    pairs = list(combinations(antenna_coordinates, 2))
    print(pairs)
    for pair in pairs:

        target_1 = pair[0] - (pair[1]-pair[0]) if np.any(pair[0] - (pair[1]-pair[0]) != pair[1]) else pair[0] + (pair[1]-pair[0])
        target_2 = pair[1] + (pair[1]-pair[0]) if np.any(pair[1] + (pair[1]-pair[0]) != pair[0]) else pair[1] - (pair[1]-pair[0])

        print(target_1,target_2)
        if 0 <= target_1[0] < result_map.shape[0] and 0 <= target_1[1] < result_map.shape[1]:
            result_map[target_1[0],target_1[1]] = "#"
        if 0 <= target_2[0] < result_map.shape[0] and 0 <= target_2[1] < result_map.shape[1]:
            result_map[target_2[0],target_2[1]] = "#"


print(result_map)
answer = np.sum(result_map=="#")
print(answer)
submit(answer, part="a", day=8, year=2024, session=session_id)