#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
session_id = open("Session", "r").read()
data = get_data(day=1, year=2024,session=session_id)


data = data.split("\n")
data = [[int(d.split("   ")[0]), int(d.split("   ")[1])] for d in data]
data = np.array(data)

list_1 = data[:,0]
list_2 = data[:,1]

score = 0
for i in range(len(list_1)):
    num = list_1[i]
    occurency = np.sum(num==list_2)
    score += num*occurency


print(score)

answer= score
submit(answer, part="b", day=1, year=2024, session=session_id)