from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import heapq

YEAR = 2023
DAY = 18
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
data=data.splitlines()

data = [entry.split("#")[1][:6] for entry in data]

print (data)

pos = (0,0)
sum1 = 0
sum2 = 0
border = 0
for entry in data:
    direction = int(entry[5])
    #extract hex value and convert to decimal
    value = int(entry[:5], 16)
    #0 means R, 1 means D, 2 means L, and 3 means U
    if direction == 0:
        new_pos = (pos[0], pos[1]+value)
    elif direction == 1:
        new_pos = (pos[0]+value, pos[1])
    elif direction == 2:
        new_pos = (pos[0], pos[1]-value)
    elif direction == 3:
        new_pos = (pos[0]-value, pos[1])

    sum1 += pos[0] * new_pos[1]
    sum2 += pos[1] * new_pos[0]
    border += value
    pos = new_pos


area_corr = abs(sum1 - sum2) / 2
result = area_corr + border / 2 + 1

print(result)
assert result > 579831012462
puzzle.answer_b = result