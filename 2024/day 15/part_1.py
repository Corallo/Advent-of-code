#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np

DAY=15
session_id = open("Session", "r").read()
data = get_data(day=DAY, year=2024,session=session_id)

"""with open(f'2024/day {DAY}/data.txt', 'r') as file:
    data = file.read()"""


stone_map,directions=data.split("\n\n")

stone_map = stone_map.split("\n")
stone_map = np.array([list(row) for row in stone_map])

directions=directions.replace("\n", "")
print(stone_map)


def find_robot(stone_map):
    robot_coords = np.where(stone_map=="@")
    return robot_coords

def calculate_move(robot_coords, direction):
    y,x=robot_coords
    if direction == "^":
        return (y-1,x)
    elif direction == "v":
        return (y+1,x)
    elif direction == "<":
        return (y,x-1)
    elif direction == ">":
        return (y,x+1)

def do_move(stone_map, object_coords, direction):
    new_coord = calculate_move(object_coords, direction)
    y,x=new_coord
    object_type = stone_map[object_coords[0],object_coords[1]]

    if stone_map[y,x] == "#":
        return False
    if stone_map[y,x] == "O":
        do_move(stone_map, (y,x), direction)
    if stone_map[y,x] == ".":
        stone_map[y,x] = object_type
        stone_map[object_coords[0],object_coords[1]] = "."
        return True
    return False

def calculate_map_score(stone_map):
    score = 0
    for i,row in enumerate(stone_map):
        for j,cell in enumerate(row):
            if cell == "O":
                score += i*100 + j
    return score

for direction in directions:
    print(direction)
    do_move(stone_map, find_robot(stone_map), direction)
    print(stone_map)

score=calculate_map_score(stone_map)


submit(score, part="a", day=DAY, year=2024, session=session_id)