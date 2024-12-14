#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import re
from z3 import *
import numpy as np
import re

DAY=14
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""


map_x = 101
map_y = 103
middle_x = map_x // 2
middle_y = map_y // 2

data=data.split("\n")
def parse_robot(line):
    pattern = r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)'
    matches = re.findall(pattern, line)
    return matches[0]

data=[parse_robot(line) for line in data]

debug_map = np.zeros((map_y, map_x), dtype=int)
time=100
quadrants = np.array([0,0,0,0])

for line in data:
    x,y=map(int, line[:2])
    vx,vy=map(int, line[2:])
    x=(x + vx*time) % map_x
    y=(y + vy*time) % map_y
    print(x,y)
    debug_map[y,x]+=1
    if x == middle_x or y == middle_y:
        continue
    elif x < middle_x and y < middle_y:  # TL
        quadrants[0] += 1
    elif x > middle_x and y < middle_y:  # TR
        quadrants[1] += 1
    elif x < middle_x and y > middle_y:  # BL
        quadrants[2] += 1
    elif x > middle_x and y > middle_y:  # BR
        quadrants[3] += 1

print(debug_map)
print(quadrants)
solution= quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3]
print(solution)
submit(solution, part="a", day=DAY, year=2024, session=session_id)