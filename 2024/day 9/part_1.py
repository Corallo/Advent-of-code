#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
from tqdm import tqdm

session_id = open("Session", "r").read()
data = get_data(day=9, year=2024,session=session_id)

data = list(data.strip())
print(data)


def generate_string(compact_data):
    d_id = 0
    result_string = []
    for d in range(len(compact_data)):
        if d % 2 == 0:
            result_string.extend([d_id]*int(compact_data[d]))
            d_id +=1
        else:
            result_string.extend(["."]*int(compact_data[d]))
    return result_string


new_data=generate_string(data)
print(new_data)
new_data = [int(d) if d != "." else -1 for d in new_data]
last_j= 0
for i in tqdm(range(len(new_data) - 1, -1, -1)):
    if new_data[i] != -1:
        for j in range(last_j,len(new_data)):
            if j > i:
                break
            if new_data[j] == -1:
                new_data[j] = new_data[i]
                new_data[i] = -1
                last_j = j-1
                break
print(new_data[:100])
answer = 0
for i,e in enumerate(new_data):
    if e != -1:
        answer += i*int(e)
print(answer)
submit(answer, part="a", day=9, year=2024, session=session_id)