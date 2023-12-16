from aocd.models import Puzzle
import numpy as np
YEAR = 2023
DAY = 14
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
data = data.split("\n")
data = [list(line) for line in data]

data= np.array(data)
border = np.array([["#" for i in range(len(data[0]))] for j in range(1)])
data = np.concatenate((border,data),axis=0)
def push_up(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                k=0
                for k in range(i-1,-1,-1):
                    if grid[k][j] != ".":
                        break
                grid[i][j] = "."
                grid[k+1][j] = "O"

    return grid

def evaluate_board(grid):
    _grid  = np.array(grid)
    _grid = _grid[::-1]
    score = 0
    for i, line in enumerate(_grid):
        c=np.sum(line=="O")
        score += c*(i+1)
    return score

grid = data.copy()
print(grid)
#save grid to file
np.savetxt("Day 14/grid_1.txt", grid, fmt="%s")

grid=push_up(grid)
print(grid)
np.savetxt("Day 14/grid_2.txt", grid, fmt="%s")
result=evaluate_board(grid)

puzzle.answer_a = result