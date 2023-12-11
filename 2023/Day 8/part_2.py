from aocd.models import Puzzle
from math import lcm
import re
import numpy as np
YEAR = 2023
DAY = 8
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data

#read data from file
#with open("./Day 8/data.txt", "r") as f:
#    data = f.read()

print(data)
data = data.split("\n\n")
planned_path = data[0]
data = data[1]
data = data.split("\n")
print(data)
data=[re.findall(r'\w+', s) for s in data]

print(data)
maze = {}
for line in data:
    maze[line[0]] = [line[1], line[2]]

print(maze)


#Find nodes ending with A
nodes = [x for x in maze.keys() if x[-1] == "A"]
print(nodes)

print(planned_path)
counters = []
for node in nodes:
    count = 0
    while node[-1] != "Z":
        if planned_path[count%len(planned_path)] == "L":
            node = maze[node][0]
            #print(nodes)
        else:
            node = maze[node][1]
            #print(nodes)
        count += 1
    counters.append(count)


print(counters)
print(lcm(*counters))
puzzle.answer_b = lcm(*counters)