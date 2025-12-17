#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
import re
session_id = open("Session", "r").read()
data = get_data(day=6, year=2025, session=session_id)
#with open("./2025/day 3/data.txt", "r") as f:
#    data = f.read()
print(data)
numbers = re.split(r"\s+", data.strip())
data = [
    [x for x in line.split()]
    for line in data.splitlines()
    if line.strip()
]
print(len(data), len(data[0]))


def mul_op(a,b):
    return a*b
def add_op(a,b):
    return a+b

op_dict = {"*": mul_op,
            "+": add_op}

answer = 0
for i in range(len(data[0])):
    current_op = op_dict[data[-1][i]]
    print(f"Operation for column {i}: {data[-1][i]}")
    for j in range(len(data)-1):
        if j == 0:
            result = int(data[j][i])
        else:
            result = current_op(result, int(data[j][i]))
    answer += result

print(answer)
submit(answer, part="a", day=6, year=2025, session=session_id)