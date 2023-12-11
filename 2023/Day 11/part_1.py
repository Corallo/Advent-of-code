from aocd.models import Puzzle
import networkx as nx
import numpy as np
YEAR = 2023
DAY = 11
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
print(data)

data = data.split("\n")
#Split each line of data into a list of characters
data = [list(line) for line  in data]
print(data)


data = np.array(data)
#find lines with only "." and duplicate them and insert next to the original
y=0
while y < len(data)-1:
    print (y, data[y])
    if all(v == "." for v in data[y]):
        data = np.insert(data, y, data[y], axis=0)
        y += 1
    y+=1


#find columns with only "." and duplicate them and insert next to the original
x=0
while x < len(data[0])-1:
    if all(v == "." for v in data[:,x]):
        data = np.insert(data, x, data[:,x], axis=1)
        x += 1
    x+=1

print(data)

#Find coordinates of "#"
coords = np.where(data == "#")
coords = list(zip(coords[0], coords[1]))
print(coords)


#Find all shortest paths between all nodes

result = 0
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        distance = abs(coords[i][0] - coords[j][0]) + abs(coords[i][1] - coords[j][1])
        print(i, j, distance)
        result += distance

print(result)



puzzle.answer_a = result