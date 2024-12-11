#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt
from functools import lru_cache

session_id = open("Session", "r").read()
data = get_data(day=11, year=2024,session=session_id)

"""with open('2024/day 11/data.txt', 'r') as file:
    data = file.read()"""

print(data)
data=data.strip().split(" ")
data = [int(d) for d in data]
print(data)

iter = 75

#data = {k: data.count(k) for k in data}
print(data)

def process_stone(stone):
    l = len(str(stone))
    if stone == 0:
        stone = 1
    elif l % 2 == 0:
        stone = [int(str(stone)[:l//2]), int(str(stone)[l//2:])]
    else:
        stone *= 2024
    return stone

@lru_cache(maxsize=None)
def process_stones_n_time(stone, n):
    if n == 0:
        return 1
    l = len(str(stone))
    if stone == 0:
        return process_stones_n_time(1, n-1)
    elif l % 2 == 0:
        return process_stones_n_time(int(str(stone)[:l//2]), n-1) + process_stones_n_time(int(str(stone)[l//2:]), n-1)
    else:
        return process_stones_n_time(stone*2024, n-1)

val = 0
for s in data:
    val += process_stones_n_time(s, iter)


print(val)
submit(val, part="b", day=11, year=2024, session=session_id)