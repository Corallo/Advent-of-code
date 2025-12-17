#from ..input_parser import get_data
from aocd import get_data
from aocd import submit

session_id = open("Session", "r").read()
data = get_data(day=1, year=2025, session=session_id)

data = data.split("\n")
data = [[d[0], int(d[1:])] for d in data]
print(data)

value = 50
solution = 0

for d in data:
    print("Value:", value)
    if d[0] == "L":
        value -= d[1]
        print("Left:", d[1])
    else:
        value += d[1]
        print("Right:", d[1])
    value = value % 100
    print("New Value:", value)
    if value == 0:
        solution += 1
print(solution)

submit(solution, part="a", day=1, year=2025, session=session_id)