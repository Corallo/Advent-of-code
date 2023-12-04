#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
session_id = open("Session", "r").read()
data = get_data(day=1, year=2023,session=session_id)

data = data.split("\n")
for i in range(len(data)):
    data[i] = [str(c) for c in data[i] if c.isdigit()]



print(data)
answer = 0
for i in range(len(data)):
    answer += int(data[i][0]+data[i][-1])
print(answer)
submit(answer, part="a", day=1, year=2023, session=session_id)
