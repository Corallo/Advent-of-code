#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
session_id = open("Session", "r").read()
data = get_data(day=5, year=2024,session=session_id)

"""with open('day 5/data.txt', 'r') as file:
    data = file.read()
print(data)
"""
rules, manuals = data.split("\n\n")
#data = [ d.strip() for d in data]
print(rules)
print(manuals)
rules = [[int(r[0:2]), int(r[3:])] for r in rules.split("\n")]
manuals = [m.split(",") for m in manuals.split("\n")]
manuals = [[int(m) for m in manual] for manual in manuals]
rules = np.array(rules)
print("===================")
result = 0
for manual in manuals:
    fixed = False
    for i in range(len(manual)-1,0,-1):
        repeat = True
        while repeat:
            repeat = False
            k = np.where(rules[:,0] == manual[i])[0]
            relevant_rules = rules[k,1]
            for j in range(i-1,-1,-1):
                if manual[j] in relevant_rules:
                    fixed = True
                    tmp = manual[j]
                    manual[j] = manual[i]
                    manual[i] = tmp
                    repeat = True

    if fixed:
        print(manual)
        result += manual[len(manual)//2]

print(result)


#submit(result, part="b", day=5, year=2024, session=session_id)