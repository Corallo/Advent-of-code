#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
from tqdm import tqdm
import networkx as nx
import matplotlib.pyplot as plt
from skimage.morphology import flood
from scipy.ndimage import convolve


DAY=12
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""

print(data)
data=data.strip().split("\n")
data = np.array([list(d) for d in data])
data = np.vectorize(ord)(data)
print(data)

def calculate_score(grid):
    zones = np.zeros_like(grid, dtype=int)
    connectivity = np.array([[0,1,0],
                    [1,1,1],
                    [0,1,0]])
    zone_id = 0
    score = 0
    total_area = 0
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if zones[i, j] == 0:
                zone_id += 1
                mask = flood(grid, (i, j), footprint=connectivity)
                zones += mask*zone_id
                primeter = calculate_perimeter(mask)
                score += count_area(mask)*primeter
                total_area += count_area(mask)

    assert total_area == zones.shape[0]*zones.shape[1]
    return score

def count_area(mask):
    return np.sum(mask)

# Reimplement this with a proper convolution instead of doing this shit loops manually
def calculate_perimeter(mask):
    padded_mask = np.pad(mask, pad_width=2, mode='constant', constant_values=0)

    kernel = np.array([[0, 1, 0],
                    [1, -1, 1],
                    [0, 1, 0]])

    # Convolve to find boundary pixels
    count=0
    for i in range(1,padded_mask.shape[0]-1):
        for j in range(1,padded_mask.shape[1]-1):
            if padded_mask[i, j]==0:
                count += np.sum(padded_mask[i-1:i+2,j-1:j+2]*kernel)

    return count



answer = calculate_score(data)
print(answer)

answer = calculate_score(data)
print(answer)
#answer = len(data)
#submit(answer, part="a", day=DAY, year=2024, session=session_id)