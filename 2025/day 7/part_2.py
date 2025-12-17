#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from functools import lru_cache

session_id = open("Session", "r").read()
data = get_data(day=7, year=2025, session=session_id)
#with open("./2025/day 7/data.txt", "r") as f:
#    data = f.read()
print(data)
data = data.splitlines()
print(data)

# find start coordinates
start = (0,0)
for i in range(len(data[0])):
    if data[0][i] == "S":
        start = (0,i)
        break
print(f"Start coordinates: {start}")
beams = [start]

@lru_cache
def move_beam(beam):
    x, y = beam
    total=0
    if x + 1 < len(data):
        if data[x+1][y] == ".":
            total+=move_beam((x+1, y))
        elif data[x+1][y] == "^":
            total+=move_beam((x+1, y+1))
            total+=move_beam((x+1, y-1))
        return total
    else:
        return 1

answer=move_beam(start)
submit(answer, part="b", day=7, year=2025, session=session_id)