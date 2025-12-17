#from ..input_parser import get_data
from aocd import get_data
from aocd import submit

session_id = open("Session", "r").read()
data = get_data(day=3, year=2025, session=session_id)
#with open("./2025/day 3/data.txt", "r") as f:
#    data = f.read()
data = data.split("\n")

answer = 0
for d in data:
    max_power = 0
    for i in range(0,len(d)):
        for j in range(i+1,len(d)):
            if max_power < int(d[i]+d[j]):
                max_power = int(d[i]+d[j])
    print(max_power)
    answer += max_power
        
submit(answer, part="a", day=3, year=2025, session=session_id)