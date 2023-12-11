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
original_data = data
data = np.array(original_data)
n = 2
data_points = []

for expansion in range(n):
    print("Iteration ", expansion)
    print("Expanding y axis")
    y=0
    while y < len(data)-1:
        if all(v == "." for v in data[y]):
            for k in range (expansion):
                data = np.insert(data, y, data[y], axis=0)
            y += expansion
        y+=1

    print("Expanding x axis")
    x=0
    while x < len(data[0])-1:
        if all(v == "." for v in data[:,x]):
            for k in range(expansion):
                data = np.insert(data, x, data[:,x], axis=1)
            x += expansion
        x+=1

    #Find coordinates of "#"
    coords = np.where(data == "#")
    coords = list(zip(coords[0], coords[1]))

    #Find all shortest paths between all nodes
    result = 0
    print("Calculating distances")
    for i in range(len(coords)):
        for j in range(i+1, len(coords)):
            distance = abs(coords[i][0] - coords[j][0]) + abs(coords[i][1] - coords[j][1])
            result += distance
    data_points.append(result)
    print(result)


#Find linear function that fits data_points

slope = (data_points[1] - data_points[0]) / 1
print(slope)
y_intercept = data_points[0]
print(y_intercept)

def f(x):
    return slope*x + y_intercept

result = int(f(1000000-1))

puzzle.answer_b = result