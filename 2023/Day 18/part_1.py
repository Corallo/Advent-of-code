from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
import heapq

YEAR = 2023
DAY = 18
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#Save data to file
with open("./Day 18/input.txt", "w") as f:
    f.write(data)
#data = puzzle.examples[0][0]
data=data.splitlines()

data = [(entry.split()[0], int(entry.split()[1])) for entry in data]

print (data)

#sum all data containing "D" as first character
height = (sum([entry[1] for entry in data if entry[0][0] == "D"])+1)*2
width  = (sum([entry[1] for entry in data if entry[0][0] == "R"])+1)*2

area = np.zeros((height, width))
pos = height//2, width//2

for entry in data:
    if entry[0] == "D":
        area[pos[0]:pos[0]+entry[1]+1, pos[1]] = 1
        pos = pos[0]+entry[1], pos[1]
    if entry[0] == "U":
        area[pos[0]-entry[1]:pos[0]+1, pos[1]] = 1
        pos = pos[0]-entry[1], pos[1]
    if entry[0] == "R":
        area[pos[0], pos[1]:pos[1]+entry[1]+1] = 1
        pos = pos[0], pos[1]+entry[1]
    if entry[0] == "L":
        area[pos[0], pos[1]-entry[1]:pos[1]+1] = 1
        pos = pos[0], pos[1]-entry[1]


print(area)
print(np.sum(area))

#remove all lines with only zeros
area = area[np.sum(area, axis=1) != 0]
#remove all columns with only zeros
area = area[:, np.sum(area, axis=0) != 0]

np.savetxt("./Day 18/output_outer.txt", area, fmt="%d")

def flood_fill(matrix, x, y):
    stack = [(x, y)]

    while stack:
        current_x, current_y = stack.pop()
        if matrix[current_x][current_y] == 0:
            matrix[current_x][current_y] = 1

            # Check and add neighboring pixels
            neighbors = [
                (current_x + 1, current_y),
                (current_x - 1, current_y),
                (current_x, current_y + 1),
                (current_x, current_y - 1)
            ]

            stack.extend((nx, ny) for nx, ny in neighbors if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]))

    return matrix

area = flood_fill(area, 150, 10)



print(area)
print(np.sum(area))
print(area.shape)

#save to file
np.savetxt("./Day 18/output.txt", area, fmt="%d")

result = np.sum(area)
puzzle.answer_a = result