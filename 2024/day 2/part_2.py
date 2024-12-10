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

print(len(data))
good_list= {}
for i in range(len(data)):
    array =  np.array(data[i])
    for j in range(len(data[i])):
        modified_array = np.delete(array, j)
        safe = verify_safe(modified_array.tolist())
        if i not in good_list or good_list[i] == 0:
            good_list[i] = safe

answer=0
for x in good_list:
    answer+=good_list[x]
print(answer)

submit(answer, part="b", day=2, year=2024, session=session_id)