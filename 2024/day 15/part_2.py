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

def print_formatted_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def save_formatted_matrix(matrix):
    with open("my_output_small.txt", "a") as file:
        for row in matrix:
            file.write(''.join(row) + '\n')
        file.write('\n')

stone_map,directions=data.split("\n\n")

stone_map = stone_map.replace(".", "..")
stone_map = stone_map.replace("#", "##")
stone_map = stone_map.replace("O", "[]")
stone_map = stone_map.replace("@", "@.")
stone_map = stone_map.split("\n")
stone_map = np.array([list(row) for row in stone_map])

directions=directions.replace("\n", "")
print_formatted_matrix(stone_map)

np.set_printoptions(linewidth=200)

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
    if object_type == ".":
        return False
    if object_type== "@" or direction == "<" or direction == ">":
        if stone_map[y,x] == "#":
            return False
        if stone_map[y,x] == "[" or stone_map[y,x] == "]":
            do_move(stone_map, (y,x), direction)
        if stone_map[y,x] == ".":
            stone_map[y,x] = object_type
            stone_map[object_coords[0],object_coords[1]] = "."
            return True
    elif direction == "^" or direction == "v":
        second_object_coord = (object_coords[0],object_coords[1]+1) if object_type == "[" else (object_coords[0],object_coords[1]-1)
        second_object_type = stone_map[second_object_coord[0],second_object_coord[1]]
        new_coord_2 = calculate_move(second_object_coord, direction)
        y2,x2=new_coord_2
        if stone_map[y,x] == "#" or stone_map[y2,x2] == "#":
            return False
        if stone_map[y,x] == "[" or stone_map[y,x] == "]" or stone_map[y2,x2] == "[" or stone_map[y2,x2] == "]":
            do_move(stone_map, (y,x), direction)
            do_move(stone_map, (y2,x2), direction)
        if stone_map[y,x] == "." and stone_map[y2,x2] == ".":
            stone_map[y,x] = object_type
            stone_map[object_coords[0],object_coords[1]] = "."
            stone_map[y2,x2] = second_object_type
            stone_map[second_object_coord[0],second_object_coord[1]] = "."
            return True
    return False

def calculate_map_score(stone_map):
    score = 0
    for i,row in enumerate(stone_map):
        for j,cell in enumerate(row):
            if cell == "[":
                score += i*100 + j
    return score


for direction in directions:
    print(direction)
    old_stone_map = np.copy(stone_map)
    if do_move(stone_map, find_robot(stone_map), direction) == False:
        stone_map = old_stone_map # ugly way to rewind partial moves if they can't be fully done
    print_formatted_matrix(stone_map)

score=calculate_map_score(stone_map)
print(score)

submit(score, part="b", day=DAY, year=2024, session=session_id)