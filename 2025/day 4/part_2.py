#from ..input_parser import get_data
from aocd import get_data
from aocd import submit

session_id = open("Session", "r").read()
data = get_data(day=4, year=2025, session=session_id)
#with open("./2025/day 3/data.txt", "r") as f:
#    data = f.read()
print(data)
data = data.split("\n")

def count_adjacent(x, y, grid):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1,-1), (1,0),(1,1)]
    # count how many @ are adjacent to (x, y)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == '@':
                count += 1
    return count


def remove_rolls(grid):
    removed = 0
    to_be_removed = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@' and count_adjacent(i, j, grid) < 4:
                print(f"Position ({i}, {j}) can be accessed.")
                removed += 1
                to_be_removed.append((i,j))
    for pos in to_be_removed:
        i, j = pos
        grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
    return removed, grid

answer = 0
while True:
    removed, data = remove_rolls(data)
    answer += removed
    if removed == 0:
        break
print(answer)

        


        
submit(answer, part="b", day=4, year=2025, session=session_id)