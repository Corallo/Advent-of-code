#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
session_id = open("Session", "r").read()
data = get_data(day=2, year=2024,session=session_id)

data = data.split("\n")
data = [d.split(" ") for d in data]

data = [[int(x) for x in sublist] for sublist in data]
score = 0

def verify_safe(line):
    safe = abs(line[1] - line[0]) <= 3 and abs(line[1] - line[0]) > 0
    increasing = line[1] > line[0]
    for j in range(1,len(line)-1):
        if (line[j+1] > line[j] ) != increasing:
            safe = 0
        if abs(line[j+1] - line[j] ) > 3 or abs(line[j+1] - line[j] ) ==0 :
            safe = 0
    return safe


for i in range(len(data)):
    safe = verify_safe(data[i])
    score += safe
print(score)

submit(score, part="a", day=2, year=2024, session=session_id)