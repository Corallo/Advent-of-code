from aocd.models import Puzzle
import re
import numpy as np
YEAR = 2023
DAY = 10
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#with open("./Day 10/data.txt", "r") as f:
#    data = f.read()
print(data)

# split by \n and convert to int
data = data.split("\n")
#Split each line of data into a list of characters
data = [list(line) for line  in data]
print(data)


#Find start position "S"

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "S":
            start = [y,x]

print(start, data[start[0]][start[1]])

def find_next_pipe(loc, previouse_loc):
    if data[loc[0]][loc[1]] == "S":
        if loc[0] > 0:
            if data[loc[0]-1][loc[1]] == "|" or data[loc[0]-1][loc[1]] == "F" or data[loc[0]-1][loc[1]] == "7":
                return [loc[0]-1, loc[1]]
        if loc[0] < len(data)-1:
            if data[loc[0]+1][loc[1]] == "|" or data[loc[0]+1][loc[1]] == "J" or data[loc[0]+1][loc[1]] == "L":
                return [loc[0]+1, loc[1]]

        if loc[1] > 0:
            if data[loc[0]][loc[1]-1] == "-" or data[loc[0]][loc[1]-1] == "L" or data[loc[0]][loc[1]-1] == "F":
                return [loc[0], loc[1]-1]
        if loc[1] < len(data[loc[1]])-1:
            if data[loc[0]][loc[1]+1] == "-" or data[loc[0]][loc[1]+1] == "J" or data[loc[0]][loc[1]+1] == "7":
                return [loc[0], loc[1]+1]
    else:
        if data[loc[0]][loc[1]] == "|":
            if previouse_loc[0] > loc[0]:
                    return [loc[0]-1, loc[1]]
            if previouse_loc[0] < loc[0]:
                    return [loc[0]+1, loc[1]]
        if data[loc[0]][loc[1]] == "-":
            if previouse_loc[1] > loc[1]:
                    return [loc[0], loc[1]-1]
            if previouse_loc[1] < loc[1]:
                    return [loc[0], loc[1]+1]
        if data[loc[0]][loc[1]] == "F":
            if previouse_loc[0] > loc[0]:
                    return [loc[0], loc[1]+1]
            if previouse_loc[1] > loc[1]:
                    return [loc[0]+1, loc[1]]
        if data[loc[0]][loc[1]] == "J":
            if previouse_loc[0] < loc[0]:
                    return [loc[0], loc[1]-1]
            if previouse_loc[1] < loc[1]:
                    return [loc[0]-1, loc[1]]
        if data[loc[0]][loc[1]] == "7":
            if previouse_loc[0] > loc[0]:
                    return [loc[0], loc[1]-1]
            if previouse_loc[1] < loc[1]:
                    return [loc[0]+1, loc[1]]
        if data[loc[0]][loc[1]] == "L":
            if previouse_loc[0] < loc[0]:
                    return [loc[0], loc[1]+1]
            if previouse_loc[1] > loc[1]:
                    return [loc[0]-1, loc[1]]

counter = 0

current_loc = find_next_pipe(start, start)
print(current_loc, data[current_loc[0]][current_loc[1]])
old_loc = start
counter += 1
while data[current_loc[0]][current_loc[1]] != "S":
    tmp = current_loc
    current_loc = find_next_pipe(current_loc, old_loc)
    old_loc = tmp
    counter +=1
    print(current_loc, data[current_loc[0]][current_loc[1]])

print(counter)
puzzle.answer_a = counter/2