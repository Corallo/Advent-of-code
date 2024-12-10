#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
session_id = open("Session", "r").read()
data = get_data(day=4, year=2024,session=session_id)

data = data.split("\n")

s1 = len(data)
s2 = len(data[0])
directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]

match_world = "XMAS"

def search(x, y, dx, dy):
    for i in range(len(match_world)):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or nx >= s1 or ny < 0 or ny >= s2 or data[nx][ny] != match_world[i]:
            return False
    return True

counter = 0
for r in range(s1):
    for c in range(s2):
        for dx, dy in directions:
            if search(r, c, dx, dy):
                counter +=1

print(counter)
#submit(result, part="a", day=3, year=2024, session=session_id)