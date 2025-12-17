#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
import networkx as nx
from itertools import combinations
from tqdm import tqdm
from shapely.geometry import Polygon, Point
session_id = open("Session", "r").read()
data = get_data(day=9, year=2025, session=session_id)
#with open("./2025/day 9/data.txt", "r") as f:
#    data = f.read()
print(data)
data = data.splitlines()
data = [list(map(int, line.split(","))) for line in data]
data = np.array(data)
print(data)

best_pair = None
polygon = Polygon(data)
max_area=0
for i, j in tqdm(combinations(range(len(data)), 2)):
    x1, y1 = data[i]
    x2, y2 = data[j]
    area = (abs(x2 - x1)+1) * (abs(y2 - y1)+1)
    if area > max_area:
        rect = Polygon([
            (x1, y1),
            (x1, y2),
            (x2, y2),
            (x2, y1)
        ])

        if rect.within(polygon):
            max_area = area
            best_pair = (data[i], data[j])

print("Max area:", max_area)
print("Points:", best_pair)

#max_area_2 = max(lambda: abs(data[i][0]-data[j][0]) * abs(data[i][1]-data[j][1]) for i, j in combinations(range(len(data)), 2))
print(max_area)
#print(max_area_2)
submit(max_area, part="b", day=9, year=2025, session=session_id)