#from ..input_parser import get_data
from aocd import get_data
from aocd import submit

session_id = open("Session", "r").read()
data = get_data(day=2, year=2025, session=session_id)
data = data.split(",")
data = [[int(d.split("-")[0]),int(d.split("-")[1])] for d in data]
print(data)

answer = 0
for r in data:
    for i in range(r[0], r[1]+1):
        s = str(i)
        if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
            print(f"Found matching number: {i}")
            answer += i

submit(answer, part="a", day=2, year=2025, session=session_id)