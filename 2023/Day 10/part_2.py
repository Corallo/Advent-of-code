from aocd.models import Puzzle
import re
import numpy as np
import sys
YEAR = 2023
DAY = 11
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
positions = []
positions.append(start)
current_loc = find_next_pipe(start, start)
positions.append(current_loc)
#print(current_loc, data[current_loc[0]][current_loc[1]])
old_loc = start
counter += 1
while data[current_loc[0]][current_loc[1]] != "S":
    tmp = current_loc
    current_loc = find_next_pipe(current_loc, old_loc)
    positions.append(current_loc)
    old_loc = tmp
    counter +=1
    #print(current_loc, data[current_loc[0]][current_loc[1]])


# create a new array with the same size as data containing only "." doubling the resolution
print(len(data), len(data[0]))
pipe_map = np.full((len(data)*2, len(data[0])*2), ".")
positions = [[int(x*2) for x in pos] for pos in positions]
print(len(pipe_map), len(pipe_map[0]))

for i in range(len(positions)):
    if i == 0:
        pos = positions[i]
        pipe_map[pos[0]][pos[1]] = "*"
    else:
        # add * to the current position and in the middle of the previous and current position
        pos = positions[i]
        prev_pos = positions[i-1]
        pipe_map[pos[0]][pos[1]] = "*"
        pipe_map[int((pos[0]+prev_pos[0])/2)][int((pos[1]+prev_pos[1])/2)] = "*"
print(pipe_map)


def count_enclosed_dots():
    rows = len(pipe_map)
    cols = len(pipe_map[0])
    sys.setrecursionlimit(len(pipe_map)*len(pipe_map[0]))
    def dfs(i, j):
        if 0 <= i  and i < rows and 0 <= j and j < cols and pipe_map[i][j] == '.':
            pipe_map[i][j] = 'O'  # Mark the cell as visited to avoid double counting
            dfs(i+1,j)
            dfs(i+1,j+1)
            dfs(i+1,j-1)
            dfs(i-1,j)
            dfs(i-1,j+1)
            dfs(i-1,j-1)
            dfs(i,j+1)
            dfs(i,j-1)


    #start dfs from the edges
    for i in range(rows):
        dfs(i, 0)
        dfs(i, cols-1)
    for j in range(cols):
        dfs(0, j)
        dfs(rows-1, j)

    count = 0
    for i in range(0,rows,2):
        for j in range(0,cols,2):
            if pipe_map[i][j] == '.':
                count += 1


    return count

result = count_enclosed_dots()
print(pipe_map)
print(result)

puzzle.answer_b = result