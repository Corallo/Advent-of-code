#from ..input_parser import get_data
from aocd import get_data
from aocd import submit
from aocd.models import Puzzle
import numpy as np
import re
session_id = open("Session", "r").read()
data = get_data(day=5, year=2024,session=session_id)
"""
with open('day 5/data.txt', 'r') as file:
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
    valid = True,
    for i in range(len(manual)-1,0,-1):
        k = np.where(rules[:,0] == manual[i])[0]
        relevant_rules = rules[k,1]
        for j in range(0,i):
            if manual[j] in relevant_rules:
                valid = False
                break
    if valid:
        #print(manual)
        result += manual[len(manual)//2]
    else:
        print(manual,",")
print(result)


#submit(result, part="a", day=5, year=2024, session=session_id)