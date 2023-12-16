from aocd.models import Puzzle
import numpy as np
from tqdm import tqdm
from functools import cache
YEAR = 2023
DAY = 14
puzzle = Puzzle(year=YEAR, day=DAY)

data = puzzle.input_data
#data = puzzle.examples[0][0]
data = data.split("\n")
data = [list(line) for line in data]

data= np.array(data)
#add border up and down
border = np.array([["#" for i in range(len(data[0]))] for j in range(1)])
data = np.concatenate((border,data,border),axis=0)
#add border left and right
border = np.array([["#" for i in range(1)] for j in range(len(data))])
data = np.concatenate((border,data,border),axis=1)
#convert numpy array of list of characters to numpy array 2d
print(data.shape)


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

push_down = lambda grid: push_up(grid[::-1])[::-1]
push_left = lambda grid: push_up(grid.T).T
push_right = lambda grid: push_down(grid.T).T


def evaluate_board(grid):
    _grid  = np.array(grid)
    _grid = _grid[::-1]
    score = 0
    for i, line in enumerate(_grid):
        c=np.sum(line=="O")
        score += c*(i)
    return score

grid = data.copy()
print(grid)

cached_grid= []
done= False
start_loop = 0
original_grid = grid.copy()
i=0
for i in range(1000000000):
    grid = push_up(grid)
    grid = push_left(grid)
    grid = push_down(grid)
    grid = push_right(grid)

    for l, cg in enumerate(cached_grid):
        if np.all(grid==cg):
            done = True
            start_loop = l
            break
    if done:
        break
    cached_grid.append(grid.copy())


loop_chache = cached_grid[start_loop:]
end_position = (1000000000-(i+1))%len(loop_chache)

print(loop_chache[end_position])
result=evaluate_board(loop_chache[end_position])
print(result)
puzzle.answer_b = result