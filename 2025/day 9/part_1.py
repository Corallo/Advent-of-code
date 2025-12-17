#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
import numpy as np
from itertools import combinations
from tqdm import tqdm
session_id = open("Session", "r").read()
data = get_data(day=9, year=2025, session=session_id)
#with open("./2025/day 9/data.txt", "r") as f:
#    data = f.read()
data = data.splitlines()
data = [list(map(int, line.split(","))) for line in data]
data = np.array(data)
print(data)

max_area=0
for i, j in tqdm(combinations(range(len(data)), 2)): # all pairs of points
    #print("Pair:", data[i], data[j])
    area = abs(data[i][0]-data[j][0]+1) * abs(data[i][1]-data[j][1]+1)
    #print("Area:", area)
    if area > max_area:
        max_area = area
        print("New max area:", max_area)
        print("Points:", data[i], data[j])
print(max_area)
submit(max_area, part="a", day=9, year=2025, session=session_id)