#from ..input_parser import get_data
from aocd import get_data
from aocd import submit

session_id = open("Session", "r").read()
data = get_data(day=4, year=2025, session=session_id)
#with open("./2025/day 3/data.txt", "r") as f:
#    data = f.read()
data = data.split("\n")

def count_adjacent(x, y, grid):
    count = 0
    directions = [(-1, -1), (-1, 0),    (-1, 1),
                  (0, -1),              (0, 1),
                  (1,-1),   (1,0),      (1,1)]
    # count how many @ are adjacent to (x, y)
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == '@':
                count += 1
    return count

answer = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '@' and count_adjacent(i, j, data) < 4:
            print(f"Position ({i}, {j}) can be accessed.")
            answer += 1
print(answer)
        


        
submit(answer, part="a", day=4, year=2025, session=session_id)