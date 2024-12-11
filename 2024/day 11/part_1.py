#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt

session_id = open("Session", "r").read()
data = get_data(day=11, year=2024,session=session_id)

"""with open('2024/day 11/data.txt', 'r') as file:
    data = file.read()"""

print(data)
data=data.strip().split(" ")
data = [int(d) for d in data]
print(data)

iter = 25

def process_stones(stones):
    for i in range(len(stones)):
        l = len(str(stones[i]))
        if stones[i] == 0:
            stones[i] = 1
        elif l % 2 == 0:
            stones[i] = [int(str(stones[i])[:l//2]), int(str(stones[i])[l//2:])]
        else:
            stones[i] *= 2024
    return stones




for _ in tqdm(range(iter)):
    data = process_stones(data)
    #flattening the list
    data = [item for sublist in data for item in ([sublist] if isinstance(sublist, int) else sublist)]

answer = len(data)
submit(answer, part="a", day=11, year=2024, session=session_id)