#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
from itertools import combinations
session_id = open("Session", "r").read()
data = get_data(day=8, year=2024,session=session_id)

print(data)
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
        vector = pair[1]-pair[0]
        target = pair[1]
        while True:
            target = target - vector
            if 0 <= target[0] < result_map.shape[0] and 0 <= target[1] < result_map.shape[1]:
                result_map[target[0],target[1]] = "#"
            else:
                break
        target = pair[0]
        while True:
            target = target + vector
            if 0 <= target[0] < result_map.shape[0] and 0 <= target[1] < result_map.shape[1]:
                result_map[target[0],target[1]] = "#"
            else:
                break


print(result_map)
answer = np.sum(result_map=="#")
print(answer)
submit(answer, part="b", day=8, year=2024, session=session_id)