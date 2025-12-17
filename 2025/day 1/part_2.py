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
rotations = []

for d in data:
    v = d[1] if d[0] == "R" else -d[1]
    rotations.append(v)

for d in rotations:
    if d < 0:
        if value == 0:  
            solution -= 1
        value += d
        solution += -((value - 1) // 100)
    else:
        value += d
        solution += value // 100
        
    value %= 100

print("Final Value:", value)
print(solution)
submit(solution, part="b", day=1, year=2025, session=session_id)