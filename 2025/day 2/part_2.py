#from ..input_parser import get_data
from aocd import get_data
from aocd import submit

session_id = open("Session", "r").read()
data = get_data(day=2, year=2025, session=session_id)


data = data.split(",")
data = [[int(d.split("-")[0]),int(d.split("-")[1])] for d in data]

answer = 0
invalid_id = set()
for r in data:
    print(f"Range: {r}")
    for i in range(r[0], r[1]+1):
        s = str(i)
        for l in range(1, len(s)//2+1):
            if s[:l] * (len(s)//l) == s:
                print(f"Found matching number: {i}")
                invalid_id.add(i)

answer = sum(invalid_id)
print(answer)
#34459250159 too high
submit(answer, part="b", day=2, year=2025, session=session_id)