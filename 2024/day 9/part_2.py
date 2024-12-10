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

def find_right_most_series(data, start):
    i = start
    while data[i] == -1:
        i -= 1
    j = i
    while data[j] == data[i] and j > 0 :
        j-=1

    return j+1, i+1

def find_left_most_free_space_of_size_n(data, n ,limit):
    i=0
    while i < limit:
        while data[i] != -1 and i<limit:
            i+=1
        j = i
        while j < len(data) and data[j] == -1:
            j+=1
        if j-i >= n:
            return i, j
        else:
            i=j+1
    return None, None
new_data=generate_string(data)
print(new_data)

new_data = [int(d) if d != "." else -1 for d in new_data]

free_space = {}
for i in range(len(new_data)):
    if new_data[i] == -1:
        for j in range(i+1,len(new_data)):
            if new_data[j] != -1:
                free_space[i] = j-i
                break
print(free_space)
print(new_data[:200])
i = len(new_data) - 1

while True:
    start, end = find_right_most_series(new_data, i)
    print(start)
    lenght = end-start
    if lenght == 0:
        break
    free_start, free_end = find_left_most_free_space_of_size_n(new_data, lenght, limit=start)
    if free_start is None:
        i = start - 1
        continue
    new_data[free_start:free_start + lenght] = new_data[start:end]
    new_data[start:end] =  [-1]*lenght
    i = start - 1


print(new_data[:100])
answer = 0
for i,e in enumerate(new_data):
    if e != -1:
        answer += i*int(e)
print(answer)

submit(answer, part="b", day=9, year=2024, session=session_id)