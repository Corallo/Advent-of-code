from aocd.models import Puzzle
import networkx as nx
import re
YEAR = 2023
DAY = 8
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
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

print(planned_path)
count = 0
node = "AAA"
while node != "ZZZ":
    if planned_path[count%len(planned_path)] == "L":
        node = maze[node][0]
        print(node)
    else:
        node = maze[node][1]
        print(node)
    count += 1
print(count)


puzzle.answer_a = count